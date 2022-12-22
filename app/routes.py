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

'''importing computational libraries'''
import numpy as np


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
        
        
        if user is None or not user.check_password(form.password.data):
            '''If the user is anonymous, meaning the user has not already
        logged in, or if the password input to the login form does not return
        the password hash that has been stored to the database for the specific
        username input into the same login form, then this if statement will
        reload the login form page, with all data entry positions blank,
        flashing a notice to the user that the credentials that were input are
        incorrect.'''
            
            
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        '''This request.args.get() call takes in the parsed contents of a URL
    query string, which is the part of the URL after the question mark. The
    parsed contents of the query string are keys in a Python dictionary. The
    value of this "next" key is the webpage the user wishes to access yet cannot
    due to the fact that they have yet to log in. Given they have not yet logged
    in, the anonymous user is redirected to the login form page upon clicking
    a link within the application that requires users be logged in before
    being able to access. The link that the user has clicked is stored as the
    value for this "next" key, and it is accessed once the user has
    successfully logged in.'''
        
        
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            
            
        return redirect(next_page)
    
    
    return render_template('login.html', title='MassiveDiscipline', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''First-time visitors to this page may register by submitting a pair of
email and password credentials to the login page of the site.'''
    
    
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
    
    
    '''Upon initially opening this page, given that there is yet no input,
the browser's GET method will process the empty form, yielding a value of
False for the "if form.validate_on_submit()" line, bringing the function
to the return statement below, which populates the page anew for the user
to provide input.'''
    return render_template('register.html', title='MassiveDiscipline',\
        form=form)


@app.route('/')
@app.route('/index')
@login_required
def index():
    '''This is the homepage of the site. Currently, posts are displayed on
this page.'''
    
    
    posts = [
        {
            'author': {'username': 'suzanne'},
            'body': 'Beautiful!'
        }
    ]
    
    
    return render_template('index.html', title='MassiveDiscipline', posts=posts)


@app.route('/score')
def score():
    '''This is the page on which I am keeping score of the success students
are meeting in my course.'''
    
    
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