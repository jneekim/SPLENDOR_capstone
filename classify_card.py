import cv2
from ultralytics import YOLO
import os

CLASSIFY_MODEL_PATH = "분류모델경로"


TEST_CROP_IMAGE = "집어넣을 잘라낸이미지"

model = YOLO(CLASSIFY_MODEL_PATH)

img_crop = cv2.imread(TEST_CROP_IMAGE)

results = model(img_crop) 

#결과
top1_index = results[0].probs.top1
#결과를 이름으로
card_name = model.names[top1_index]

#신뢰도
confidence = results[0].probs.top1conf.item() 

print("\n--- YOLO 분류 식별 결과 ---")
print(f"  입력 이미지: {TEST_CROP_IMAGE}")
print(f"  매칭된 카드: {card_name} (신뢰도: {confidence * 100:.2f}%)")