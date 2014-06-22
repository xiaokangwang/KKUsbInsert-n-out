__author__ = 'xiaokangwang'
import json
import os
import logging
import uuid


def main():
    logging.basicConfig(filename="KKUsbO.log",
                        filemode='a',
                        format='\n\n%(levelname)s: %(asctime)s %(name)s %(message)s',
                        level=logging.DEBUG)
    logging_kwconf = {"stack_info": True}
    lg = logging.getLogger("KKUsbInO_configor")
    config = {}

    if os.path.isfile("config.conf"):

        with open("config.conf") as conf_fd:
            config = json.load(conf_fd)
    else:
        if os.path.exists("config.conf"):
            lg.critical("config.conf is not file", stack_info=True)
            print("config.conf must be file")
        else:
            lg.info("config.conf doesn't exist", stack_info=True)
            config["uuid"] = str(uuid.uuid4())  # prevent loading json from a empty file, which will lead to exception
            print("config.conf doesn't exist, we will create one.")

    print("Ready, uuid: %s", config["uuid"])

    while (1):
        lg.debug("requesting for next command")
        inpd = input("[>")

        inpds = inpd.split()

        if len(inpds) == 0:
            continue

        if inpds[0] == "x":
            lg.info("Asked to writing to file")
            try:
                if not os.path.exists("config.json"):
                    open("config.conf", 'a').close()
                with open("config.conf", "w") as conf_fd:
                    json.dump(config, conf_fd)
                    lg.info("writing to file finished without error")
                    print("done!")


            except Exception as errs:
                lg.error("Failed to write to config.conf, %s", str(errs))
                print("Failed to write to config.conf, %s", str(errs))

        if inpds[0] == "q":
            lg.info("Asking to quit")
            exit(0)

        if inpds[0] == "r":
            config = {}
            config["uuid"] = str(uuid.uuid4())
            lg.info("Asking to reset uuid, new uuid: %s", config["uuid"])
            print("Reseted, uuid: ", config["uuid"])

        if inpds[0] == "l":
            lg.info("Asking to list config")
            for key in config.keys():
                print(key, config[key])
            print("EOL")

        if inpds[0] == "s":
            if len(inpds) != 3:
                print("too few or too many args")
                continue
            config[inpds[1]] = inpds[2]
            lg.info("set arg: %s => %s ", inpds[1], inpds[2])

        if inpds[0] == "d":
            if len(inpds) != 2:
                print("too few or too many args")
                continue

            print(config[inpds[1]])
            lg.info("get arg: %s => %s ", inpds[1], config[inpds[1]])





if __name__ == "__main__":
    main()