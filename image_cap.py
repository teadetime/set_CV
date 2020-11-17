import numpy as np
import cv2
cap = cv2.VideoCapture(0)
i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):
        print("Saving frame!!")
        # Save the frame
        cv2.imwrite('images/cards_' + str(i) + '.jpg', frame)
        i += 1
    elif key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()