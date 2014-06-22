__author__ = 'xiaokangwang'
import os
import shutil
import json
import time
import logging


def enum_drive_win():
    drivelst=set()
    chars="abcdefghijkmlnopqrstvuwxyz"
    charlst = list(chars)
    for char in charlst:
        res = os.path.exists(char + ":\\")
        if res:
            drivelst.add(char + ":\\")

    return set(drivelst)


def enum_drive_linux(mounting_point):
    drs = os.listdir(mounting_point)
    drsx = set()
    for drsxt in drs:
        drs.append(mounting_point + drsxt)

    return drsx
 
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
        exit(0)

    if not os.path.isdir("push"):
        lg.critical("push is not dir", stack_info=True)
        print("push should be a dir")
        exit(0)

    if not os.path.isfile("config.conf"):
        lg.critical("no configure file found", stack_info=True)
        print("no configure file found")
        exit(0)

    config = {}

    try:
        with open("config.conf") as config_fd:
            config = json.load(config_fd)
    except Exception as errs:
        lg.critical("Cannot load config.json as json, %s", str(errs), stack_info=True)
        print(errs)

    print("Config loaded, uuid:" + config['uuid'])

    enum_drive = 0

    if os.name == "posix":
        enum_drive = enum_drive_linux
        requiredConfig = set(["ti"  # rescan interval
            , "mp", "uuid"]  # mounting point
        )
        if not requiredConfig <= set(config, ):
            lg.error("Too few Configs for linux")
            print("there is too few configure item for current posix system,following is required args")
            print(requiredConfig)
    elif os.name == "nt":
        enum_drive = enum_drive_win
        requiredConfig = set(["ti", "uuid"]  # rescan interval
        )
        if not requiredConfig <= set(config, ):
            lg.error("Too few Configs for win")
            print("there is too few configure item for current win system,following is required args")
            print(requiredConfig)
    else:
        lg.critical("unsupported OS")
        print("There isn't a support for this OS")
        exit(1)

    if len(os.listdir("push")) == 0:
        lg.error("push is empty, there is nothing to push")
        print("dir push is empty")
        exit(0)

    tif = -1.0
    try:
        tif = float(config["ti"])
    except Exception as errs:
        lg.error("ti in config is not float like")
        print("ti is not float")

    previosdrive = enum_drive()

    lg.info("founded device to be skipped,count= %s", len(previosdrive))
    print("Ready.")

    while (1):
        nowdev = enum_drive()
        if nowdev == previosdrive:
            time.sleep(tif)
            continue
        else:
            newdev = list(nowdev - previosdrive)
            lg.info("device founded, %s", newdev[0])
            print("device was found at ", newdev[0])

            print("Copying......")
            shutil.copytree("push", newdev[0] + "push")

            lg.info("Copy finished!, %s", newdev[0])
            print("Copy finished!", newdev[0])

            print("You can remove your device now.")
            keepl = 1
            while (keepl):
                if previosdrive == enum_drive():
                    lg.info("device was removed.")
                    print("Ready for next device!")
                    keepl = 0








 
if __name__ == "__main__":
    main()