import os
import re
import shutil
print("ceshi..")

for root, ds, fs in os.walk("E:/study/Code/npm/node_modules"):
    for f in fs:
        if (f == "package.json"):
            os.chdir(root)
            os.system("npm pack")
for root, ds, fs in os.walk("E:/study/Code/npm/node_modules"):
    for f in fs:
        if re.match(r'.*tgz$', f):
            name, suffix = f.rsplit(".tgz")
            print(root+"\\"+f)
            print("E:/study/Code/npm/new"+name+".tgz")
            shutil.copyfile(root+"\\"+f, "E:/study/Code/npm/new/"+name+".tgz")
            abc