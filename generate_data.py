import cv2
import numpy as np
import os
import random


os.makedirs("dataset/images", exist_ok=True)
os.makedirs("dataset/labels", exist_ok=True)


COLORS = {
    'red': (0, 0, 255),
    'blue': (255, 0, 0),
    'green': (0, 255, 0)
}

def create_synthetic_image(img_id):
    
    img = np.zeros((640, 640, 3), dtype=np.uint8)
    img[:] = (34, 139, 34) 
    noise = np.random.normal(0, 20, (640, 640, 3)).astype(np.uint8)
    img = cv2.add(img, noise)

    
    shape_type = random.choice(['rectangle', 'circle'])
    color_name = random.choice(list(COLORS.keys()))
    color = COLORS[color_name]
    
    
    x = random.randint(50, 590)
    y = random.randint(50, 590)
    size = random.randint(30, 80)
    
    if shape_type == 'rectangle':
        top_left = (x - size, y - size)
        bottom_right = (x + size, y + size)
        cv2.rectangle(img, top_left, bottom_right, color, -1)
       
        cls = 0
    else:
        cv2.circle(img, (x, y), size, color, -1)
        
        cls = 1

   
    img_path = f"dataset/images/img_{img_id}.jpg"
    cv2.imwrite(img_path, img)


    norm_x = x / 640
    norm_y = y / 640
    norm_w = (size * 2) / 640
    norm_h = (size * 2) / 640
    
    label_path = f"dataset/labels/img_{img_id}.txt"
    with open(label_path, "w") as f:
        f.write(f"{cls} {norm_x:.6f} {norm_y:.6f} {norm_w:.6f} {norm_h:.6f}")

print("Generating 100 synthetic drone images...")
for i in range(100):
    create_synthetic_image(i)
print("Done! Check the 'dataset' folder.")