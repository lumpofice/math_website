from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import GraphForm
from app.geometric_processing import Geometric


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='MassiveDiscipline')


@app.route('/graph', methods=['GET', 'POST'])
def graph():
    form = GraphForm()
    
    if form.validate_on_submit():
        
        flash('Lower bound: {}, Upper bound: {}'\
        .format(form.lower_bound.data, form.upper_bound.data))
        
        geo = Geometric()
        geo.graph(form.lower_bound.data, form.upper_bound.data)
        
        return redirect(url_for('graph_results'))
    
    return render_template('graph.html', title='Graphs', form=form)


@app.route('/graph_results')
def graph_results():
    return render_template('graph_results.html', title='MassiveDiscipline')