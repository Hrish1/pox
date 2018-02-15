from pox.lib.bottle import Bottle, response
from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.util
import threading
import json
import time
import os
import ast

app = Bottle()
log = core.getLogger()
stats = None
port = long(38663)

@app.hook("after_request")
def enable_cors ():
	response.headers["Access-Control-Allow-Origin"]="*"
	response.headers["Access-Control-Allow-Methods"]="PUT,GET,POST,DELETE,OPTIONS"
	response.headers["Access-Control-Allow-Headers"]="Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"


@app.route("/web/jsonrest/controller")
def get_controller_information():
	try:
		data = {}
		of = core.components.get("of_01")
		if of == None:
			log.error("error obtaining module pox.openflow.of_01")
			return json.dumps(data)
		data = {
				"Address":of.address,				
				"Port":of.port
			}
		return json.dumps(data)
	
	except  BaseException, e:
        	log.error(e.message)
        	data = {}
        	return json.dumps(data)



@app.route("/web/jsonrest/switch_stat")
def get_swith_stats():
	try:
		data_body = []
		openflow = core.components.get("openflow")
		if openflow == None:
			log.error("cannot find module pox.openflow")
			return json.dumps(data_body)
		connections = openflow._connections
	
		for key in connections.keys():
			conn = connections.get(key)
			dpid = dpidToStr(conn.dpid)
			data = {
				"dpid": dpid,
				"uptime": conn.connect_time 
				}
			data_body.append(data)
		return json.dumps(data_body)

	except BaseException, e:
        	log.error(e.message)
        	dataArray = []
        	return json.dumps(dataArray)



def dpidToStr (dpid):
    
    dpidStr = pox.lib.util.dpidToStr(dpid)
    dpidStr = dpidStr.replace("-", ":")
    dpidStr = "00:00:" + dpidStr
    return dpidStr



def launch(host = None, port = None):
	def run():
		try:
			kwargs = {"host" : host, "port" : int(port)}
			app.run(**kwargs)
		except   BaseException,e:
			 log.error(e.message)

	thread = threading.Thread(target = run)
    	thread.daemon = True
   	thread.start()
	
