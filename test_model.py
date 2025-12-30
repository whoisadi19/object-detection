from ultralytics import YOLO
import cv2
import glob
import random
import os
import easyocr
import numpy as np

print("Loading YOLO and OCR models...")
yolo_path = 'runs/detect/suas_model_v1/weights/best.pt'
model = YOLO(yolo_path)

reader = easyocr.Reader(['en'], gpu=False) 

def clean_image_for_ocr(img_crop):
    
    img_crop = cv2.resize(img_crop, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    
   
    gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
    
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.adaptiveThreshold(
        blur, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 19, 5 
    )
    
    
    kernel = np.ones((3,3), np.uint8) 
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    
    return clean


image_files = glob.glob('dataset_v2/images/*.jpg')
if not image_files:
    print("Error: No images found!")
    exit()

test_image_path = random.choice(image_files)
print(f"Testing on: {test_image_path}")
img = cv2.imread(test_image_path)
original_img = img.copy() 

results = model(img)

for result in results:
    boxes = result.boxes
    for box in boxes:
        
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        
        
        roi = original_img[y1:y2, x1:x2]
        
        
        clean_roi = clean_image_for_ocr(roi)
        
        
        cv2.imshow("What the Robot Sees", clean_roi)
        
       
        text_results = reader.readtext(
        clean_roi, 
        detail=0, 
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        
        if text_results:
            letter = text_results[0]
            print(f"SUCCESS: Found shape with letter '{letter}'")
            
            
            label = f"Shape: {model.names[int(box.cls)]} | Letter: {letter}"
            cv2.putText(img, label, (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            print("Found shape, but OCR was unsure about the letter.")


cv2.imshow("Drone Vision Final", img)

cv2.imshow("Drone Vision Final", img)
print("Waiting 100 seconds... (or press 'q' in the window to close)")


key = cv2.waitKey(100000) 

if key == ord('q') or key == -1:
    print("Closing windows...")
    cv2.destroyAllWindows()