from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import GraphForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='MassiveNap')


@app.route('/graph', methods=['GET', 'POST'])
def graph():
    form = GraphForm()
    
    if form.validate_on_submit():
        
        flash('Lower bound: {}, Upper bound: {}'\
        .format(form.lower_bound.data, form.upper_bound.data))
        
        return redirect(url_for('index'))
    
    return render_template('graph.html', title='Graphs', form=form)