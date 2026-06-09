#Bug 1vehicle_count = 15
# green_time = 10 + vehiclecount * 2
# print('Green time:', green_time)
# SOLUTION 
vehicle_count = 15
# green_time = 10 + vehicle_count * 2
# print('Green time:', green_time)
# BUG 2
# signal_state = 'GREEN'
# if signal_state = 'GREEN':
#  print('Gaadiyaan chal sakti hain!')
# else:
#  print('Ruko!')
 #SOLUTION
#  signal_state = 'GREEN'
# if signal_state == 'GREEN':
#  print('Gaadiyaan chal sakti hain!')
# else:
#  print('Ruko!')   
#BUG 3
# lanes = ['North', 'South', 'East', 'West']
# for lane in lanes
#  print('Lane:', lane)
#SOLUTON
# lanes = ['North', 'South', 'East', 'West']
# for lane in lanes:
#  print('Lane:', lane)
#BUG 4
import cv2
# img = cv2.imread('traffic.jpg')
# cv2.imshow('Traffic', img)
# cv2.destroyAllWindows()
# Window open hoti hai aur turant band ho jaati hai!
# solution
#img = cv2.imread('traffic.jpg')
# cv2.imshow('Traffic', img)
# cv2.destroyAllWindows()
# bug 5
# from ultralytics import YOLO
# import cv2
# model = YOLO('yolov8n.pt')
# img = cv2.imread('traffic.jpg')
# results = model(img)
# for box in results.boxes: # <-- yahan dhyan do
#  class_id = int(box.cls[0])
#  print(model.names[class_id])
#solution 
# import cv2
# from ultralytics import YOLO

# model = YOLO('yolov8n.pt')

# img = cv2.imread('traffic.jpg')

# results = model(img)

# first_result = results[0]
# for box in first_result.boxes:
    # class_id = int(box.cls[0].item())
