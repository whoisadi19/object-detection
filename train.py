from ultralytics import YOLO


model = YOLO("yolov8n.pt") 


results = model.train(
    data="data.yaml",
    epochs=50,          
    imgsz=640,
    device="cpu",
    name="train_v2"     
)