import sys
import os
import gitlab

path = "/home/vs/work/" # TODO: change to your projects folder
token = "provate-token" # TODO: Insert your gitlab private token
gitlabUrl = "https://gitlab.com" # TODO: Change to your gitlab server url

def createGl():
    folderName = str(sys.argv[1])
    dir = path + str(folderName)

    os.mkdir(dir)

    gl = gitlab.Gitlab(gitlabUrl, private_token=token)
    gl.projects.create({'name': folderName})
    print("Successfully created repository {}".format(folderName))

if __name__ == "__main__":
    createGl()
