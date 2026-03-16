from flask import Flask, jsonify, request
from task00 import make_dataframe
from task01 import get_departments
from task02 import get_towns
from task04 import get_prices
app= Flask(__name__)
df_real_estate =make_dataframe('real_estate.csv')

@app.route('/')
def home():
    return"Hello Ace"
@app.route("/departments")
def departments ():
    result= get_departments(df_real_estate)
    return jsonify(result), 200
@app.route("/towns")
def towns ():
    department= request.args.get('department', None)
    results= get_towns(df_real_estate, department)
    return jsonify(results), 200
@app.route("/prices/departments/<department_code>")
def prices_by_department(department_code):
    town_code = request.args.get('town_code', "")
    result= get_prices(df_real_estate, department_code, town_code)
    return jsonify(result), 200
@app.route('/price/departments/<department_code>/towns/<town_code>')
def prices_by_town(department_code, town_code):
    result= get_prices(df_real_estate,department_code,town_code)
    return jsonify(result), 200



