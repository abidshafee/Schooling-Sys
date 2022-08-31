import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)