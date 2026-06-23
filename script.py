import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
trail = []
cap = cv2.VideoCapture(0)
while True:
    
    
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    
    
    if not ret:
        break
    if result.multi_hand_landmarks == None:
        continue
    landmarks = result.multi_hand_landmarks[0].landmark
    tip_index = landmarks[8]
    tip_thumb = landmarks[4]

    x_thumb = int(tip_thumb.x * frame.shape[1])
    y_thumb = int(tip_thumb.y * frame.shape[0])

    x_index = int(tip_index.x * frame.shape[1])
    y_index = int(tip_index.y * frame.shape[0])

    x_y = (x_index, y_index)
    cv2.rectangle(frame, (x_index-35, y_index-35), (x_index+35, y_index+35), (0, 255, 0), 3)
    
    if len(trail) > 200:
        trail.pop(0)
    
    distance = math.sqrt((x_thumb-x_index)**2 + (y_thumb-y_index)**2)
    if distance > 30:
        trail.append((x_index, y_index))
        for i in range(1, len(trail)):
            cv2.line(frame, trail[i-1], trail[i], (0, 0, 255), 3)
    else:
        trail.clear()

    cv2.imshow("name", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    

print(trail)
