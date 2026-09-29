

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return{
		"Result":"Your interaction is successfully created."
	}
