from flask import Flask
from flask import redirect, url_for, jsonify
from flask import request
import json
import urllib2
import time
import random
app = Flask(__name__)

class SendHTTPTrap(Thread):   
	def run(self, url):
		while 1:
			#url = "https://trap.noit.circonus.net/module/httptrap/bee46025-b5e0-4c4e-a014-138b3efbc34d/mys3cr3t"
			requestHeaders = {"Accept": "application/json"}
			req = urllib2.Request(url, json.dumps(data), headers = requestHeaders)
			req.get_method = lambda: 'PUT'
			opener = urllib2.urlopen(req)
			putresponse = json.loads(opener.read())
			time.sleep(60)

sendtrap = SendHTTPTrap()
data = {}

@app.route('/')
def index():
	#no idea if this works
	if enableSendTrap:
		sendtrap.start(trapurl)
	else:
		sendtrap.stop()
	
	return 'Index Page'

@app.route('/getfakedata')
def getfakedata():
	return json.dumps(data)

if __name__ == '__main__':
	app.run(debug=True)
