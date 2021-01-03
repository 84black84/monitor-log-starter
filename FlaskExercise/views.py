from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # Appropriately log the different button presses with the appropriate log level.
    if log == "warning":
        app.logger.info('Warning occurred')
    elif log == "error":
        app.logger.info('Error occurred')
    elif log == "critical":
        app.logger.critical("Critical error occurred")
    else:    
        app.logger.info("No issue \n")

    return render_template(
        'index.html',
        log=log
    )
