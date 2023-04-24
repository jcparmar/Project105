import os
import cv2

path="Images/"

img=[]

for file in os.listdir(path):

    name,ext = os.path.splitext(file)

    if ext in [".jpg",".jpeg",".png"]:

        file_name = path+"/"+file
        print(file_name)

        img.append(file_name)

count = len(img)

frame = cv2.imread(img[0])

h,w,c = frame.shape

size=(w,h)

print(size)

out= cv2.VideoWriter("Project105.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):

    image=cv2.imread(img[i])

    out.write(image)

out.release()

print("YOur Work Is Done")