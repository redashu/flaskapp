from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return "welcome to the flask tutorials"

@app.route('/app')
def app():
	return render_template("app.html")

if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5000, debug = True) 

