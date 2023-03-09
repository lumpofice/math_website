'''importing python libraries and modules'''
from datetime import datetime

'''importing flask methods and libraries'''
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

'''importing objects, methods, and scripts from the application'''
from app import app, db
from app.forms import *
from app.geometric_series import GeometricSeries
from app.polynomial_degree_1_transform import PolynomialDegree1Transform
from app.polynomial_degree_2_transform import PolynomialDegree2Transform
from app.polynomial_degree_3_transform import PolynomialDegree3Transform
from app.absolute_value_transform import AbsoluteValueTransform
from app.reciprocal_degree_0_by_degree_1_transform import\
    ReciprocalDegree0ByDegree1Transform
from app.square_root_transform import SquareRootTransform
from app.cube_root_transform import CubeRootTransform
from app.general_exponential_transform import GeneralExponentialTransform
from app.general_logarithmic_transform import GeneralLogarithmicTransform
from app.base_e_exponential_transform import BaseEExponentialTransform
from app.base_e_logarithmic_transform import BaseELogarithmicTransform
from app.models import User, Post
from app.email import send_password_reset_email

'''importing computational libraries'''
import numpy as np


@app.before_request
def before_request():
    '''The current_user variable has as it's value the value from the "id"
field of the User model. That "id" value corresponds to the user object for
the given session, which contains the other User fields; namely, the last_seen
field.'''
    
    
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''This is the login page, to which anonymous users will be directed,
while nonanonymous users will see, in place of the "login" link in the header,
a link in the header allowing them to "logout" of the site.'''
    
    
    if current_user.is_authenticated:
        '''The "current_user" variable can take on the "id" provided by the
    "load_user" function written into the "models.py" script, if such an "id"
    already exists. This "id" comes from the database and is the value for
    the variable, current_user, which is the user object
    representing the client of the request. If such "id" does exist, the
    variable's value indicates that the user is non-anonymous (is logged in),
    and then this if statement returns True to redirect the user to the index
    page. However, in the event that this if statement returns False, this
    python script proceeds to load the login form webpage.'''
        
        
        return redirect(url_for('index'))
    
    
    form = LoginForm()
    
    
    if form.validate_on_submit():
        '''This if statement queries the database for the username, grabbing
    the first entry with that username. The User model sets a unique
    qualification for this field. Thus, there is no chance of us drawing the
    wrong account through this query.'''
        
        
        user = User.query.filter_by(username=form.username.data).first()
        '''This variable takes on the username input to the login form by
    the user. Given that username is a unique field in the User model, we
    conclude our query at the first encountered match.'''
        
        
        if user is None or not user.check_password(form.password.data):
            '''If the user is anonymous, meaning the user has not already
        logged in, or if the password input to the login form does not return
        the password hash that has been stored to the database for the specific
        username input into the same login form, then this if statement will
        reload the login form page, with all data entry positions blank,
        flashing a notice to the user that the credentials that were input are
        incorrect. However, if the user is authenticated, then this if
        statement evaluates to False; the script moves on to log in the user.'''
            
            
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        
        login_user(user, remember=form.remember_me.data)
        '''Once the user is authenticated, this function will log the user into
    the application. If the user wishes to be remembered, they simply check
    the "Remember Me" box, and the login_user function passes a value of "True"
    to the "remember" parameter.'''
        
        
        next_page = request.args.get('next')
        '''This request.args.get() call takes in the parsed contents of a URL
    query string, which is the part of the URL after the question mark in the
    following formated URL
    
    <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    
    The parsed contents of the query string are keys in a Python dictionary.
    The value of this "next" key is the webpage the user wishes to access yet
    cannot due to the fact that they have not yet logged in. Thus,
    the anonymous user is redirected to the login form page upon clicking
    a link within the application that requires users be logged in before
    accessing. The link that the user has clicked is stored as the
    value for this "next" key, and it is accessed once the user has
    successfully logged in.'''
        
        
        if not next_page or url_parse(next_page).netloc != '':
            '''This if statement checks whether the variable next_page has a
        value of True or if the url_parse(next_page) is a relative URL using
        the .netloc method. If url_parse(next_page) is a relative path, then
        it has no hostname. With no hostname, we return to the index page of
        the application.'''
            
            
            next_page = url_for('index')
            
            
        return redirect(next_page)
    
    
    return render_template('login.html', title='MassiveDiscipline', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''First-time visitors to this page may register by submitting a pair of
email and password credentials to the login page of the site.

Upon initially opening this page, given that there is yet no input,
the browser's GET method will process the empty form, yielding a value of
False for the "if form.validate_on_submit()" line, bringing the function
to the return statement below, which populates the page anew for the user
to provide input.'''
    
    
    if current_user.is_authenticated:
        '''The "current_user" variable can take on the "id" provided by the
    "load_user" function written into the "models.py" script, if such an "id"
    already exists. This "id" comes from the database and is the value for
    the variable, current_user, which is the user object
    representing the client of the request. If such "id" does exist, the
    variable's value indicates that the user is non-anonymous (is logged in),
    and then this if statement returns True to redirect the user to the index
    page. However, in the event that this if statement returns False, this
    python script proceeds to load the registration form webpage.'''
        
        
        return redirect(url_for('index'))
    
    
    form = RegistrationForm()
    
    
    if form.validate_on_submit():
        '''Upon submitting the form, the browser's POST request submits
    the form data to the server, and when the data meets validator expectations,
    this if statement returns True, redirecting the user ro the "login" page.'''
        
        
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    
    
    return render_template('register.html', title='MassiveDiscipline',\
        form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
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
        
        
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    
    
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
    next_url = url_for('index', page=posts.next_num)\
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num)\
        if posts.has_prev else None
    
    
    return render_template('index.html', title='MassiveDiscipline',
        form = form, posts=posts.items, next_url=next_url, prev_url=prev_url)


@app.route('/user/<username>')
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
    next_url = url_for('user', username=user.username, page=posts.next_num)\
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num)\
        if posts.has_prev else None
    
    
    form = EmptyForm()
    '''Hitting the sumbit button for this EmptyForm form will signal this
viewfunction to render the form in POST, which will process the information
according to the "follow" viewfunction being accessed by the
"user.html" template.'''
    
    
    return render_template('user.html', user=user, posts=posts.items,
        next_url=next_url, prev_url=prev_url, form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
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
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        
        
    return render_template('edit_profile.html', title='MassiveDiscipline',\
        form=form)


@app.route('/follow/<username>', methods=['POST'])
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
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('user', username=username))
    
    
    else:
        return redirect(url_for('index'))
    
    
@app.route('/unfollow/<username>', methods=['POST'])
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
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}'.format(username))
        return redirect(url_for('user', username=username))
    
    
    else:
        return redirect(url_for('index'))


@app.route('/explore')
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
    next_url = url_for('explore', page=posts.next_num)\
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num)\
        if posts.has_prev else None
    
    
    return render_template('index.html', title='MassiveDiscipline',
        posts=posts.items, next_url=next_url, prev_url=prev_url)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    '''This function sends out the email used to prompt the user towards a
password reset.'''
    
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    
    form = ResetPasswordRequestForm()
    
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        
        if user:
            '''Once the form is validated, we use the send_password_reset_email
        method, bearing the user's email as an argument, from the email.py file
        to generate a token and send it to the user via email.'''
            
            
            send_password_reset_email(user)
            
            
        flash('An instructional email has been sent.')
        return redirect(url_for('login'))
    
    
    return render_template('reset_password_request.html',
        title='Massive Discipline', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/score')
@login_required
def score():
    '''This is the page on which I am keeping score of the success students
are meeting in my course. The @login_required decorator from
Flask-Login sets accessibility restrictions to only those users who are logged
in.'''
    
    
    return render_template('score.html', title='MassiveDiscipline')


@app.route('/logout')
def logout():
    '''This is the "logout" link nonanonymous users will see in the header
once they are logged into the site.'''
    
    
    logout_user()
    return redirect(url_for('index'))


@app.route('/geometric_series', methods=['GET', 'POST'])
def geometric_series():
    '''This function constructs a graph of the geometric series, from parametes
input by the user.'''
    
    
    form = GeometricSeriesForm()
    
    
    if form.validate_on_submit():
        flash('Base: {}, Scalar: {}, epsilon: {}, Large m: {}'\
            .format(form.base.data, form.scalar.data, form.epsilon.data,\
            form.large_m.data))
        geo = GeometricSeries()
        geo.graph(form.base.data, form.scalar.data, form.epsilon.data,\
            form.large_m.data)
        return redirect(url_for('geometric_series_graph_results'))
    
    
    return render_template('geometric_series.html', title='MassiveDiscipline',\
        form=form)


@app.route('/geometric_series_graph_results')
def geometric_series_graph_results():
    '''This function displays the graph of the geometric series constructed
from parameters input by the user.'''
    
    
    return render_template(\
        'geometric_series_graph_results.html', title='MassiveDiscipline')


@app.route('/polynomial_degree_1_transform', methods=['GET', 'POST'])
def polynomial_degree_1_transform():
    '''This function constructs the graph of the parent polynomial degree 1
function, overlaid by a transformed polynomial degree 1 function, based on
transformations input by the user.'''
    
    
    form = PolynomialDegree1TransformForm()
    
    
    if form.validate_on_submit():
            
            
        if form.y_scalar.data == 0:
            flash('Parent Function Only')
        
        
        else:
            flash('h = {} ____ a = {} ____ k = {} ____ '\
                'domain = ({}, {}) ____ '\
                'range = ({}, {})'\
                .format(form.horizontal_shift.data, form.y_scalar.data,\
                form.vertical_shift.data, -np.inf, np.inf,\
                -np.inf, np.inf))
    
    
        id_transform = PolynomialDegree1Transform()
        id_transform.graph(form.horizontal_shift.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'polynomial_degree_1_transform_graph_results'))
    
    
    return render_template(\
        'polynomial_degree_1_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/polynomial_degree_1_transform_graph_results')
def polynomial_degree_1_transform_graph_results():
    '''This function displays the parent and transformed polynomial degree 1
functions.'''
    
    
    return render_template(\
        'polynomial_degree_1_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/polynomial_degree_2_transform', methods=['GET', 'POST'])
def polynomial_degree_2_transform():
    '''This function constructs the graph of the parent polynomial degree 2
function, overlaid by a transformed polynomial degree 2 function, based on
transformations input by the user.'''
    
    
    form = PolynomialDegree2TransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
        
        
            if form.y_scalar.data >= 0:
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    form.vertical_shift.data, np.inf))
        
        
            elif form.y_scalar.data < 0:
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    -np.inf, form.vertical_shift.data))
    
    
        square_transform = PolynomialDegree2Transform()
        square_transform.graph(form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data, form.y_scalar.data,\
            form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'polynomial_degree_2_transform_graph_results'))
    
    
    return render_template(\
        'polynomial_degree_2_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/polynomial_degree_2_transform_graph_results')
def polynomial_degree_2_transform_graph_results():
    '''This function displays the parent and transformed polynomial degree 2
functions.'''
    
    
    return render_template(\
        'polynomial_degree_2_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/polynomial_degree_3_transform', methods=['GET', 'POST'])
def polynomial_degree_3_transform():
    '''This function constructs the graph of the parent polynomial degree 3
function, overlaid by a transformed polynomial degree 3 function, based on
transformations input by the user.'''
    
    
    form = PolynomialDegree3TransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                'k = {} ____ '\
                'domain = ({}, {}) ____ '\
                'range = ({}, {})'\
                .format(form.horizontal_shift.data, form.x_scalar.data,\
                form.x_reflection.data, form.y_scalar.data,\
                form.vertical_shift.data, -np.inf, np.inf,\
                -np.inf, np.inf))
    
    
        cubed_transform = PolynomialDegree3Transform()
        cubed_transform.graph(form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data, form.y_scalar.data,\
            form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'polynomial_degree_3_transform_graph_results'))
    
    
    return render_template(\
        'polynomial_degree_3_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/polynomial_degree_3_transform_graph_results')
def polynomial_degree_3_transform_graph_results():
    '''This function displays the parent and transformed polynomial degree 3
functions.'''
    
    
    return render_template(\
        'polynomial_degree_3_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/absolute_value_transform', methods=['GET', 'POST'])
def absolute_value_transform():
    '''This function constructs the graph of the parent absolute value
function, overlaid by a transformed absolute value function, based on
transformations input by the user.'''
    
    
    form = AbsoluteValueTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            
            
            if form.y_scalar.data > 0:
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    form.vertical_shift.data, np.inf))
            
            
            elif form.y_scalar.data < 0:
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    -np.inf, form.vertical_shift.data))
    
    
        absolute_value_transform = AbsoluteValueTransform()
        absolute_value_transform.graph(\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'absolute_value_transform_graph_results'))
    
    
    return render_template(\
        'absolute_value_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/absolute_value_transform_graph_results')
def absolute_value_transform_graph_results():
    '''This function displays the parent and transformed absolute value
functions.'''
    
    
    return render_template(\
        'absolute_value_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/reciprocal_degree_0_by_degree_1_transform',\
methods=['GET', 'POST'])
def reciprocal_degree_0_by_degree_1_transform():
    '''This function constructs the graph of the parent reciprocal
function, with polynomial degree 0 in the numerator and polynomial degree 1
in the denominator, overlaid by a transformed reciprocal function, with
polynomial degree 0 in the numerator and polynomial degree 1 in the denominator,
based on transformations input by the user.'''
    
    
    form = ReciprocalDegree0ByDegree1TransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                'k = {} ____ '\
                'domain = {{x : x < {} and {} < x}} ____ '\
                'range = {{g(x) : g(x) < {} and {} < g(x)}} ____ '\
                'VA: x = {} ____ '\
                'HA: y = {}'\
                .format(form.horizontal_shift.data, form.x_scalar.data,\
                form.x_reflection.data, form.y_scalar.data,\
                form.vertical_shift.data,\
                form.horizontal_shift.data, form.horizontal_shift.data,\
                form.vertical_shift.data, form.vertical_shift.data,\
                form.horizontal_shift.data, form.vertical_shift.data))
    
    
        reciprocal_transform = ReciprocalDegree0ByDegree1Transform()
        reciprocal_transform.graph(\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'reciprocal_degree_0_by_degree_1_transform_graph_results'))
    
    
    return render_template(\
        'reciprocal_degree_0_by_degree_1_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/reciprocal_degree_0_by_degree_1_transform_graph_results')
def reciprocal_degree_0_by_degree_1_transform_graph_results():
    '''This function displays the parent and transformed reciprocal
functions, with numerators having polynomials degree 0 and denominators
have polynomials degree 1.'''
    
    
    return render_template(\
        'reciprocal_degree_0_by_degree_1_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/square_root_transform',\
methods=['GET', 'POST'])
def square_root_transform():
    '''This function constructs the graph of the parent square root
function, overlaid by a transformed square root function, based on
transformations input by the user.'''
    
    
    form = SquareRootTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.y_scalar.data >= 0:
            
            
            if form.x_reflection.data >= 0:
            
            
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, form.horizontal_shift.data,\
                    np.inf,\
                    form.vertical_shift.data, np.inf))
                
                
            if form.x_reflection.data < 0:
                
                
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf,\
                    -form.horizontal_shift.data,\
                    form.vertical_shift.data, np.inf))
        
        
        if form.y_scalar.data < 0:
            
            
            if form.x_reflection.data >= 0:
            
            
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, form.horizontal_shift.data,\
                    np.inf,\
                    -np.inf, form.vertical_shift.data))
                
                
            if form.x_reflection.data < 0:
                
                
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {})'\
                    .format(form.horizontal_shift.data, form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf,
                    -form.horizontal_shift.data,\
                    np.inf, form.vertical_shift.data))
    
    
        square_root_transform = SquareRootTransform()
        square_root_transform.graph(\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data, form.y_scalar.data,\
            form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'square_root_transform_graph_results'))
    
    
    return render_template(\
        'square_root_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/square_root_transform_graph_results')
def square_root_transform_graph_results():
    '''This function displays the parent and transformed square root
functions.'''
    
    
    return render_template(\
        'square_root_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/cube_root_transform',\
methods=['GET', 'POST'])
def cube_root_transform():
    '''This function constructs the graph of the parent cube root
function, overlaid by a transformed cube root function, based on
transformations input by the user.'''
    
    
    form = CubeRootTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                'k = {} ____ '\
                'domain = ({}, {}) ____ '\
                'range = ({}, {})'\
                .format(form.horizontal_shift.data, form.x_scalar.data,\
                form.x_reflection.data, form.y_scalar.data,\
                form.vertical_shift.data, -np.inf, np.inf,\
                -np.inf, np.inf))
    
    
        cube_root_transform = CubeRootTransform()
        cube_root_transform.graph(\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'cube_root_transform_graph_results'))
    
    
    return render_template(\
        'cube_root_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/cube_root_transform_graph_results')
def cube_root_transform_graph_results():
    '''This function displays the parent and transformed cube root
functions.'''
    
    
    return render_template(\
        'cube_root_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/general_exponential_transform',\
methods=['GET', 'POST'])
def general_exponential_transform():
    '''This function constructs the graph of the parent general exponential
function, overlaid by a transformed general exponential function, based on
transformations input by the user.'''
    
    
    form = GeneralExponentialTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            
            
            if form.y_scalar.data > 0:
                flash('B = {} ____ h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ HA: y = {}'\
                    .format(form.base.data, form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    form.vertical_shift.data, np.inf, form.vertical_shift.data))
                
                
            elif form.y_scalar.data < 0:
                flash('B = {} ____ h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ HA: y = {}'\
                    .format(form.base.data, form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    -np.inf, form.vertical_shift.data,\
                    form.vertical_shift.data))
    
    
        general_exponential_transform = GeneralExponentialTransform()
        general_exponential_transform.graph(\
            form.base.data,\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'general_exponential_transform_graph_results'))
    
    
    return render_template(\
        'general_exponential_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/general_exponential_transform_graph_results')
def general_exponential_transform_graph_results():
    '''This function displays the parent and transformed general exponential
functions.'''
    
    
    return render_template(\
    'general_exponential_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/general_logarithmic_transform',\
methods=['GET', 'POST'])
def general_logarithmic_transform():
    '''This function constructs the graph of the parent general logarithmic
function, overlaid by a transformed general logarithmic function, based on
transformations input by the user.'''
    
    
    form = GeneralLogarithmicTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            
            
            if form.x_reflection.data > 0:
                flash('B = {} ____ h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ VA: x = {}'\
                    .format(form.base.data, form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, form.horizontal_shift.data,\
                    np.inf,\
                    -np.inf, np.inf, form.horizontal_shift.data))
                
                
            elif form.x_reflection.data < 0:
                flash('B = {} ____ h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ VA: x = {}'\
                    .format(form.base.data, form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf,\
                    (-1)*form.horizontal_shift.data,\
                    -np.inf, np.inf, (-1)*form.horizontal_shift.data))
    
    
        general_logarithmic_transform = GeneralLogarithmicTransform()
        general_logarithmic_transform.graph(\
            form.base.data,\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'general_logarithmic_transform_graph_results'))
    
    
    return render_template(\
        'general_logarithmic_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/general_logarithmic_transform_graph_results')
def general_logarithmic_transform_graph_results():
    '''This function displays the parent and transformed general logarithmic
functions.'''
    
    
    return render_template(\
        'general_logarithmic_transform_graph_results.html',\
        title='MassiveDiscipline')


@app.route('/base_e_exponential_transform',\
methods=['GET', 'POST'])
def base_e_exponential_transform():
    '''This function constructs the graph of the parent base e exponential
function, overlaid by a transformed base e exponential function, based on
transformations input by the user.'''
    
    
    form = BaseEExponentialTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            
            
            if form.y_scalar.data > 0:
                flash('h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ HA: y = {}'\
                    .format(form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    form.vertical_shift.data, np.inf, form.vertical_shift.data))
                
                
            elif form.y_scalar.data < 0:
                flash('h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ HA: y = {}'\
                    .format(form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf, np.inf,\
                    -np.inf, form.vertical_shift.data,\
                    form.vertical_shift.data))
    
    
        base_e_exponential_transform = BaseEExponentialTransform()
        base_e_exponential_transform.graph(\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'base_e_exponential_transform_graph_results'))
    
    
    return render_template(\
        'base_e_exponential_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/base_e_exponential_transform_graph_results')
def base_e_exponential_transform_graph_results():
    '''This function displays the parent and transformed base e exponential
functions.'''
    
    
    return render_template(\
    'base_e_exponential_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/base_e_logarithmic_transform',\
methods=['GET', 'POST'])
def base_e_logarithmic_transform():
    '''This function constructs the graph of the parent base e logarithmic
function, overlaid by a transformed base e logarithmic function, based on
transformations input by the user.'''
    
    
    form = BaseELogarithmicTransformForm()
    
    
    if form.validate_on_submit():
        
        
        if form.x_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.y_scalar.data == 0:
            flash('Parent Function Only')
            
            
        elif form.x_reflection.data == 0:
            flash('Parent Function Only')
        
        
        else:
            
            
            if form.x_reflection.data > 0:
                flash('h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ VA: x = {}'\
                    .format(form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, form.horizontal_shift.data,\
                    np.inf,\
                    -np.inf, np.inf, form.horizontal_shift.data))
                
                
            elif form.x_reflection.data < 0:
                flash('h = {} ____ b = {} ____ c = {} ____ '\
                    'a = {} ____ '\
                    'k = {} ____ '\
                    'domain = ({}, {}) ____ '\
                    'range = ({}, {}) ____ VA: x = {}'\
                    .format(form.horizontal_shift.data,\
                    form.x_scalar.data,\
                    form.x_reflection.data, form.y_scalar.data,\
                    form.vertical_shift.data, -np.inf,\
                    (-1)*form.horizontal_shift.data,\
                    -np.inf, np.inf, (-1)*form.horizontal_shift.data))
    
    
        base_e_logarithmic_transform = BaseELogarithmicTransform()
        base_e_logarithmic_transform.graph(\
            form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data,\
            form.y_scalar.data, form.vertical_shift.data)
        
        
        return redirect(url_for(\
            'base_e_logarithmic_transform_graph_results'))
    
    
    return render_template(\
        'base_e_logarithmic_transform.html',\
        title='MassiveDiscipline',\
        form=form)


@app.route('/base_e_logarithmic_transform_graph_results')
def base_e_logarithmic_transform_graph_results():
    '''This function displays the parent and transformed base e logarithmic
functions.'''
    
    
    return render_template(\
        'base_e_logarithmic_transform_graph_results.html',\
        title='MassiveDiscipline')