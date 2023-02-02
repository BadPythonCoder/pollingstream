from pollingstream import *
import threading

server = Server(port=3000)

#def test_amogus():
	#global server
	
@server.event
def connect(id, token):
	print(f"Connection, id: {id}")
	server.send(id,"yo whatsup")
#threading.Thread(target=server.run,daemon=True).start()
@server.event
def disconnect(id):
	print(f"Disconnection, id: {id}")

@server.event
def message(id,msg):
	print(f"{id}: {msg}")

server.run()

x
