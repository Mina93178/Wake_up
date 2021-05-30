import cv2
import numpy as np


# Slope of line
def dy_by_dx(a, b, c, d):
    return (d - b) / (c - a)
def seat_built_detector():
    video = cv2.VideoCapture(0)

    while True:

        _, instantaneous_photo = video.read()

        # Converting To GrayScale


        # No Belt Detected Yet
        belt = False
        grey_scale_built = cv2.cvtColor(instantaneous_photo, cv2.COLOR_BGR2GRAY)
        # Bluring The Image For Smoothness
        blur = cv2.blur(grey_scale_built, (1, 1))

        image_edges = cv2.Canny(blur, 50, 400)
        previous_slope = 0


        previous_x1, previous_y1, previous_x2, previous_y2 = 0, 0, 0, 0

        # Extracting Lines
        lines = cv2.HoughLinesP(image_edges, 1, np.pi / 270, 30, maxLineGap=20, minLineLength=170)

        # If "lines" Is Not Empty
        if lines is not None:

            # Loop line by line
            for line in lines:
                current_x1, current_y1, current_x2, current_y2 = line[0]

                # Slope Of Current Line
                current_line_slope = dy_by_dx(current_x1, current_y1, current_x2, current_y2)

                if ((abs(current_line_slope) > 0.7) and (abs(current_line_slope) < 2)): # tan(dy/dx)

                    # And Previous Line's Slope Is Within 0.7 To 2
                    if ((abs(previous_slope) > 0.7) and (abs(previous_slope) < 2)):

                        if (((abs(current_x1 - previous_x1) > 2) and (abs(current_x2 - previous_x2) > 2)) or (
                                (abs(current_y1 - previous_y2) > 2) and (abs(current_y2 - previous_y2) > 2))):
                            cv2.line(instantaneous_photo, (current_x1, current_y1), (current_x2, current_y2), (0, 0, 255), 3)
                            cv2.line(instantaneous_photo, (previous_x1, previous_y1), (previous_x2, previous_y2), (0, 0, 255), 3)

                            print("Belt Detected")
                            belt = True

                # Otherwise Current Slope Becomes Previous Slope (ps) And Current Line Becomes Previous Line (px1, py1, px2, py2)
                previous_slope = current_line_slope
                previous_x1,previous_y1, previous_x2, previous_y2 = line[0]

        cv2.imshow("Seat Belt", instantaneous_photo)
        # if belt == False:
        #     print("No Seatbelt detected")

        # Show The "beltframe"

        key = cv2.waitKey(10)
        if key == 27:
            break
    video.release()
    cv2.destroyAllWindows()


#seat_built_detector()
