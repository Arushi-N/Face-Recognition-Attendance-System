# 🎓 Face Recognition Attendance System

A **real-time face recognition-based attendance system** built with Python.  
It detects faces via webcam, recognizes them from pre-stored student images, and automatically marks attendance in a CSV file.  

Created by **Arushi 💙**

---

## 🚀 Features

- 👀 Real-time face detection using OpenCV and `face_recognition`  
- 📝 Automatic attendance marking in CSV files  
- 👥 Supports multiple faces simultaneously  
- 🗂️ Scalable: just add student images in `faces/` folder  
- 📅 Attendance files saved with the current date (YYYY-MM-DD.csv)  

---

## 🛠️ Tech Stack

- Python  
- OpenCV (`opencv-python`)  
- `face_recognition` library  
- NumPy  

---

## 📦 Requirements

- Python 3.x installed  
- Webcam  
- Internet connection (optional, only if using online images)  

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Arushi-N/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Add student images

Place student images in the faces/ folder

Name each image with the student’s name (e.g., Arushi.png)

4️⃣ Run the program
python attendance.py
5️⃣ Usage

Press q to quit the camera window

Attendance will be saved automatically in a CSV file named by date, e.g., 2026-02-22.csv

🔧 Sample .gitignore
# Ignore Python cache
__pycache__/
*.pyc

# Ignore generated attendance files
*.csv

# Ignore VS Code temp files
tempCodeRunnerFile.python
📌 Sample requirements.txt
face-recognition
opencv-python
numpy
🔐 Security Note

This project does NOT store any sensitive data directly in the code.

CSV attendance files are generated dynamically and ignored via .gitignore to prevent cluttering the repository.

🎯 Future Improvements

Add a GUI interface using Tkinter

Replace CSV storage with a database for easier management

Deploy as a web app using Flask or Streamlit

Display confidence scores for recognition

Automatically send attendance reports via email

📜 License

This project is open-source and free to use for learning purposes.

🙌 Contribution

Feel free to fork this project and improve it.
Pull requests are welcome!
