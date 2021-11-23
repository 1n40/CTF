import os
import pickle, hmac, hashlib

def reverse_fun():
      with open("users.json","rb") as f:
            data = f.read()
      data = data.split(" ".encode())
      
      # Checking the integrity of the data
      cip = hmac.new(b'key', data[1],hashlib.sha1).hexdigest()
      
      # If fails, no unpacking of the data
      if cip != data[0].decode():
            print("Improper Pickiling detected!")
            return 1
      
      # If the integrity check passes, continue with pickling
      else:
            d = pickle.loads(data[1])
            return d

if __name__ == '__main__':
      print(reverse_fun())
