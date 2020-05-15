import discord
import sys
import json
#volume, queue, pause, next, previous, play
import recommender
class CustomClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.playList = {}
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    async def on_message(self, message):
        print(f'Message received from {message.author}')
        print(self.playList)
        s = {}
        # "command": "queue", "argument": None, "command": "pause", "argument": None,"command": "Next", "argument": None, "command": "previous", "argument": None, "command": "next": "argument": None]
        #s = {"volume":None,"queue":None,"pause":None,"next":None,"previous":None,"play":None}
        #with open(output.json, mode='w') as f:
            #json.dump([], f)
        if(message.content.find('volume') != -1):
            if("up" in message.content or "Up" in message.content):
                upDown = 'up'
            else: 
                upDown = 'down'
            s["command"] = 'volume'
            s["argument"] = upDown
            #jsonObj = json.dumps(s)
            print(s)
        elif(message.content.find('queue') != -1):
            #if("put" in message.content):
                #song = message.content[message.content.find('put')+4:message.content.find('in')-1]
            #elif("place" in message.content):
                #song = message.content[message.content.find('place')+6:message.content.find('in')-1]
            s["command"] = 'queue'
            song = message.content[message.content.find('queue') + 6:]
            s["argument"] = song
            if(song in self.playList):
                self.playList[song] += 1
            else:
                self.playList[song] = 1
            #print(s)
            #jsonObj = json.dumps(s)
            print(s)
        elif(message.content.find('pause') != -1):
            s["command"] = 'pause'
            s["arugment"] = True
            #jsonObj = json.dumps(s)
            print(s)
        elif(message.content.find('next') != -1):
            if("put" in message.content):
                song = message.content[message.content.find('put')+4:message.content.find('in')-1]
            elif("place" in message.content):
                song = message.content[message.content.find('place')+6:message.content.find('in')-1]
            s["command"] = 'next'
            s["argument"] = song
            #if(song in self.playList):
                #self.playList[song] += 1
            #else:
                #self.playList[song] = 1
            #jsonObj = json.dumps(s)
            print(s)
        elif(message.content.find('previous') != -1):
            if("put" in message.content):
                song = message.content[message.content.find('put')+4:message.content.find('in')-1]
            elif("place" in message.content):
                song = message.content[message.content.find('place')+6:message.content.find('in')-1]
            s["command"]='previous'
            s["argument"] = song
            #if(song in self.playList):
                #self.playList[song] += 1
            #else:
                #self.playList[song] = 1
            #jsonObj = json.dumps(s)
            print(s)
        elif(message.content.find('play') != -1):
            substr = message.content[message.content.find('play')+5:]
            s["command"] = 'play'
            s["argument"] = True
            #jsonObj = json.dumps(s)
            print(s)
        else: 
            print("No song recognized.")
        with open("function_commands.json", "w") as outfile:      
            json.dump(s, outfile, indent=2)

            