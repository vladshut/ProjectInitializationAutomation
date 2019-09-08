import sys
import os
from github import Github

path = "/home/vs/work/"

username = "vladshut" #Insert your github username here
password = "Newwarrior2929!" #Insert your github password here

def createGh():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName)
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    createGh()
