from ultralytics import YOLO


model = YOLO("yolov8n.pt") 


model.train(
    data="data_v2.yaml",  
    epochs=50,            
    imgsz=640,
    device="cpu",
    name="suas_model_v1"  
)