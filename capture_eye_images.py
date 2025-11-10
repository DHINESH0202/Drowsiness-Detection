import cv2
import os

os.makedirs("dataset/open", exist_ok=True)
os.makedirs("dataset/closed", exist_ok=True)

cap = cv2.VideoCapture(0)
mode = "open"
count = 0

print("Press 'c' to capture, 'm' to toggle mode (open/closed), 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.putText(frame, f"Mode: {mode}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Capture Eye Images", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        file_path = f"dataset/{mode}/{mode}_{count}.jpg"
        cv2.imwrite(file_path, frame)
        print(f"Saved {file_path}")
        count += 1

    elif key == ord('m'):
        mode = "closed" if mode == "open" else "open"
        print(f"Mode changed to: {mode}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
