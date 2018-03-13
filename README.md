
***REST endpoints to POX controller***

The present APIs let you gather JSON-ish information on the Controller, the switch and the inter-switch links

In order to get the APIs to working you might need to start some additional modules as well.

**API descriptions**:

**Endpoint address**:	  /web/jsonrest/controller
  
  Data returned:	      controller listen ip and port for the detectable switching modules 	
  
  Modules needed:	      openflow.of_01
  
  Method:		            GET
 
**Endpoint address**:	  /web/jsonrest/switch_stat 
  
  Data returned:	      switch dpid and the uptime (by switch I mean all the switches that the controller detects)
  
  Modules needed:	      openflow (running by default)
  
  Method:		            GET
 
To run the controller with the REST endpoints ready to service the requests, make sure you start these modules with the controller or else the 
reply will be empty or incorrect.

Let us say we want to find the listen address of the controller then we must load the module openflow.of_01, and the jsonrest module as well
with the hosts that this module would be listening for (usually 0.0.0.0) and the port number on which it shall be listening for the requests.


```$ ./pox.py openflow.of_01 forwarding.l2_learning web.jsonrest --host=0.0.0.0 --port=8008```

The above command starts the controller and launches the modules as well. After that you can make a request to the 
URI /web/jsonrest/controller to get the controller listen-address (ip and port). 

pox.py boots up POX. It takes a list of module names on the command line,
locates the modules, calls their launch() function (if it exists), and
then transitions to the "up" state.
