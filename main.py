from flask import Flask, render_template, flash, redirect, url_for
from forms import WeatherSearchForm
from utils import get_alerts

app = Flask(__name__)
app.config['SECRET_KEY'] = '12a07c85-425e-4c9f-9537-ca4039366c3c'


@app.route("/", methods=['GET', 'POST'])
def home():
    form = WeatherSearchForm()
    if form.validate_on_submit():
        #  Get all the data from the form
        state_field = form.state_field.data
        urgency_field = form.urgency_field.data
        severity_field = form.severity_field.data
        certainty_field = form.certainty_field.data
        max_results_field = form.max_results_field.data
        # Call the NOAA API with the user requested inputs
        status_code, results = get_alerts(state_field, urgency_field, severity_field, certainty_field, max_results_field)
        #  Let the user know what is going on by returning a message
        if status_code != 200:
            message = "Unable to retrieve alerts.  Please try back later"
        elif len(results) == 0:
            message = f"No active alerts."
        else:
            message = f"{len(results)} active alerts."

        return render_template('home.html', title='Weather Alert Search', form=form, results=results, message=message)

    return render_template('home.html', title='Weather Alert Search', form=form)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

