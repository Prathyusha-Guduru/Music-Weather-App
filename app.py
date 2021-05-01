from flask import Flask, json,render_template,request,redirect,url_for
from flask.signals import template_rendered
import requests

def temp_change(status):
	if(status == '1'):
		lat = request.form.get("lat", False)
		long = request.form.get("long", False)
		print(f"{lat},{long}")
		api_address = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=4f152fe40915295e05a97c1cdd65151d"
		json_data = requests.get(api_address).json()
		print(json_data["weather"][0]["description"])
		temp = json_data["main"]["temp"]
		return redirect(url_for('weather'))
	else:
		temp = 0
		return redirect(url_for('noaccess'))
	return temp
		

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def index():
	status = request.form.get("userStatus", False)

	temp = temp_change(status)
	lol = 302.7
	i = 0
	print(f"Temp is {temp_change(status)}")
	return render_template('index.html',temp = temp)

@app.route('/weather')
def weather():
	return render_template('weather.html')

@app.route('/noaccess')
def noaccess():
	return render_template('noaccess.html')


if __name__ == "__main__":
	app.run(debug=True)