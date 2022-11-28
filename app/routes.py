from flask import render_template, flash, redirect, url_for
from app import app
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
import numpy as np


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='MassiveDiscipline')


@app.route('/score')
def score():
    return render_template('score.html', title='MassiveDiscipline')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='MassiveDiscipline', form=form)


@app.route('/geometric_series', methods=['GET', 'POST'])
def geometric_series():
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
    return render_template(\
    'geometric_series_graph_results.html', title='MassiveDiscipline')


@app.route('/polynomial_degree_1_transform', methods=['GET', 'POST'])
def polynomial_degree_1_transform():
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
    return render_template(\
    'polynomial_degree_1_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/polynomial_degree_2_transform', methods=['GET', 'POST'])
def polynomial_degree_2_transform():
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
        form.x_reflection.data, form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'polynomial_degree_2_transform_graph_results'))
    
    return render_template(\
    'polynomial_degree_2_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/polynomial_degree_2_transform_graph_results')
def polynomial_degree_2_transform_graph_results():
    return render_template(\
    'polynomial_degree_2_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/polynomial_degree_3_transform', methods=['GET', 'POST'])
def polynomial_degree_3_transform():
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
        form.x_reflection.data, form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'polynomial_degree_3_transform_graph_results'))
    
    return render_template(\
    'polynomial_degree_3_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/polynomial_degree_3_transform_graph_results')
def polynomial_degree_3_transform_graph_results():
    return render_template(\
    'polynomial_degree_3_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/absolute_value_transform', methods=['GET', 'POST'])
def absolute_value_transform():
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
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'absolute_value_transform_graph_results'))
    
    return render_template(\
    'absolute_value_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/absolute_value_transform_graph_results')
def absolute_value_transform_graph_results():
    return render_template(\
    'absolute_value_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/reciprocal_degree_0_by_degree_1_transform',\
methods=['GET', 'POST'])
def reciprocal_degree_0_by_degree_1_transform():
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
            'range = {{g(x) : g(x) < {} and {} < g(x)}} ____ VA: x = {} ____ '\
            'HA: y = {}'\
            .format(form.horizontal_shift.data, form.x_scalar.data,\
            form.x_reflection.data, form.y_scalar.data,\
            form.vertical_shift.data,\
            form.horizontal_shift.data, form.horizontal_shift.data,\
            form.vertical_shift.data, form.vertical_shift.data,\
            form.horizontal_shift.data, form.vertical_shift.data))
    
        reciprocal_transform = ReciprocalDegree0ByDegree1Transform()
        reciprocal_transform.graph(\
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'reciprocal_degree_0_by_degree_1_transform_graph_results'))
    
    return render_template(\
    'reciprocal_degree_0_by_degree_1_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/reciprocal_degree_0_by_degree_1_transform_graph_results')
def reciprocal_degree_0_by_degree_1_transform_graph_results():
    return render_template(\
    'reciprocal_degree_0_by_degree_1_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/square_root_transform',\
methods=['GET', 'POST'])
def square_root_transform():
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
                form.vertical_shift.data, form.horizontal_shift.data, np.inf,\
                form.vertical_shift.data, np.inf))
                
            if form.x_reflection.data < 0:
                
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                'k = {} ____ '\
                'domain = ({}, {}) ____ '\
                'range = ({}, {})'\
                .format(form.horizontal_shift.data, form.x_scalar.data,\
                form.x_reflection.data, form.y_scalar.data,\
                form.vertical_shift.data, -np.inf, -form.horizontal_shift.data,\
                form.vertical_shift.data, np.inf))
        
        if form.y_scalar.data < 0:
            
            if form.x_reflection.data >= 0:
            
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                'k = {} ____ '\
                'domain = ({}, {}) ____ '\
                'range = ({}, {})'\
                .format(form.horizontal_shift.data, form.x_scalar.data,\
                form.x_reflection.data, form.y_scalar.data,\
                form.vertical_shift.data, form.horizontal_shift.data, np.inf,\
                -np.inf, form.vertical_shift.data))
                
            if form.x_reflection.data < 0:
                
                flash('h = {} ____ b = {} ____ c = {} ____ a = {} ____ '\
                'k = {} ____ '\
                'domain = ({}, {}) ____ '\
                'range = ({}, {})'\
                .format(form.horizontal_shift.data, form.x_scalar.data,\
                form.x_reflection.data, form.y_scalar.data,\
                form.vertical_shift.data, -np.inf, -form.horizontal_shift.data,\
                np.inf, form.vertical_shift.data))
    
        square_root_transform = SquareRootTransform()
        square_root_transform.graph(\
        form.horizontal_shift.data, form.x_scalar.data,\
        form.x_reflection.data, form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'square_root_transform_graph_results'))
    
    return render_template(\
    'square_root_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/square_root_transform_graph_results')
def square_root_transform_graph_results():
    return render_template(\
    'square_root_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/cube_root_transform',\
methods=['GET', 'POST'])
def cube_root_transform():
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
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'cube_root_transform_graph_results'))
    
    return render_template(\
    'cube_root_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/cube_root_transform_graph_results')
def cube_root_transform_graph_results():
    return render_template(\
    'cube_root_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/general_exponential_transform',\
methods=['GET', 'POST'])
def general_exponential_transform():
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
                -np.inf, form.vertical_shift.data, form.vertical_shift.data))
    
        general_exponential_transform = GeneralExponentialTransform()
        general_exponential_transform.graph(\
        form.base.data,\
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'general_exponential_transform_graph_results'))
    
    return render_template(\
    'general_exponential_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/general_exponential_transform_graph_results')
def general_exponential_transform_graph_results():
    return render_template(\
    'general_exponential_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/general_logarithmic_transform',\
methods=['GET', 'POST'])
def general_logarithmic_transform():
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
                form.vertical_shift.data, form.horizontal_shift.data, np.inf,\
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
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'general_logarithmic_transform_graph_results'))
    
    return render_template(\
    'general_logarithmic_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/general_logarithmic_transform_graph_results')
def general_logarithmic_transform_graph_results():
    return render_template(\
    'general_logarithmic_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/base_e_exponential_transform',\
methods=['GET', 'POST'])
def base_e_exponential_transform():
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
                -np.inf, form.vertical_shift.data, form.vertical_shift.data))
    
        base_e_exponential_transform = BaseEExponentialTransform()
        base_e_exponential_transform.graph(\
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'base_e_exponential_transform_graph_results'))
    
    return render_template(\
    'base_e_exponential_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/base_e_exponential_transform_graph_results')
def base_e_exponential_transform_graph_results():
    return render_template(\
    'base_e_exponential_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/base_e_logarithmic_transform',\
methods=['GET', 'POST'])
def base_e_logarithmic_transform():
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
                form.vertical_shift.data, form.horizontal_shift.data, np.inf,\
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
        form.horizontal_shift.data, form.x_scalar.data, form.x_reflection.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'base_e_logarithmic_transform_graph_results'))
    
    return render_template(\
    'base_e_logarithmic_transform.html',\
    title='MassiveDiscipline',\
    form=form)


@app.route('/base_e_logarithmic_transform_graph_results')
def base_e_logarithmic_transform_graph_results():
    return render_template(\
    'base_e_logarithmic_transform_graph_results.html',\
    title='MassiveDiscipline')