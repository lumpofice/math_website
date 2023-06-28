'''importing python libraries and modules'''
from datetime import datetime
from langdetect import detect, LangDetectException

'''importing flask methods and libraries'''
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
from flask_babel import get_locale

'''importing objects, methods, and scripts from the application'''
from app import db
from app.main.forms import *
from app.models import User
from app.main import bp
from app.main.geometric_series import GeometricSeries
from app.main.polynomial_degree_1_transform import PolynomialDegree1Transform
from app.main.polynomial_degree_2_transform import PolynomialDegree2Transform
from app.main.polynomial_degree_3_transform import PolynomialDegree3Transform
from app.main.absolute_value_transform import AbsoluteValueTransform
from app.main.reciprocal_degree_0_by_degree_1_transform import\
    ReciprocalDegree0ByDegree1Transform
from app.main.square_root_transform import SquareRootTransform
from app.main.cube_root_transform import CubeRootTransform
from app.main.general_exponential_transform import GeneralExponentialTransform
from app.main.general_logarithmic_transform import GeneralLogarithmicTransform
from app.main.base_e_exponential_transform import BaseEExponentialTransform
from app.main.base_e_logarithmic_transform import BaseELogarithmicTransform

'''importing computational libraries'''
import numpy as np


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
 
    if request.method == 'POST':
        if request.form['submit_button'] == 'Precalculus':
            return redirect(url_for('main.precalculus'))
        if request.form['submit_button'] == 'Calculus':
            return redirect(url_for('main.calculus'))
    
    return render_template('index.html', title='Math Website') 



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
    
    
    return render_template('user.html', user=user)


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
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        
        
    return render_template('edit_profile.html', title='Math Website',\
        form=form)


# FUNCTIONS---------------------------------------------------------------------
# FUNCTIONS---------------------------------------------------------------------
# FUNCTIONS---------------------------------------------------------------------
# FUNCTIONS---------------------------------------------------------------------


@bp.route('/precalculus', methods=['GET', 'POST']) 
@login_required
def precalculus():
    '''This is the page on which I am keeping score of the success students
are meeting in my course. The @login_required decorator from
Flask-Login sets accessibility restrictions to only those users who are logged
in.'''
    
    if request.method == 'POST':
        if request.form['submit_button'] == 'Transforms':
            return redirect(url_for('main.transforms'))
        elif request.form['submit_button'] == 'Series of Numbers':
            return redirect(url_for('main.series_of_numbers'))
    
    
    return render_template('precalculus/precalculus.html',\
            title='Math Website')

@bp.route('/transforms')
@login_required
def transforms():
    return render_template('precalculus/transforms/transforms.html',\
            title='Math Website')


@bp.route('/series_of_numbers')
@login_required
def series_of_numbers():
    return render_template(\
            'precalculus/series_of_numbers/series_of_numbers.html',\
            title='Math Website')


@bp.route('/calculus')
@login_required
def calculus():
    return render_template('calculus/calculus.html', \
            title='Math Website')


@bp.route('/geometric_series', methods=['GET', 'POST'])
def geometric_series():
    '''This function constructs a graph of the geometric series,
from parameters input by the user.'''
    
    
    form = GeometricSeriesForm()
    
    
    if form.validate_on_submit():
        flash('Base: {}, Scalar: {}, epsilon: {}, Large m: {}'\
            .format(form.base.data, form.scalar.data, form.epsilon.data,\
            form.large_m.data))
        geo = GeometricSeries()
        geo.graph(form.base.data, form.scalar.data, form.epsilon.data,\
            form.large_m.data)
        return redirect(url_for('main.geometric_series_graph_results'))
    
    
    return render_template(
        'precalculus/series_of_numbers/geometric_series.html', \
        title='Math Website',form=form)


@bp.route('/geometric_series_graph_results')
def geometric_series_graph_results():
    '''This function displays the graph of the geometric series constructed
from parameters input by the user.'''
    
    
    return render_template(\
        'precalculus/series_of_numbers/geometric_series_graph_results.html', \
        title='Math Website')


@bp.route('/polynomial_degree_1_transform', methods=['GET', 'POST'])
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
            'main.polynomial_degree_1_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/polynomial_degree_1_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/polynomial_degree_1_transform_graph_results')
def polynomial_degree_1_transform_graph_results():
    '''This function displays the parent and transformed polynomial degree 1
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/'\
        'polynomial_degree_1_transform_graph_results.html',\
        title='Math Website')


@bp.route('/polynomial_degree_2_transform', methods=['GET', 'POST'])
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
            'main.polynomial_degree_2_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/polynomial_degree_2_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/polynomial_degree_2_transform_graph_results')
def polynomial_degree_2_transform_graph_results():
    '''This function displays the parent and transformed polynomial degree 2
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/'\
        'polynomial_degree_2_transform_graph_results.html',\
        title='Math Website')


@bp.route('/polynomial_degree_3_transform', methods=['GET', 'POST'])
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
            'main.polynomial_degree_3_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/polynomial_degree_3_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/polynomial_degree_3_transform_graph_results')
def polynomial_degree_3_transform_graph_results():
    '''This function displays the parent and transformed polynomial degree 3
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/'\
        'polynomial_degree_3_transform_graph_results.html',\
        title='Math Website')


@bp.route('/absolute_value_transform', methods=['GET', 'POST'])
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
            'main.absolute_value_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/absolute_value_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/absolute_value_transform_graph_results')
def absolute_value_transform_graph_results():
    '''This function displays the parent and transformed absolute value
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/absolute_value_transform_graph_results.html',\
        title='Math Website')


@bp.route('/reciprocal_degree_0_by_degree_1_transform',\
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
            'main.reciprocal_degree_0_by_degree_1_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/'\
        'reciprocal_degree_0_by_degree_1_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/reciprocal_degree_0_by_degree_1_transform_graph_results')
def reciprocal_degree_0_by_degree_1_transform_graph_results():
    '''This function displays the parent and transformed reciprocal
functions, with numerators having polynomials degree 0 and denominators
have polynomials degree 1.'''
    
    
    return render_template(\
        'precalculus/transforms/'\
        'reciprocal_degree_0_by_degree_1_transform_graph_results.html',\
        title='Math Website')


@bp.route('/square_root_transform',\
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
            'main.square_root_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/square_root_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/square_root_transform_graph_results')
def square_root_transform_graph_results():
    '''This function displays the parent and transformed square root
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/square_root_transform_graph_results.html',\
        title='Math Website')


@bp.route('/cube_root_transform',\
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
            'main.cube_root_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/cube_root_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/cube_root_transform_graph_results')
def cube_root_transform_graph_results():
    '''This function displays the parent and transformed cube root
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/cube_root_transform_graph_results.html',\
        title='Math Website')


@bp.route('/general_exponential_transform',\
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
            'main.general_exponential_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/general_exponential_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/general_exponential_transform_graph_results')
def general_exponential_transform_graph_results():
    '''This function displays the parent and transformed general exponential
functions.'''
    
    
    return render_template(\
    'precalculus/transforms/general_exponential_transform_graph_results.html',\
    title='Math Website')


@bp.route('/general_logarithmic_transform',\
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
            'main.general_logarithmic_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/general_logarithmic_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/general_logarithmic_transform_graph_results')
def general_logarithmic_transform_graph_results():
    '''This function displays the parent and transformed general logarithmic
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/'\
        'general_logarithmic_transform_graph_results.html',\
        title='Math Website')


@bp.route('/base_e_exponential_transform',\
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
            'main.base_e_exponential_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/base_e_exponential_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/base_e_exponential_transform_graph_results')
def base_e_exponential_transform_graph_results():
    '''This function displays the parent and transformed base e exponential
functions.'''
    
    
    return render_template(\
    'precalculus/transforms/base_e_exponential_transform_graph_results.html',\
    title='Math Website')


@bp.route('/base_e_logarithmic_transform',\
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
            'main.base_e_logarithmic_transform_graph_results'))
    
    
    return render_template(\
        'precalculus/transforms/base_e_logarithmic_transform.html',\
        title='Math Website',\
        form=form)


@bp.route('/base_e_logarithmic_transform_graph_results')
def base_e_logarithmic_transform_graph_results():
    '''This function displays the parent and transformed base e logarithmic
functions.'''
    
    
    return render_template(\
        'precalculus/transforms/'\
        'base_e_logarithmic_transform_graph_results.html',\
        title='Math Website')
