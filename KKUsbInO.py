__author__ = 'xiaokangwang'
import os
import shutil
import json


def enum_drive_win():
    drivelst=set()
    chars="abcdefghijkmlnopqrstvuwxyz"
    charlst = list(chars)
    for char in charlst:
        res=os.system("cd "+char+":")
        if !res:
            drivelst.append(char)

    return drivelst


def enum_drive_linux(mounting_point):
    return set(os.listdir(mounting_point))
 
def main():
    if !os.path.exists("push"):
        print("nothing to push")

    if !os.path.isdir("push"):
        print("push should be a dir")

    if !os.path.isfile("config.json"):
        print "no configure found"

    config = {}

    try:
        with open("config.json") as config_fd:
            config = json.load(config_fd)
    except Exception as errs:
        print(err)



 
if __name__ == "__main__":
    main()