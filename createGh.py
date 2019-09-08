import sys
import os
from github import Github

path = "/home/vs/work/" # TODO: change to your projects folder

username = "username" # TODO: Insert your github username here
password = "password" # TODO: Insert your github password here

def createGh():
    folderName = str(sys.argv[1])
    dir = path + str(folderName)

    os.mkdir(dir)

    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    createGh()
