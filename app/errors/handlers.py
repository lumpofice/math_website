from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    '''We have a second return value of "404," which is the error code number.
A default second return value error code of "200," indicating a successful
response, is replaced in this instance with the specific, unsuccessful error
code response, "404".'''
    
    
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    '''We have a second return value of "500," which is the error code number.
A default second return value error code of "200," indicating a successful
response, is replaced in this instance with the specific, unsuccessful error
code response. Additionally, given that "500" is the error code response for
a failed database session, a session rollback is issued to ensure no database
template-triggered access attempts experience interference by this failed
database session.'''
    
    
    db.session.rollback()
    return render_template('errors/500.html'), 500
