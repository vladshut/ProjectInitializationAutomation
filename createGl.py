import sys
import os
import shutil
import gitlab

path = "/home/vs/work/"

token = "1u3_vi7Z_zsHQ4_1PFek"

def createGl():
    folderName = str(sys.argv[1])
    dir = path + str(folderName)

    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)

    gl = gitlab.Gitlab("https://gitlab.com", private_token=token)
    gl.projects.create({'name': folderName})
    print("Successfully created repository {}".format(folderName))

if __name__ == "__main__":
    createGl()
