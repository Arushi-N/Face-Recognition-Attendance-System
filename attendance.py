import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

# Folder with known faces
KNOWN_FACES_DIR = "faces"
# CSV folder
ATTENDANCE_DIR = "attendance"

os.makedirs(ATTENDANCE_DIR, exist_ok=True)

known_face_encodings = []
known_face_names = []

# Load known faces dynamically
for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(KNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            # Use filename without extension as name
            known_face_names.append(os.path.splitext(filename)[0])

# Open camera
video = cv2.VideoCapture(0)

students = known_face_names.copy()

# Create attendance file with current date
date = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(ATTENDANCE_DIR, f"{date}.csv")
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Time"])  # header

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Resize for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_small)
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(distances)
            name = "Unknown"

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                if name in students:
                    students.remove(name)
                    time = datetime.now().strftime("%H:%M:%S")
                    writer.writerow([name, time])
                    print(f"Attendance marked for {name}")

            # Draw rectangle and label
            top, right, bottom, left = face_location
            top, right, bottom, left = top*4, right*4, bottom*4, left*4
            cv2.rectangle(frame, (left, top), (right, bottom), (220, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (220, 255, 0), 2)

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()