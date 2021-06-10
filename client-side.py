#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time, socket




# functions to add border to text

def bordered_center(text):
    text = text.splitlines()
    maxlen = max(len(s) for s in text)
    colwidth = maxlen + 2
    print(('+' + '-'*colwidth + '+').center(100," "))
    for s in text:
        print(('| %-*.*s |' % (maxlen, maxlen, s)).center(100," "))
    print(('+' + '-'*colwidth + '+').center(100," "))

def bordered_right(text):
    text = text.splitlines()
    maxlen = max(len(s) for s in text)
    colwidth = maxlen + 2
    print(('+' + '-'*colwidth + '+').rjust(100," "))
    for s in text:
        print(('| %-*.*s |' % (maxlen, maxlen, s)).rjust(100," "))
    print(('+' + '-'*colwidth + '+').rjust(100," "))
    
    
def bordered_left(text):
    text = text.splitlines()
    maxlen = max(len(s) for s in text)
    colwidth = maxlen + 2
    print(('+' + '-'*colwidth + '+').ljust(100," "))
    for s in text:
        print(('| %-*.*s |' % (maxlen, maxlen, s)).ljust(100," "))
    print(('+' + '-'*colwidth + '+').ljust(100," "))
    
print()
bordered_center("       CHAT BOX APPLICATION       ")



print(('... Client Side ...').center(100," "))
print()

time.sleep(1)

name = input('\nEnter your name: ')
print()




time.sleep(1)
soc = socket.socket()

server_host = "localhost"
port = 9999

soc.connect((server_host, port))
print("Server connected...\n")

time.sleep(1)





soc.send(name.encode())

server_name = soc.recv(1024)
server_name = server_name.decode()

print("_"*100)
print()
print((server_name + ' has connected.').center(100))
print()
print(('Enter [bye] to leave the chat room\n').center(100))
print("_"*100)
print()

while True:
    message = soc.recv(1024)
    message = message.decode()
    bordered_right(server_name)
    print(message.rjust(100))
    
    bordered_left("Me")
    message = input()
    
    if message == "[bye]":
        message = "Leaving the Chat room"
        soc.send(message.encode())
        print("\n")
        break
    soc.send(message.encode())

soc.close()

time.sleep(1)

print("_"*100)
print()
print(('... Connection Closed ...').center(100," "))

