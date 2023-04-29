'''importing flask methods and libraries'''
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

'''importing objects, methods, and scripts from the application'''
from app import db
from app.auth import bp
from app.auth.forms import *
from app.models import User
from app.auth.email import send_password_reset_email


@bp.route('/login', methods=['GET', 'POST'])
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
        
        
        return redirect(url_for('main.index'))
    
    
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
            return redirect(url_for('auth.login'))
        
        
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
            
            
            next_page = url_for('main.index')
            
            
        return redirect(next_page)
    
    
    return render_template('auth/login.html', title='MassiveDiscipline',\
        form=form)


@bp.route('/logout')
def logout():
    '''This is the "logout" link nonanonymous users will see in the header
once they are logged into the site.'''
    
    
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
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
        
        
        return redirect(url_for('main.index'))
    
    
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
        return redirect(url_for('auth.login'))
    
    
    return render_template('auth/register.html', title='MassiveDiscipline',\
        form=form)


@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    '''This function sends out the email used to prompt the user towards a
password reset.'''
    
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    
    form = ResetPasswordRequestForm()
    
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        
        if user:
            '''Once the form is validated, we use the send_password_reset_email
        method, bearing the user's email as an argument, from the email.py file
        to generate a token and send it to the user via email.'''
            
            
            send_password_reset_email(user)
            
            
        flash('An instructional email has been sent.')
        return redirect(url_for('auth.login'))
    
    
    return render_template('auth/reset_password_request.html',
        title='Massive Discipline', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    '''Upon clicking the link within the password reset request email, we are
redirected to the "reset_password" template, with the url_for call carrying
the link-embedded token with us, assuming the
"User.verify_reset_password_token(token)" value is True. If the value is
instead False, then we are redirected to the "index" template.'''
    
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    
    user = User.verify_reset_password_token(token)
    
    
    if not user:
        '''This conditional brings us back to the index view if our token is
    not verified.'''
        
        
        return redirect(url_for('main.index'))
    
    
    form = ResetPasswordForm()
    
    
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    
    
    return render_template('auth/reset_password.html', form=form)