import socketio

token = 'paste-token-here'

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def event(data):
    print('Event', data)

@sio.event
def disconnect(reason):
    print('disconnected from server ', reason)

print('Starting socket client')
sio.connect('http://localhost:39252?token=' + token)
sio.wait()