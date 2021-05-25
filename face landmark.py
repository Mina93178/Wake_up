import cv2
import dlib

video = cv2.VideoCapture(0)
#index	camera_id + domain_offset (CAP_*)
#id of the video capturing device to open. To open default camera using default backend just pass 0
frontal_shot = dlib.get_frontal_face_detector()
# this function uses what is so called (the hog face detector) ,
# which detects the frontal face of humans which is compatible with the task of our project
landmarks = dlib.shape_predictor("landmarks.dat")
# shape predictor function returns the post-trained face data ,
# so " landmarks " variable will contain the location of each landmark or we can say benchmark on the human's face
while True:
    _, instantaneous_photo = video.read()
    gray_frame = cv2.cvtColor(instantaneous_photo, cv2.COLOR_BGR2GRAY)

    detected_frontal_faces = frontal_shot(gray_frame)
    for face in detected_frontal_faces:
        current_face_landmarks = landmarks(gray_frame, face)
        for n in range(1, 68):
            x = current_face_landmarks.part(n).x
            y = current_face_landmarks.part(n).y
            cv2.circle(instantaneous_photo, (x, y), 1, (0, 255, 255), 1)


    cv2.imshow("Face Landmarks", instantaneous_photo)

    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()