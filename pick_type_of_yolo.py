import os 
import cv2

pick_image_floder = "/home/alien/Desktop/yolomark/Yolo_mark/x64/Release/data/img"
pick_types = ["0"]

label_out_floder = "/home/alien/Desktop/yolomark/Yolo_mark/x64/Release/data/dl_label"

for label_name in os.listdir(pick_image_floder):
    label_name = label_name.strip("\n")
    if label_name.endswith(".txt"):
        out_file_path = os.path.join(label_out_floder,label_name)
        file_path = os.path.join(pick_image_floder,label_name)
        write_file = open(out_file_path,"w")
        for line in open(file_path,"r"):
            for pick in pick_types:
                if line.startswith(pick):
                    write_file.write(line)
        write_file.close()

