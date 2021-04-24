from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
	status = request.form.get("userStatus", False)
	print(f"status is {status} and its type is {type(status)}")
	print(type(status))
	if(status == '1'):
		print(f"Status is {status} and yes user allowed")
		lat = request.form.get("lat", False)
		long = request.form.get("long", False)
		print(f"{lat},{long}")
		api_address = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=4f152fe40915295e05a97c1cdd65151d"
		json_data = requests.get(api_address).json()
		print(json_data["weather"][0]["description"])

	else:
		print(f"Status is {status} and no, he did not allow")
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)