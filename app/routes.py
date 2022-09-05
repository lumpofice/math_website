from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import *
from app.geometric_processing import Geometric
from app.square_function_transformation_processing import SquareFunction


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='MassiveDiscipline')


@app.route('/geometric', methods=['GET', 'POST'])
def geometric():
    form = GeometricForm()
    
    if form.validate_on_submit():
        
        flash('Base: {}, Scalar: {}, epsilon: {}, Large m: {}'\
        .format(form.base.data, form.scalar.data, form.epsilon.data,\
        form.large_m.data))
        
        geo = Geometric()
        geo.graph(form.base.data, form.scalar.data, form.epsilon.data,\
        form.large_m.data)
        
        return redirect(url_for('graph_results'))
    
    return render_template('geometric.html', title='Geometric Series',\
    form=form)


@app.route('/graph_results')
def graph_results():
    return render_template('graph_results.html', title='MassiveDiscipline')


@app.route('/square_transform', methods=['GET', 'POST'])
def square_transform():
    form = SquareFunctionForm()
    
    if form.validate_on_submit():
    
        square_transform = SquareFunction()
        square_transform.graph(form.scalar.data)
        
        return redirect(url_for('graph_results_square_transform'))
    
    return render_template('square_transform.html', title='Square Function Transformation',\
    form=form)


@app.route('/graph_results_square_transform')
def graph_results_square_transform():
    return render_template('graph_results_square_transform.html', title='MassiveDiscipline')

