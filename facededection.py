import cv2

# Use the correct path to the Haar cascade file
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
a = cv2.CascadeClassifier(cascade_path)

# Check if the classifier is loaded successfully
if a.empty():
    print("Error loading cascade classifier")
    exit()

b = cv2.VideoCapture(0)

while True:
    c_rec, d_image = b.read()
    if not c_rec:
        print("Error reading frame from camera")
        break
    
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    F = a.detectMultiScale(e, 1.3, 6)

    for (x1, y1, w1, h1) in F:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)
    
    cv2.imshow('img', d_image)
    
    # Break the loop if 'q' is pressed
    h = cv2.waitKey(40) & 0xff
    if h == ord('q'):
        break

b.release()
cv2.destroyAllWindows()
