__author__ = 'xiaokangwang'
import json
import os
import logging


def main():
    logging.basicConfig(filename="KKUsbO.log",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging_kwconf = {"stack_info": True}
    logging.getLogger("KKUsbInO_configor")
    config = {}
    if os.path.isfile("config.conf"):

        with open("config.conf") as conf_fd:
            config = json.load(conf_fd)
    else:
        if os.path.exists("config.conf"):
            print("config.conf must be file")
        else:
            print("config.conf doesn't exist, we will create one.")


if __name__ == "__main__":
    main()