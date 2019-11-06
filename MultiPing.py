# Python 2.7
# -*- coding: UTF-8 -*-

import multiprocessing
from multiprocessing import Pool, Lock
import os

# global lock to ensure only one process prints at a time
lock = Lock()

def run_ping(ip_address):
    # set ping timeout
    ping_timeout_ms = "1000"

    # ping and IP and suppress default output
    response = os.system("ping -w " + ping_timeout_ms + " " + ip_address + " > nul")

    with lock:
        if response == 0:   # if ping was successful
            print "\n" + ip_address + " is UP"
        else:               # if ping failed
            print "\n" + ip_address + " is DOWN"



# the below line prtects the “entry point” of the program
if __name__ == "__main__":

    list_IPs = ["192.168.1.83", "192.168.1.84"]

    # get number of threads and allocate them into pool
    pool = Pool(multiprocessing.cpu_count())

    # Declare a new process and pass arguments to it
    p1 = multiprocessing.Process(target=run_ping, args=(list_IPs[0]))
    # Declare a new process and pass arguments to it
    p2 = multiprocessing.Process(target=run_ping, args=(list_IPs[1]))
    p1.start()  # starting workers
    p2.start()  # starting workers

    # results = pool.imap_unordered(run_ping, list_IPs))