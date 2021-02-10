from flask import Flask,url_for,request,render_template, jsonify, Response
import werkzeug
import json
from functools import wraps 

app = Flask(__name__)

def check(username,password):
	return username == "admin" and password == "1234"

#SSL benutzen für mehr Sicherheit prototyp reicht erstmal 
def auth():
	return Response('Bitte einloggen',401, {'WWW-Authenticate':'Basic real = "Login Requried" '})

def requires_auth(f):
	@wraps(f)
	def deco(*args,**kwargs):
		autho = request.authorization
		if not autho or not check(autho.username, autho.password): 
			return auth() 
		return f(*args,**kwargs)
	return deco 
	

@app.route('/adminpanel',methods=['GET'])
@requires_auth
def adminpanel():
	return "Hello Admin"


@app.route('/homesite', methods=['GET']) 
def index():
	return '''
	<h1>Besuchersromanalyse Tobias Werz</h1> 
	<h1>weiter gehts wenn der Sensor vorliegt und betriebsbereit ist</h1> 
	 <a href='+url_for("los")+'> Los gehts</a>
	 '''

@app.route('/template') 
def start():
	return render_template('/index.html',fantasie = "Besucherstrom",param = 50)

@app.route('/login', methods = ['POST','GET']) 
def login():
	name = ""
	if request.method == 'POST':
		name = request.form['name']
	else:
		name = request.args.get('name')
	return "Hello " + name 

#einlesen der daten
@app.route('/postme', methods = ['POST']) 
def json():
	postedJson= json.loads(request.data.decode('utf-8')) #"{'data':'mydata'}"
	print(postedJson)
	return "success"

@app.route('/path',defaults = {'path': ''})
@app.route("/<path:path>")
def bonus1(path):
	return "Hello World " + path 

@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound(e):
	return jsonify(error = str(e), mykey = "value", list=[42,2,1,7]), e.code 

 
if __name__ == '__main__':
    app.run(debug=True,port = 5000)