from flask import Flask
from flask import render_template, request


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
        pi = 3.14
        tank_top = pi * radius**2
        print(tank_top)
        tank_side = 2 * (pi * (radius * height))
        print(tank_side)
        tank_area = tank_top + tank_side
        total_sqft = tank_area / 144
        material_cost = total_sqft * 25
        labor_cost = total_sqft * 15
        total_estimate = "${:,.2f}".format(round(material_cost + labor_cost, 2))
        return render_template('estimate.html', estimate = total_estimate)
    return render_template('estimate.html', pageTitle='VTM Estimator')

if __name__ == '__main__':
    app.run(debug=True)