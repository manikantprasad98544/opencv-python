import cv2
import mediapipe as mp

# Drawing utility
mp_drawing = mp.solutions.drawing_utils
# Hand detection utility
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        flag, frame = cap.read()
        results = hands.process(frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(0,0, 255), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),)

        if not flag:
            print("Could not access the camera.")
            break
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()