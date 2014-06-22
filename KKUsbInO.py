__author__ = 'xiaokangwang'
import os
import shutil


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
    pass
 
if __name__ == "__main__":
    main()