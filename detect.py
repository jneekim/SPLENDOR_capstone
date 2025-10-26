import cv2
from ultralytics import YOLO
import os
import numpy as np


MODEL_PATH = "모델저장경로"

TEST_IMAGE_PATH="집어넣을이미지경로"

OUTPUT_CROP_IMG="출력이미지경로"

model=YOLO(MODEL_PATH)

img = cv2.imread(TEST_IMAGE_PATH)


results = model(img,conf=0.5)

card_count=0
gem_count= 0
crop_card_counter=0
crop_gem_counter=0

for box in results[0].boxes:
    class_id=int(box.cls[0])
    class_name=model.names[class_id]

    x1,y1,x2,y2 =box.xyxy[0].cpu().numpy().astype(int)

    if class_name == 'card':
        label = 'card'
        card_count += 1

        cropped_card=img[y1:y2,x1:x2]

        crop_filename=f"{OUTPUT_CROP_IMG}/crop_card_{crop_card_counter}.jpg"
        cv2.imwrite(crop_filename,cropped_card)
        crop_card_counter+=1
    elif class_name == 'gem':
        label='gem'
        gem_count+=1
        cropped_gem=img[y1:y2,x1:x2]

        crop_filename=f"{OUTPUT_CROP_IMG}/crop_gem_{crop_gem_counter}.jpg"
        cv2.imwrite(crop_filename,cropped_gem)
        crop_gem_counter+=1   


print(f"\n -- 탐지 결과 --\n")
print(f"카드: {card_count},보석: {gem_count}")