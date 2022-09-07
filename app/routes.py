from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import *
from app.geometric_series import GeometricSeries
from app.polynomial_degree_2_transform import PolynomialDegree2Transform
from app.polynomial_degree_1_transform import PolynomialDegree1Transform
from app.reciprocal_degree_0_by_degree_1_transform import\
ReciprocalDegree0ByDegree1Transform


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='MassiveDiscipline')


@app.route('/score')
def score():
    return render_template('score.html', title='MassiveDiscipline')


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
    
    return render_template('geometric_series.html', title='Geometric Series',\
    form=form)


@app.route('/geometric_series_graph_results')
def geometric_series_graph_results():
    return render_template(\
    'geometric_series_graph_results.html', title='MassiveDiscipline')


@app.route('/polynomial_degree_2_transform', methods=['GET', 'POST'])
def polynomial_degree_2_transform():
    form = PolynomialDegree2TransformForm()
    
    if form.validate_on_submit():
    
        square_transform = PolynomialDegree2Transform()
        square_transform.graph(form.horizontal_shift.data, form.x_scalar.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'polynomial_degree_2_transform_graph_results'))
    
    return render_template(\
    'polynomial_degree_2_transform.html',\
    title='Polynomial Degree 2 Transformation',\
    form=form)


@app.route('/polynomial_degree_2_transform_graph_results')
def polynomial_degree_2_transform_graph_results():
    return render_template(\
    'polynomial_degree_2_transform_graph_results.html',\
    title='MassiveDiscipline')


@app.route('/polynomial_degree_1_transform', methods=['GET', 'POST'])
def polynomial_degree_1_transform():
    form = PolynomialDegree1TransformForm()
    
    if form.validate_on_submit():
    
        id_transform = PolynomialDegree1Transform()
        id_transform.graph(form.horizontal_shift.data,\
        form.y_scalar.data, form.vertical_shift.data)
        
        return redirect(url_for(\
        'polynomial_degree_1_transform_graph_results'))
    
    return render_template(\
    'polynomial_degree_1_transform.html',\
    title='Polynomial Degree 1 Transformation',\
    form=form)


@app.route('/polynomial_degree_1_transform_graph_results')
def polynomial_degree_1_transform_graph_results():
    return render_template(\
    'polynomial_degree_1_transform_graph_results.html',\
    title='MassiveDiscipline')

