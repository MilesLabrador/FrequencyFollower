import time
import zmq
import random
import numpy as np


def consumer():
    signal_set = []
    consumer_id = random.randrange(1,10005)
    print("I am consumer #%s" % (consumer_id))
    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    
    count = 0
    while count < 10:
        buff = consumer_receiver.recv()
        #print(time.time())
        data = np.frombuffer(buff, dtype="float32")
        signal_set.append(np.mean(data))
        if (len(signal_set) >= 100):
            #print(np.mean(signal_set))
            #signal_set = []
            count += 1
        #print(len(data))
        #time.sleep(0.5)
        #exit()
    mean = np.mean(signal_set)
    signal_set = []
    return mean

def detect_sig():    
    return consumer()