import cv2
import mediapipe as mp

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
    tip = landmarks[8]
    x = int(tip.x * frame.shape[1])
    y = int(tip.y * frame.shape[0])
    x_y = (x, y)
    cv2.rectangle(frame, (x-35, y-35), (x+35, y+35), (0, 255, 0), 3)
    trail.append((x, y))
    for point in trail:
        cv2.circle(frame, point, 5, (0, 0, 255), -1)
    cv2.imshow("name", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    

print(trail)
