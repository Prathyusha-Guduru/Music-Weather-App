#IMPORTING NECESSARY VARIABLES
from flask import render_template,Flask,redirect,url_for,request,make_response
from flask.json import jsonify
import requests	
from form import checkWeatherForm


#APP CREATION AND CONFIGURATION
app =  Flask(__name__)
app.config['SECRET_KEY'] = "izzasecret"

#VIEWS
#homepage view



@app.route('/',methods = ['GET','POST'])
def index():
	req = request.get_json()
	print(req)
	res = make_response(jsonify({"message":"JSON recieved"}),200)
	return render_template('index.html')


# @app.route('/',methods=['GET', 'POST'])
# def index():
# 	form = checkWeatherForm()
# 	if form.validate_on_submit():
# 		return redirect(url_for('weather'))
# 	return render_template('index.html',form = form)

# #weather-result page
# @app.route('/weather',methods=['GET', 'POST'])
# def weather():
# 	status = request.form.get("userStatus", False)
# 	print(f"Status is {status}")
# 	if(status == '1'):
# 		lat = request.form.get("lat", False)
# 		long = request.form.get("long", False)
# 		print(f"{lat},{long}")
# 		api_address = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=4f152fe40915295e05a97c1cdd65151d"
# 		json_data = requests.get(api_address).json()
# 		print(json_data["weather"][0]["description"])
# 		temp = json_data["main"]["temp"]
		
# 	return render_template('weather.html')

if __name__ == '__main__':
	app.run(debug = True)