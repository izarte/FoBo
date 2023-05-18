from websocket import create_connection
import json

class Client():
    # def __init__(self):

    # def __del__(self):

    def send_data(self, data):
        self.ws = create_connection("ws://localhost:8000/")
        self.ws.send(json.dumps(data))
        self.ws.close()

if __name__ == '__main__':
    client = Client()
    while True:
        if input() == 'a':
            print("DATA")
            client.send_data({'x': 0, 'y': 0})