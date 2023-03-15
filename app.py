from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("cleaned_car_data.csv")
# print(df.columns)


@app.route("/")
def hello():
    companies = df['company'].unique()
    names = df['name'].unique()
    years = df['year'].unique()
    fuel_type = df['fuel_type'].unique()

    return render_template('index.html', companies=companies,names=names,years=years,fuel_type=fuel_type)


if __name__=="__main__":
    app.run(debug=True)


