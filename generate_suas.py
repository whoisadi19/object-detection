import cv2
import numpy as np
import os
import random
import string


os.makedirs("dataset_v2/images", exist_ok=True)
os.makedirs("dataset_v2/labels", exist_ok=True)

COLORS = {
    'red': (0, 0, 255), 
    'blue': (255, 0, 0), 
    'green': (0, 255, 0),
    'purple': (128, 0, 128), 
    'orange': (0, 165, 255),
    'white': (255, 255, 255)
}

def create_suas_image(img_id):
    
    img = np.zeros((640, 640, 3), dtype=np.uint8)
    img[:] = (34, 139, 34) 
    noise = np.random.normal(0, 20, (640, 640, 3)).astype(np.uint8)
    img = cv2.add(img, noise)

    
    shape_type = random.choice(['rectangle', 'circle', 'triangle'])
    color_name = random.choice(list(COLORS.keys()))
    color = COLORS[color_name]
    
    x = random.randint(100, 540)
    y = random.randint(100, 540)
    size = random.randint(40, 80)

    
    if shape_type == 'rectangle':
        cv2.rectangle(img, (x-size, y-size), (x+size, y+size), color, -1)
        cls = 0
    elif shape_type == 'circle':
        cv2.circle(img, (x, y), size, color, -1)
        cls = 1
    elif shape_type == 'triangle':
        pts = np.array([[x, y-size], [x-size, y+size], [x+size, y+size]], np.int32)
        cv2.fillPoly(img, [pts], color)
        cls = 2

    
    letter = random.choice(string.ascii_uppercase)
    text_color = (0, 0, 0) if color_name == 'white' else (255, 255, 255)
    cv2.putText(img, letter, (x-15, y+15), cv2.FONT_HERSHEY_SIMPLEX, 1.5, text_color, 3)

    
    cv2.imwrite(f"dataset_v2/images/img_{img_id}.jpg", img)

    
    norm_x = x / 640
    norm_y = y / 640
    norm_w = (size * 2) / 640
    norm_h = (size * 2) / 640
    
    with open(f"dataset_v2/labels/img_{img_id}.txt", "w") as f:
        f.write(f"{cls} {norm_x:.6f} {norm_y:.6f} {norm_w:.6f} {norm_h:.6f}")

print("Generating 2,000 SUAS Competition images...")
for i in range(2000):
    create_suas_image(i)
    if i % 200 == 0: print(f"Generated {i}...")
print("Done! Data is ready in 'dataset_v2'.")