import os

def list_sizes(dir):
    contents = [os.path.join(dir, f) for f in os.listdir(dir)]
    for f in contents:
        if os.path.isfile(f): # base case
            print(f + ": " + str(os.path.getsize(f)))
        else:
            list_sizes(f)

list_sizes("CM1103 Python Problem Solving")
input()
