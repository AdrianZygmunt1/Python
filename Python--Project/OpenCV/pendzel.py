import cv2
import mediapipe as mp
import time
import math
import numpy as np

# Funkcja do rysowania efektu prądu
def draw_electric_discharge(img, p1, p2, color_core, color_glow):
    num_segments = 10  
    displacement = 15  
    
    points = [p1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    for i in range(1, num_segments):
        fraction = i / num_segments

        temp_x = int(p1[0] + fraction * dx)
        temp_y = int(p1[1] + fraction * dy)

        rand_x = np.random.randint(-displacement, displacement)
        rand_y = np.random.randint(-displacement, displacement)
        points.append((temp_x + rand_x, temp_y + rand_y))
    
    points.append(p2)
    
    for i in range(len(points) - 1):
        cv2.line(img, points[i], points[i+1], color_glow, 5, cv2.LINE_AA)
    # Rysujemy środek (cieńszy, biały)
    for i in range(len(points) - 1):
        cv2.line(img, points[i], points[i+1], color_core, 2, cv2.LINE_AA)

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

pTime = 0

while True:
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    pos_left = {}
    pos_right = {}

    if results.multi_hand_landmarks:
        for handLms, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id in [4, 8, 12]:
                    if label == "Left":
                        pos_left[id] = (cx, cy)
                        color = (0, 0, 255)
                    else:
                        pos_right[id] = (cx, cy)
                        color = (0, 255, 0)
                    
                    cv2.circle(img, (cx, cy), 10, color, cv2.FILLED)
        if 8 in pos_left and 8 in pos_right:
            p1 = pos_left[8]
            p2 = pos_right[8]
            
            distance = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            
            if distance < 150: # Efekt prądu aktywuje 
                draw_electric_discharge(img, p1, p2, (255, 255, 255), (255, 255, 0))
                
                if distance < 50: # Bardzo blisko
                    cv2.putText(img, "DANGER!", (int((p1[0]+p2[0])/2)-40, int((p1[1]+p2[1])/2)-20), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    
                if distance < 25:#bum
                    break
            else:
                # Normalna cienka 
                cv2.line(img, p1, p2, (255, 255, 255), 1)

    # Obliczanie FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    
    cv2.imshow("Electric Hands", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()