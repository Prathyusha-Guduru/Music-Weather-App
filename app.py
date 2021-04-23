from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
	status = request.form.get("userStatus", False)
	print(status)
	if(status == 1):
		cords = request.form.get("coord", False)
		print(f"Latitude is {cords[0]} and Longitude is {cords[1]}")
		api_address = f"http://api.openweathermap.org/data/2.5/weather?lat={cords[0]}&lon={cords[1]}&appid=4f152fe40915295e05a97c1cdd65151d"
		json_data = requests.get(api_address).json()
		print(json_data["weather"][0]["description"])

	else:
		print("User denied geo acess")
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)