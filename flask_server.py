from flask import Flask, request, make_response, jsonify, render_template
from pprint import pprint

VERIFICATION_TOKEN = "YOUR VERIFICATION TOKEN FOR THE FACEBOOK APP"

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/callback', methods=['GET', 'POST'])
def callback_function():
	if request.method == 'GET':
		hub_verify_token = request.args['hub.verify_token']
		hub_challenge = request.args['hub.challenge']
		if hub_verify_token == VERIFICATION_TOKEN:
			print("Verified")
		else:
			print("Verification Failed")
		return hub_challenge
	else:
		pprint(request) #Request (Response Code)
		pprint(request.get_json()) #dictionary
		return make_response("Response OK", 200)


if __name__ == '__main__':
	app.run('0.0.0.0', port=8080)
