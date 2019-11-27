import cv2
import os

label_floder = "/home/alien/Pictures/ddddd-bb/abc"
out_floder = "/home/alien/Pictures/ddddd-bb/crop_dianbiao"
for file_name in os.listdir(label_floder):
    file_name = file_name.strip("\n")
    if file_name.endswith("txt"):
        image_path = os.path.join(label_floder,file_name.replace("txt","jpg"))
        txt_path = os.path.join(label_floder,file_name)
        if os.path.exists(txt_path) and os.path.getsize(txt_path)>0 and os.path.exists(image_path):
            image = cv2.imread(image_path)
            image_height,image_width,_ = image.shape
            count_idx = 0
            for line in open(txt_path,"r"):
                count_idx += 1
                line = line.strip("\n")
                class_id,centerX,centerY,width,height = line.split(" ")
                rect_width = int(image_width * float(width))
                rect_height = int(image_height * float(height))
                rect_left = int(image_width * float(centerX))-int(rect_width/2)
                rect_top = int(image_height * float(centerY))-int(rect_height/2)
                # cv2.rectangle(image,(rect_left,rect_top),(rect_left+int(rect_width),rect_top+int(rect_height)),(0,0,255),2)
                obj = image[rect_top:rect_top+rect_height,rect_left:rect_left+rect_width]
                out_file_name = "%s_%02d_%02d.jpg"%(file_name.replace(".txt",""),int(class_id),count_idx)
                out_path = os.path.join(out_floder,out_file_name)
                cv2.imwrite(out_path,obj)
                print(out_path)