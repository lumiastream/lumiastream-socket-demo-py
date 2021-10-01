import asyncio
from websocket import create_connection

# Paste token from Lumia Stream (Settings > Advanced > Developers API > Show Token)
token = 'paste-token-here'

url = "ws://localhost:39231/api?token=" + token
print(url)
ws = create_connection(url)

# Example of sending a command using a websocket
ws.send('{ "type": "alert", "params": { "value": "twitch-follower" } }')

# Infinite loop waiting for WebSocket data
while True:
    msg = ws.recv()
    print(msg)
