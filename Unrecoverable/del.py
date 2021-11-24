import os

os.system('curl https://download.sysinternals.com/files/SDelete.zip --output del.zip')
os.system('tar -xf del.zip')

while 1:
    print("Enter 'show' to list directory!\nEnter ':q' to quit!\n\n")
    
    filename = str(input('Enter file name: '))

    if filename == "show":
        os.system('dir')
        continue
    if filename == ":q":
        break
    
    os.system(f'sdelete64 -p 5 {filename}')
