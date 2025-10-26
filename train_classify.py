from ultralytics import YOLO

def main():
    model = YOLO('yolov8n-cls.pt')

    results = model.train(
        data="잘라놧던이미지경로",

        epochs = 50,
        imgsz=224,
        name='splendor_classifier'
    )

    if __name__ == '__main__':
        main()
