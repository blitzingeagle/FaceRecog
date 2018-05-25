from PIL import Image
import face_recognition

image = face_recognition.load_image_file("images/biden.jpg")

face_locations = face_recognition.face_locations(image)
