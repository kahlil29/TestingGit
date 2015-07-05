from dulwich.repo import Repo
from os import mkdir
import os
os.chdir("/home/shubham/Documents")
mkdir("dulwichtest")
repo = Repo.init("dulwichtest")
repo
index = repo.open_index()
repr(index).replace('\\\\', '/')
list(index)
f = open('dulwichtest/foo', 'w')
f.write("monty")
f.close()
repo.stage(["foo"])

