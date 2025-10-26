import cv2
import os
import pickle



DB_FOLDER_PATH = "card_database/"

OUTPUT_DB_FILE = "card_db.pkl"


orb = cv2.ORB_create(nfeatures=1000)

card_features_list = []



for filename in os.listdir(DB_FOLDER_PATH):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(DB_FOLDER_PATH, filename)
        
     
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"  경고: {filename}을 불러올 수 없음.")
            continue
        
        keypoints, descriptors = orb.detectAndCompute(img, None)
        
        if descriptors is None:
            print(f"  경고: {filename}에서 특징점을 찾을 수 없음.")
            continue
     
        card_features_list.append({
            "filename": filename,
            "descriptors": descriptors
        })


with open(OUTPUT_DB_FILE, 'wb') as f:
    pickle.dump(card_features_list, f)

print(f"\n총 {len(card_features_list)}개의 카드 특징점을 추출하여")
print(f"'{OUTPUT_DB_FILE}' 파일로 저장했습니다.")