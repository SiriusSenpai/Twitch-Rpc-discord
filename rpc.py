from turtle import color
import discord
from discord.ext import commands
from pystyle import Colors, Colorate
from colored import fg
import os 





color = fg('#8c00ff')
color2 = '\x1b[38;5;196m'

os.system('cls')

os.system(f'cls & mode 85,20 & title [Twitch Rpc]'),
print(Colorate.Horizontal(Colors.blue_to_purple,
f"""
████████╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗
╚══██╔══╝██║    ██║██║╚══██╔══╝██╔════╝██║  ██║
   ██║   ██║ █╗ ██║██║   ██║   ██║     ███████║
   ██║   ██║███╗██║██║   ██║   ██║     ██╔══██║
   ██║   ╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
   made by Auro#7749
   
 
"""))

token = input(f"{color} <!> Enter Token> ")

client = commands.Bot(command_prefix='.', self_bot=True, help_command=None)

text = input(f"{color} <!> Enter Streaming Text> ")

url = input(f"{color} <!> Enter Twitch Or Youtube Url> ")



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name= f'{text}', url=f'{url}'))
    print(f"{color} <!> Rpc Connecting...")
    print(f"{color} <!> Rpc Connected To {client.user}")
    


client.run(token, bot = False)
