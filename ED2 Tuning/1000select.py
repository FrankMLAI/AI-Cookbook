import os
import random
import shutil


files_list = []

for root, dirs, files in os.walk(r"C:\Users\Frank\stable-diffusion-webui-modified\CLIP\input1000"):
    for file in files:
        #all 
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            files_list.append(os.path.join(root, file))


#print images
#lets me count and print the amount of jpeg,jpg,pmg 
file_count = len(files_list)
print (file_count)

# print files_list   
filesToCopy = random.sample(files_list, 100)  #prints two random files from list 

destPath = r"C:\Users\Frank\stable-diffusion-webui-modified\CLIP\input900"

# if destination dir does not exists, create it
if os.path.isdir(destPath) == False:
        os.makedirs(destPath)

# iteraate over all random files and move them
for file in filesToCopy:
    shutil.move(file, destPath)