import os

def run(**args):
    print " in dir module"
    filles=os.listdir(".")
    return str(filles)
