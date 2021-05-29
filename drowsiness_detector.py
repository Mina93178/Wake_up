import cv2
import dlib
from scipy.spatial import distance as d
import winsound
import time
# definition of the function concerning calculating the Eye Aspect Ratio (EAR)
def EAR_calculator(ELM): #ELM : eye landmarks
    # the indexes of ( eye ) variable are based on the facial landmarks paper
	#vertical landmarks
	P2_minus_P6 = d.euclidean(ELM[1], ELM[5])
	P3_minus_P5 = d.euclidean(ELM[2], ELM[4])
	#horizontal landmark
	P1_minus_P4 = d.euclidean(ELM[0], ELM[3])
	aspect_ratio = (P2_minus_P6+P3_minus_P5)/(2.0*P1_minus_P4)
	return aspect_ratio
def drowsiness_detector():
    video = cv2.VideoCapture(0)
    # index	camera_id + domain_offset (CAP_*)
    # id of the video capturing device to open. To open default camera using default backend just pass 0
    frontal_shot = dlib.get_frontal_face_detector()
    # this function uses what is so called (the hog face detector) ,
    # which detects the frontal face of humans which is compatible with the task of our project
    landmarks = dlib.shape_predictor("landmarks.dat")
    # shape predictor function returns the post-trained face data ,
    # so " landmarks " variable will contain the location of each landmark or we can say benchmark on the human's face
    dummy_counter = 0
    while True:
        # getting the current frame from camera
        _, instantaneous_photo = video.read()
        # dlib python library is trained to detect face landmarks in greyscale image so we have to convert it into greyscale
        gray_frame = cv2.cvtColor(instantaneous_photo, cv2.COLOR_BGR2GRAY)
        # and now it's time to detect how many face are in the current frame using dlib.get_frontal_face_detector()(current_frame)
        detected_frontal_faces = frontal_shot(gray_frame)
        for face in detected_frontal_faces:
            # getting the landmarks
            face_landmarks = landmarks(gray_frame, face)
            left_eye_coordinates = []  # the array which will contain the x,y coordinates of the left eye landmarks in the current frame
            right_eye_coordinates = []  # the array which will contain the x,y coordinates of the right eye landmarks in the current frame
            '''
            37  38                      43  44
         36        39                42         45
            41  40                      47  40

            the above numbers shows the positions of the left and eye landmarks according to the paper we are working on 
            so we have to get the x,y coodrdinates of these landmarks and then connecting them with a line for example
            as to show the live position of the eye on the screen .. 

            The next 2 For loops , will loop in each point of the landmarks points and get the x,y coordinates of it then 
            append them to left_eye_coordinates and right_eye_coordinates lists 

            '''
            for i in range(36, 42):
                x = face_landmarks.part(i).x
                y = face_landmarks.part(i).y
                left_eye_coordinates.append((x, y))
                last_point_check = i + 1
                if i == 41:
                    last_point_check = 36
                temp_1 = face_landmarks.part(last_point_check).x
                temp_2 = face_landmarks.part(last_point_check).y
                cv2.line(instantaneous_photo, (x, y), (temp_1, temp_2), (255, 255, 0), 1)

            for i in range(42, 48):
                x = face_landmarks.part(i).x
                y = face_landmarks.part(i).y
                right_eye_coordinates.append((x, y))
                last_point_check = i + 1
                if i == 47:
                    last_point_check = 42
                temp_1 = face_landmarks.part(last_point_check).x
                temp_2 = face_landmarks.part(last_point_check).y
                cv2.line(instantaneous_photo, (x, y), (temp_1, temp_2), (255, 255, 0), 1)

            left_ear = EAR_calculator(left_eye_coordinates)
            right_ear = EAR_calculator(right_eye_coordinates)

            EAR = (left_ear + right_ear) / 2
            EAR = round(EAR, 2)
            if EAR < 0.26:
                dummy_counter += 1

            # print(EAR)
            else:
                dummy_counter = 0

            if (dummy_counter > 30):
                #
                # cv2.putText(instantaneous_photo, "DROWSY", (20, 100),
                #             cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
                # cv2.putText(instantaneous_photo, "Sleepy ?", (20, 400),
                #             cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                winsound.PlaySound("wake_up_or_i_kill_yo.wav", winsound.SND_FILENAME)
                # print("Drowsy")
            cv2.imshow("Are you Sleepy", instantaneous_photo)

        key = cv2.waitKey(10)
        if key == 27:
            break
    video.release()
    cv2.destroyAllWindows()


#drowsiness_detector()