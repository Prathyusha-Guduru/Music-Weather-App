from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
	status = request.form.get("userStatus", False)
	print(status)
	if(status == 1):
		cords = request.form.get("coord", False)
	else:
		print("User denied geo acess")
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)