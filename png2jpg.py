

import glob,os
from os import listdir
from PIL import Image

png_list=[]
jpg_list=[]


output_dir="jpg_images/"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)
    print("Directory " , output_dir ,  " Created ")
else:    
    print("Directory " , output_dir ,  " is exist")



for file in listdir():
    if file.endswith(".png"):
        png_list.append(file.split(".")[0])

for file in listdir(output_dir):        
    if file.endswith(".jpg"):
        jpg_list.append(file.split(".")[0])

print(len(png_list),"PNG Files Found" )

jpg_cnt=len(png_list)

for name in png_list:
    if name not in jpg_list:
        im = Image.open(name+".png")
        rgb_im = im.convert('RGB')
        rgb_im.save(output_dir+name+'.jpg')
        print(jpg_cnt,"jpg file remained ","Converting..",name)
        jpg_cnt=jpg_cnt-1

print("all file converted ",len(png_list))
