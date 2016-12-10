from flask import Flask, render_template, request
import forecast
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	weather = None
	if address:
		weather = forecast.get_weather(address)
	return render_template('index.html', weather=weather)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run()
