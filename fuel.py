import formfill
from flask import Flask, render_template, request

app = Flask(__name__)

def gallons_to_litres(gallons):
	return gallons * 3.78541
def add_fuel_entry(gallons,dollars,km):
	data = {}
	litres = gallons_to_litres(gallons)
	data['entry.2.single'] = litres
	data['entry.3.single'] = dollars
	data['entry.4.single'] = km

	url = "https://spreadsheets.google.com/viewform?formkey=dDZPN1RzdUZYcG5HRFJDeUZ2MGcwOWc6MQ&ifq"

	formfill.fill_form(data, url)

@app.route('/', methods=["GET","POST"])
def index():
	if request.method == "POST":
		try:
			gallons = float(request.form['gallons'])
			dollars = float(request.form['dollars'])
			km = float(request.form['km'])
			add_fuel_entry(gallons, dollars, km)
			return render_template('complete.html')
		except:
			return render_template('fail.html')

	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=42000, debug=True)
