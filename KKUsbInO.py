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
        exit(0)

    if not os.path.isdir("push"):
        lg.critical("push is not dir", stack_info=True)
        print("push should be a dir")
        exit(0)

    if not os.path.isfile("config.json"):
        lg.critical("no configure file found", stack_info=True)
        print("no configure found")
        exit(0)

    config = {}

    try:
        with open("config.json") as config_fd:
            config = json.load(config_fd)
    except Exception as errs:
        lg.critical("Cannot load config.json as json, %s", str(errs), stack_info=True)
        print(errs)

    print("Config loaded, uuid:" + config['uuid'])

    enum_drive = Null

    if os.name == "posix":
        enum_drive = enum_drive_linux
        requiredConfig = set("ti"  # rescan interval
                             , "mp"  #mounting point
        )
        if requiredConfig is not in config:
            lg.error("Too few Configs for linux")
            print("there is too few configure item for current posix system,following is required args")
            print(requiredConfig)
    elif os.name == "nt":
        enum_drive = enum_drive_win
        requiredConfig = set("ti"  # rescan interval
        )
        if requiredConfig is not in config:
            lg.error("Too few Configs for win")
            print("there is too few configure item for current win system,following is required args")
            print(requiredConfig)
    else:
        lg.critical("unsupported OS")
        print("There isn't a support for this OS")
        exit(1)






 
if __name__ == "__main__":
    main()