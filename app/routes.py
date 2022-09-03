from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import *
from app.geometric_processing import Geometric


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    geometric = ChooseFunction()
    
    if geometric.validate_on_submit():
        
        return redirect(url_for('geometric'))
    
    return render_template('index.html', title='MassiveDiscipline', form=geometric)


@app.route('/geometric', methods=['GET', 'POST'])
def geometric():
    form = GeometricForm()
    
    if form.validate_on_submit():
        
        flash('Base: {}, Scalar: {}'\
        .format(form.base.data, form.scalar.data))
        
        geo = Geometric()
        geo.graph(form.base.data, form.scalar.data)
        
        return redirect(url_for('graph_results'))
    
    return render_template('geometric.html', title='Graphs', form=form)


@app.route('/graph_results')
def graph_results():
    return render_template('graph_results.html', title='MassiveDiscipline')