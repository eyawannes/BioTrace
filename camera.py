import cv2
from logs import create_log

def start_camera():

    # ✅ Fix caméra Windows
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Camera not working")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Error reading camera")
            break

        cv2.putText(frame,
                    "Press A = Authorized / D = Denied / Q = Quit",
                    (20,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0,255,0),
                    2)

        cv2.imshow("Camera Access Control", frame)

        key = cv2.waitKey(1) & 0xFF   # ✅ important

        if key == ord('a'):
            create_log("Eya", "Authorized")
            print("Authorized logged")

        elif key == ord('d'):
            create_log("Unknown", "Denied")
            print("Denied logged")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()