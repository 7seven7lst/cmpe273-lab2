import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
dashboard_receiver = context.socket(zmq.PULL)
dashboard_receiver.connect("tcp://127.0.0.1:1235")

# Run a simple "Echo" server
while True:
    # Receive data from the socket.
    message= dashboard_receiver.recv()
    message = message.decode()
    print("dashboard received: ", message)