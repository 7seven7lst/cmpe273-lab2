import time
import zmq
import math

while True: 
    # ZeroMQ Context
    context = zmq.Context()
    # receive work, worker_receiver is a socket
    generator_receiver = context.socket(zmq.PULL)
    generator_receiver.connect("tcp://127.0.0.1:1234")
    # Receive data from the socket.
    message = generator_receiver.recv()
    message = message.decode()
    # close the socket
    generator_receiver.close()
    # decode the data
    if message:
        # send work
        worker_sender = context.socket(zmq.PUSH)
        worker_sender.bind("tcp://127.0.0.1:1235")
        msg_to_dashboard = "the square root of {} is {}".format(message,math.sqrt(int(message)))
        print ("message to dashboard >", msg_to_dashboard)
        worker_sender.send(msg_to_dashboard.encode())
        worker_sender.close()
