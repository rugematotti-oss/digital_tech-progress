from flask import Flask
from task00 import make_dataframe
from task01 import get_departments
app= Flask(__name__)
df_real_estate =make_dataframe('real_estate.csv')

@app.route('/')
def home():
    return"Hello Ace"