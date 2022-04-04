from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Vertical Tank Maintenance')

@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        tank_top = pi * radius**2
        tank_side = 2 * (pi * (radius * height))
        tank_area = tank_top + tank_side
        total_sqft = tank_area / 144
        material_cost = total_sqft * 25
        labor_cost = total_sqft * 15
        total_estimate = "${:,.2f}".format(round(material + labor, 2))
    return render_template('estimate.html', pageTitle='VTM Estimator', estimate = total_estimate)

if __name__ == '__main__':
    app.run(debug=True)