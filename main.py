import cv2
from cvzone.HandTrackingModule import HandDetector

def count_fingers(hands):
    fingers = []

    # Thumb (check if thumb is extended or not)
    if hands[0]['lmList'][4][1] < hands[0]['lmList'][5][1]: #นิ้วโป้งนะ #ข้อนิ้วที่5ตํ่ากว่าข้อนิ้วที่6 คือชูนิ้วนั้นเเหละ
        fingers.append(1) #จริงก็คือชู
    else:
        fingers.append(0) #ไม่จริงก็คือไม่ชู

    # Fingers (check if each finger is extended or not)
    for finger_tip_id in range(8, 21, 4):
        if hands[0]['lmList'][finger_tip_id][2] < hands[0]['lmList'][finger_tip_id - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    ret, frame = cap.read()

    if ret:
        hands, img_out = detector.findHands(frame)
        if hands:
            finger_count = count_fingers(hands)
            cv2.putText(img_out, str(finger_count), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

        cv2.imshow("Finger Count", img_out)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
