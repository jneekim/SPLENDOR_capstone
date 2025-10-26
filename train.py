from ultralytics import YOLO
import os

def main():
    model=YOLO('yolov8n.pt')

    results = model.train(
        data='splendor_data.yaml',
        epochs=100,
        imgsz=640,
        batch=8,
        name='splendor_yolov8_run'
    )

if __name__ == '__main__':
    main()    