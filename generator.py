import zmq
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
generator_sender = context.socket(zmq.PUSH)

# Bind the socket to address
generator_sender.bind("tcp://127.0.0.1:1234")

for num in range(10001):
    time.sleep(1)
    print("current number is ",num)
    # Returns a formatted string 
    generator_sender.send("{}".format(num).encode())

generator_sender.close()
