import cv2

cap = cv2.VideoCapture(0)
image1 = cv2.imread("Assignment1/background.jpg")
image2 = cv2.imread("Assignment1/background1.jpg")
image3 = cv2.imread("Assignment1/background2.jpg")
image4 = cv2.imread("Assignment1/background3.jpg")
image5 = cv2.imread("Assignment1/background4.jpg")
image6 = cv2.imread("Assignment1/background5.jpg")

ch = int(input("Enter a choice : "))

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Could not access the camera")
        break

    else:
        if ch == 1:
            image1=cv2.resize(image1,(frame.shape[1],frame.shape[0]))
            blended_image1 = cv2.addWeighted(frame,0.7,image1,0.3,gamma=0.1)
            cv2.imshow("Blended Image",blended_image1)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        elif ch ==2 :
            image2=cv2.resize(image2,(frame.shape[1],frame.shape[0]))
            blended_image2 = cv2.addWeighted(frame,0.7,image2,0.3,gamma=0.1)
            cv2.imshow("Blended Image",blended_image2)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        elif ch ==3 :
            image3=cv2.resize(image3,(frame.shape[1],frame.shape[0]))
            blended_image3 = cv2.addWeighted(frame,0.7,image3,0.3,gamma=0.1)
            cv2.imshow("Blended Image",blended_image3)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        elif ch ==4 :
            image4=cv2.resize(image4,(frame.shape[1],frame.shape[0]))
            blended_image4 = cv2.addWeighted(frame,0.7,image4,0.3,gamma=0.1)
            cv2.imshow("Blended Image",blended_image4)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        elif ch ==5 :
            image5=cv2.resize(image5,(frame.shape[1],frame.shape[0]))
            blended_image5 = cv2.addWeighted(frame,0.7,image5,0.3,gamma=0.1)
            cv2.imshow("Blended Image",blended_image5)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        elif ch ==6 :
            image6=cv2.resize(image6,(frame.shape[1],frame.shape[0]))
            blended_image6 = cv2.addWeighted(frame,0.7,image6,0.3,gamma=0.1)
            cv2.imshow("Blended Image",blended_image6)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        else:
            break

cap.release()
cv2.destroyAllWindows()

