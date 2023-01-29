from pollingstream.client import Client


client = Client()

@client.event
def connect(id,tok):
	print("pogr!")

@client.event
def message(msg):
	print("VENT")
	client.send("yes")

client.connect("http://192.168.178.38:3000")
