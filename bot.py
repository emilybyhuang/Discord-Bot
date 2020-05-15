import os
import dotenv
import discord
from SpotifyClient import CustomClient

dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')

guild = 'Spotify Collab'

client = CustomClient()
client.run(token)