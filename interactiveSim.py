""" Simulator for letting multiple instances of native programs 
    communicate via TCP as if they did via their LoRa chip. 
    Usage: python3 interactiveSim.py [nrNodes] [--p <full-path-to-program>]
    Specify what you want to send in the 'try' clause. 
"""
import time
from lib.common import *
from lib.interactive import *

sim = interactiveSim() # Start the simulator

try:
    time.sleep(20)  # Wait until nodeInfo messages are sent
    
    """ Uh oh! LoRa stopped working! Try Wifi."""
    sim.wifi()

    """ Broadcast Message from node 0 """
    # fromNode = 0
    # sim.sendBroadcast("Hi all! My name is node0", fromNode)

    """ Direct Message from node 0 to node 1 """
    fromNode = 0
    toNode = 1
    sim.sendDM("Hello Node 1! This is Node 0", fromNode, toNode)
    time.sleep(10)
    
    """ Uh oh! Wifi stopped working! Try Bluetooth."""
    sim.bluetooth()
    time.sleep(10)
    
    """ Nevermind. LoRa works again!"""
    sim.defaultRadio()
    
    """ Direct Message from node 1 to node 0 """   
    fromNode = 1
    toNode = 0
    sim.sendDM("Hello Node 0! This is Node 1", fromNode, toNode)
    time.sleep(10)

    """ Ping node 1 from node 0 """
    # fromNode = 0
    # toNode = 1
    # sim.sendPing(fromNode, toNode)

    """ Admin Message (setOwner) from node 0 to node 1 
        (First add shared admin channel.) """
    # for n in sim.nodes:
    #     n.addAdminChannel()  # or sim.getNodeById(n.nodeid).setURL('<YOUR_URL>')  
    # fromNode = 0
    # toNode = 1
    # sim.sendFromTo(fromNode, toNode).setOwner(long_name="Test")  # can be any function in Node class

    time.sleep(10) # Wait until message are sent
    sim.showNodes()
    sim.closeNodes()
except KeyboardInterrupt:
    sim.closeNodes()

sim.graph.initRoutes()  # Visualize the route of messages sent 
