import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  value = int(input("Value to append: "))       # Call an exposed operation,
  conn.root.exposed_append(value)       # and append two elements
  print (conn.root.exposed_value())   # Print the result
