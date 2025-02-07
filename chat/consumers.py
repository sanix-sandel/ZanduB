"""import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from django.shortcuts import get_object_or_404



class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages=Message.objects.all()
        content={
            'command':'messages',
            'messages':self.messages_to_json(messages)
        }
        
        self.send_message(content)



    def messages_to_json(self, messages):
        result=[]
        for message in messages:
            result.append(self.message_to_json(message))
        return result



    def send_message(self, message):
        self.send(text_data=json.dumps(message))
        #Send to websocket


    def message_to_json(self, message):
        return {
            'author':message.author.username,
            'content':message.content,
            'timestamp':str(message.sent_on)
        }



    def new_message(self, data):
        from accounts.models import User
        author=data['from']
        author_user=get_object_or_404(User, username=author)
        message=Message.objects.create(author=author_user,
            content=data['message']
        )
        content={
            'command':'new_message',
            'message':self.message_to_json(message)
        }
        return self.send_chat_message(content)

    commands={
        'fetch_messages':fetch_messages,
        'new_message':new_message
    }



    def connect(self):
       # self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='chat' 

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()



    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )



    def receive(self, text_data):
       #Receive message from WebSocket
       #text_data={"command":"fetch_messages"}
       data=json.loads(text_data)#{'command':'fetch_messages'}
      
       self.commands[data['command']](self, data)

    def send_chat_message(self, message): #Send retrieved messages 
        #stored in
        # the database to room group   
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    def send_message(self, message):
        self.send(text_data=json.dumps(message))    

    #Receive message from room group
    def chat_message(self, event):
        message=event['message']

        #send message to websocket
        self.send(text_data=json.dumps(message))    """