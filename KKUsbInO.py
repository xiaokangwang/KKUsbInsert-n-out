__author__ = 'xiaokangwang'
import os
import shutil
 
def enum_drive():
    drivelst=set()
    chars="abcdefghijkmlnopqrstvuwxyz"
    charlst=(chars)
    for char in charlst:
        res=os.system("cd "+char+":")
        if !res:
            drivelst.append(char)

 
 
def main():
    pass
 
if __name__ == "__main__":
    main()