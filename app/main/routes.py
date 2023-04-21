'''importing python libraries and modules'''
from datetime import datetime
from langdetect import detect, LangDetectException

'''importing flask methods and libraries'''
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from flask_babel import get_locale

'''importing objects, methods, and scripts from the application'''
from app import app, db
from app.main.forms import *
from app.models import User, Post
from app.main import bp


@bp.before_request
def before_request():
    '''The current_user variable has as it's value the value from the "id"
field of the User model. That "id" value corresponds to the user object for
the given session, which contains the other User fields; namely, the last_seen
field.'''
    
    
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        
        
    g.locale = str(get_locale())
    
    
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    '''This is the homepage of the site. The @login_required decorator from
Flask-Login sets accessibility restrictions to only those users who are logged
in.'''
    
    
    form = PostForm()
    if form.validate_on_submit():
        '''We access the PostForm form from the forms.py file and transfer
    the data from the TextAreaField to the body of the Post model in the
    models.py file.'''
        
        
        try:
            language = detect(form.post.data)
            
        except LangDetectException:
            language = ''
            
            
        post = Post(body=form.post.data, author=current_user, language=language)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))
    
    
    page = request.args.get('page', 1, type=int)
    '''This request.args.get() call takes in the parsed contents of a URL
query string, which is the part of the URL after the question mark in the
following formated URL
    
<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    
The parsed contents of the query string are keys in a Python dictionary. The
value of this "page" key corresponds to the same object on which a limit of
posts per view has been set in our config.py file under the "POSTS_PER_PAGE"
key. We paginate with respect to posts from those we follow and our own posts,
which is clear from the variable definitions and "return" statement of the
"followed_posts" function of our models.py file, starting from page 1, where
the pages are ordered by descending timestamp in the "followed_posts" function
of our models.py file.'''
    
    
    posts = current_user.followed_posts().paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('main.index', page=posts.next_num)\
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num)\
        if posts.has_prev else None
    
    
    return render_template('index.html', title='MassiveDiscipline',
        form = form, posts=posts.items, next_url=next_url, prev_url=prev_url)


@bp.route('/explore')
@login_required
def explore():
    '''We grab page 1 from the URL query string for the list of posts, which
we have set to a limit under the ['POSTS_PER_PAGE'] key within config.py. The
"error_out" keyword is set to False so that when out-of-range pages are
accessed, instead of a 404 error being thrown, an empty list for the
out-of-range pages will be returned.'''
    
    
    page = request.args.get('page', 1, type=int)
    '''This request.args.get() call takes in the parsed contents of a URL
query string, which is the part of the URL after the question mark in the
following formated URL
    
<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    
The parsed contents of the query string are keys in a Python dictionary. The
value of this "page" key corresponds to the same object on which a limit of
posts per view has been set in our config.py file under the "POSTS_PER_PAGE"
key. We paginate with respect to all posts from the database,
starting from page 1, where the pages are ordered by descending
timestamp.'''
    
    
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('main.explore', page=posts.next_num)\
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num)\
        if posts.has_prev else None
    
    
    return render_template('index.html', title='MassiveDiscipline',
        posts=posts.items, next_url=next_url, prev_url=prev_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    '''This is the profile page of the logged in user. The <username> dynamic
component in the @app.route function accepts the username from this user
function, which takes as an argument the username corresponding to the value of
the relevant form variable input by the user at the login view function.'''
    
    
    user = User.query.filter_by(username=username).first_or_404()
    '''If the username exists, it will be unique and thus, the first to be
encountered in a query to the database. If the username does not exist, then
an 404 exception is raised. The user variable now points to the User model and
all of its field values for the user holding this specific username. We use
this to coordinate post entries through our _post.html file so that they may
render on the webpage.'''
    
    
    page = request.args.get('page', 1, type=int)
    '''This request.args.get() call takes in the parsed contents of a URL
query string, which is the part of the URL after the question mark in the
following formated URL
    
<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    
The parsed contents of the query string are keys in a Python dictionary. The
value of this "page" key corresponds to the same object on which a limit of
posts per view has been set in our config.py file under the "POSTS_PER_PAGE"
key. We paginate with respect to posts from the self user,
which correspond to the "posts" variable of our User model in the models.py
file, starting from page 1, where the pages are ordered by descending
timestamp.'''
    
    
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('main.user', username=user.username, \
        page=posts.next_num)\
        if posts.has_next else None
    prev_url = url_for('main.user', username=user.username, \
        page=posts.prev_num)\
        if posts.has_prev else None
    
    
    form = EmptyForm()
    '''Hitting the sumbit button for this EmptyForm form will signal this
viewfunction to render the form in POST, which will process the information
according to the "follow" viewfunction being accessed by the
"user.html" template.'''
    
    
    return render_template('user.html', user=user, posts=posts.items,
        next_url=next_url, prev_url=prev_url, form=form)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    '''Upon intializing this view function for the first time, the user object
will reference the current_user variable for username and about_me field
values to store in the respective EditProfileForm form positions. (The elif
statement is evaluating True in this scenario.) Upon
subsequent initializations, the form, prepopulated with field values obtained
in the first initialization, will supply the current_user variable with those
relevant field values chosen, in-edit, by the user. (The if statement is
evaluating True in this scenario.)'''
    
    
    form = EditProfileForm(current_user.username)
    '''The curren_user.username argument will need to be removed when testing
the app with the goal of displaying the 500 error message template.'''
    
    
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        
        
    return render_template('edit_profile.html', title='MassiveDiscipline',\
        form=form)


@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    '''We call the EmptyForm by pressing the submit button, which reads as
"Follow" when the user-to-user relationship warrants such a readout. If the
validation fails, it is because the CSRF token is invalid.

The "user" variable here corresponds to the user whom the "current_user" wishes
to follow.'''
    
    
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('main.index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('main.user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('main.user', username=username))
    
    
    else:
        return redirect(url_for('main.index'))
    
    
@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    '''We call the EmptyForm by pressing the submit button, which reads as
"Unfollow" when the user-to-user relationship warrants such a readout. If the
validation fails, it is because the CSRF token is invalid.

The "user" variable here corresponds to the user whom the "current_user" wishes
to unfollow.'''
    
    
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found'.format(username))
            return redirect(url_for('main.index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('main.user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}'.format(username))
        return redirect(url_for('main.user', username=username))
    
    
    else:
        return redirect(url_for('main.index'))