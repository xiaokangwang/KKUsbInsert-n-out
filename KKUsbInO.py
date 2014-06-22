__author__ = 'xiaokangwang'
import os
import shutil
import json
import logging


def enum_drive_win():
    drivelst=set()
    chars="abcdefghijkmlnopqrstvuwxyz"
    charlst = list(chars)
    for char in charlst:
        res=os.system("cd "+char+":")
        if not res:
            drivelst.append(char)

    return drivelst


def enum_drive_linux(mounting_point):
    return set(os.listdir(mounting_point))
 
def main():
    logging.basicConfig(filename="KKUsbO.log",
                        filemode='a',
                        format='\n\n%(levelname)s: %(asctime)s %(name)s %(message)s',
                        level=logging.DEBUG)
    logging_kwconf = {"stack_info": True}
    lg = logging.getLogger("KKUsbInO_runtime")

    if not os.path.exists("push"):
        lg.critical("no push dir", stack_info=True)
        print("nothing to push")

    if not os.path.isdir("push"):
        lg.critical("push is not dir", stack_info=True)
        print("push should be a dir")

    if not os.path.isfile("config.json"):
        lg.critical("no configure file found", stack_info=True)
        print("no configure found")

    config = {}

    try:
        with open("config.json") as config_fd:
            config = json.load(config_fd)
    except Exception as errs:
        lg.critical("Cannot load config.json as json, %s", str(errs), stack_info=True)
        print(errs)



 
if __name__ == "__main__":
    main()