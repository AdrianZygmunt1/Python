import cv2
import mediapipe as mp
import time
import math



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
                if id in [4, 8, 12,16,20]:
                    if label == "Left":
                        pos_left[id] = (cx, cy)
                        color = (0, 0, 255) 
                    else:
                        pos_right[id] = (cx, cy)
                        color = (0, 255, 0)
                    cv2.circle(img, (cx, cy), 10, color, cv2.FILLED)
                    
        id = [4, 8, 12,16,20]
        for l_id in id:
            for r_id in id:
                if l_id in pos_left and r_id in pos_right:
                    p1 = pos_left[l_id]
                    p2 = pos_right[r_id]  
                    distance = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
                    cv2.line(img, p1, p2, (255, 255, 255), 2)
                    if distance < 50:
                        cv2.line(img, p1, p2, (0, 255, 0), 6)
    # Obliczanie i wyświetlanie FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()