import socket
import random
import csv
import pandas as pd
import os

def czy_online(host = "8.8.8.8", port = 53, timeout = 3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return "Connection: ONLINE"
    except socket.error:
        return "Connection: OFFLINE"
        
def sprawdzacz():
    return str(random.random())

class TicketListManager:
    def __init__(self, path):
        self.path = path
        if os.path.getsize(path) == 0:
            self.ticketList = pd.DataFrame(columns=['ID', 'Name', 'Ticket', 'URL'])
        else:
            self.ticketList = pd.read_csv(self.path)
    def ticketListCSV(self):
        try:
            with open(self.path, "r") as f:
                information = "FILE WITH LIST OF TICKETS EXIST AND WAS OPENED CORRECTLY"
        except FileNotFoundError:
            with open(self.path, "w") as f:
                information = "FILE WITH LIST OF TICKETS DID NOT EXIST, AND WAS CREATE CORRECTLY"
        return information
    
    def save(self):
        self.ticketList.to_csv(self.path, index = False)