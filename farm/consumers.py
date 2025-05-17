# farm/consumers.py  
from channels.generic.websocket import AsyncWebsocketConsumer  
import json  

class YourConsumer(AsyncWebsocketConsumer):  
    async def connect(self):  
        await self.accept()  

    async def disconnect(self, close_code):  
        pass  # Handle disconnection logic if needed  

    async def receive(self, text_data):  
        text_data_json = json.loads(text_data)  
        message = text_data_json['message']  

        # Echo the message back  
        await self.send(text_data=json.dumps({  
            'message': message  
        }))  