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




print(('... Server Side ...').center(100," "))
print()

time.sleep(1)
name = input('\nEnter your name: ')
print()





time.sleep(1)
soc = socket.socket()

host_name = "localhost"
port = 9999

soc.bind((host_name, port))

soc.listen(1)
print('Waiting for incoming connections...')

connection, addr = soc.accept()
print(">> Received connection from ", addr,"\n")


time.sleep(1)


client_name = connection.recv(1024)
client_name = client_name.decode()

print("_"*100)
print()
print((client_name + ' has connected.').center(100))
print()
print(('Enter [bye] to leave the chat room\n').center(100))
print("_"*100)
print()
connection.send(name.encode())

while True:
    bordered_left("Me")
    message = input()
    
    if message == '[bye]':
        message = 'Leaving the Chat room'
        connection.send(message.encode())
        print("\n")
        break
        
    connection.send(message.encode())
    
    message = connection.recv(1024)
    message = message.decode()
    
    bordered_right(client_name)
    print(message.rjust(100))

connection.close()

time.sleep(1)

print("_"*100)
print()
print(('... Connection Closed ...').center(100," "))

