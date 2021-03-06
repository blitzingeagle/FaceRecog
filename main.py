from PIL import Image
import face_recognition

import cv2

fake_news = True
image = face_recognition.load_image_file("images/biden.jpg")

if fake_news:
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
else:
    face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)

    pil_image.show()

    cv2.imshow("face", pil_image)
    cv2.waitKey()
    cv2.destoyAllWindows()
