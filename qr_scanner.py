import cv2
from pyzbar.pyzbar import decode
import webbrowser

def open_link_or_show(data):
    print(f"Scanned Data: {data}")
    if data.startswith("http://") or data.startswith("https://"):
        open_browser = input("Open this link in browser? (y/n): ")
        if open_browser.lower() == 'y':
            webbrowser.open(data)
    else:
        print(f"QR Code contains: {data}")

def scan_qr_code():
    cap = cv2.VideoCapture(0)
    print("Scanning... Press 'q' to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            break

        for qr in decode(frame):
            qr_data = qr.data.decode("utf-8")
            qr_type = qr.type
            (x, y, w, h) = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = f"{qr_data}"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 255, 0), 2)
            print("\nQR Code Detected!")
            open_link_or_show(qr_data)
            print("Resuming scan...\n")

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the scanner
scan_qr_code()



#export DYLD_LIBRARY_PATH=/opt/homebrew/lib
#python qr_scanner.py