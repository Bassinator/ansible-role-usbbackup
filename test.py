import glob
import os

filenames = glob.glob("/Users/bastianbukatz/*")
print os.listdir("/Users/bastianbukatz/") 

assert 1 == 1
assert not len(filenames) == 1

