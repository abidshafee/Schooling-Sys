import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 520)

detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        # print(faces[0])
        face = faces[0]
        for idNo, point in enumerate(face):
            cv2.putText(img, str(idNo), point, cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5, (255,0,254), 1)


    cv2.imshow("Image", img)
    cv2.waitKey(1)