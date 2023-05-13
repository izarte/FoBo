from websocket import create_connection
import json

ws = create_connection("ws://localhost:8000/")
data = {'x': 0, 'y': 0}
ws.send(json.dumps(data))
ws.close()