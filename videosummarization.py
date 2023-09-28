# import cv2 # pip install opencv-python frameworks, including Caffe, TensorFlow, and Torch/PyTorch
# import numpy as np # pip install numpy

# video = cv2.VideoCapture('test.mp4')
# width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# threshold = 20.

# writer = cv2.VideoWriter('test1.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 25, (width, height))
# ret, frame1 = video.read()
# prev_frame = frame1

# a = 0
# b = 0
# c = 0

# while True:
#     ret, frame = video.read()
#     if ret is True:
#         if (((np.sum(np.absolute(frame-prev_frame))/np.size(frame)) > threshold)):
#             frame = cv2.rotate(frame,cv2.ROTATE_180)
#             writer.write(frame)
#             prev_frame = frame
#             a += 1
#         else:
#             prev_frame = frame
#             b += 1

#         cv2.imshow('frame', frame)
#         c += 1
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    

# print("Total frames: ", c)
# print("Unique frames: ", a)
# print("Common frames: ", b)
# video.release()
# writer.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
import sys

video = cv2.VideoCapture('test.mp4')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
threshold = 20.0

# Use 'XVID' codec instead of 'DIVX'
writer = cv2.VideoWriter('test1.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (width, height))

ret, frame1 = video.read()
prev_frame = frame1

a = 0
b = 0
c = 0

try:
    while True:
        ret, frame = video.read()
        if ret is True:
            frame_diff = np.sum(np.absolute(frame - prev_frame)) / np.size(frame)
            if frame_diff > threshold:
                frame = cv2.rotate(frame, cv2.ROTATE_180)
                writer.write(frame)
                prev_frame = frame
                a += 1
            else:
                prev_frame = frame
                b += 1

            cv2.imshow('frame', frame)
            c += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Display the resulting frame
        cv2.putText(frame, "Press spacebar to play/pause, and ESC to close", (10, height-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.imshow('frame', frame)
        c += 1
    
        # Write frame to output video
        writer.write(frame)
        # check for spacebar or ESC key press
        key = cv2.waitKey(1)
        if key == 32:  # spacebar key code
            while True:
                key2 = cv2.waitKey(10)
                cv2.imshow('frame', frame)
                if key2 == 32:
                    break
        elif key == 27:  # ESC key code
            break

except KeyboardInterrupt:
    # Keyboard interrupt received, release resources and exit
    video.release()
    writer.release()
    cv2.destroyAllWindows()
    sys.exit(0)

print("Total frames: ", c)
print("Unique frames: ", a)
print("Common frames: ", b)

video.release()
writer.release()
cv2.destroyAllWindows()