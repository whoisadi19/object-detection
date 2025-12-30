from ultralytics import YOLO
import cv2
import numpy as np
import random


model = YOLO("runs/detect/train_v2/weights/best.pt")


img = np.zeros((640, 640, 3), dtype=np.uint8)
img[:] = (34, 139, 34) 
noise = np.random.normal(0, 20, (640, 640, 3)).astype(np.uint8)
img = cv2.add(img, noise)


shape_type = random.choice(['circle', 'rectangle'])


x = random.randint(100, 500)
y = random.randint(100, 500)

if shape_type == 'circle':
    
    cv2.circle(img, (x, y), 50, (255, 0, 0), -1)
    print(f"I drew a CIRCLE at ({x}, {y})")
else:
   
    
    cv2.rectangle(img, (x, y), (x+80, y+80), (0, 0, 255), -1)
    print(f"I drew a RECTANGLE at ({x}, {y})")


results = model(img, conf=0.5)


result_img = results[0].plot()
cv2.imwrite("final_proof.jpg", result_img)
print("Check 'final_proof.jpg' to see if the AI got it right!")