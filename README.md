# 🔒 Finger Vein Recognition System

A **Deep Learning-Based Finger Vein Recognition System** for secure and reliable user authentication using CNN. The system supports **user registration and login**, after which it automatically redirects to the main vein recognition interface.

---

## 📁 Project Structure

```

FINGERVEIN/
├── Dataset/             # Stored/processed vein data
├── images/              # Sample or registered finger images
├── model/               # Trained models
├── testImages/          # Images for testing
├── FingerVein.py        # Main recognition logic
├── Test.py              # Entry point (runs login/registration and then main app)
├── users.txt            # Stores registered user credentials
├── run.bat              # Optional batch file for running the project
├── SCREENS.docx         # Screenshots or documentation
├── LICENSE
└── README.md

````

---

## ⚙️ Requirements

> ⚠️ **Important:** This project **only supports Python 3.7**.  
> It will **not work** with Python 3.8 or above due to library compatibility.

### 🐍 Python Libraries:
Install required packages using:

```bash
pip install opencv-python numpy keras tensorflow==2.3.0
````

Also ensure:

* Pillow
* sklearn
* imutils (if used)

---

## 🚀 How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/finger-vein-recognition.git
   cd finger-vein-recognition
   ```

2. **Set up environment with Python 3.7** (you can use \[virtualenv]):

   ```bash
   python3.7 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the system**:

   ```bash
   python Test.py
   ```

4. **Workflow**:

   * User registers or logs in.
   * Automatically redirects to the vein recognition interface handled by `FingerVein.py`.

---

## 📊 Features

* User Registration and Login
* Automatic Redirection to Recognition Module
* CNN-based Vein Feature Extraction
* High Accuracy & Security
* Simple GUI (if applicable)

---

## 👨‍💻 Team Members

This project was developed as part of a final year engineering project by:

- **[Sri Nandan Moram]** – [Team Lead]
- **[Prasanna Surisetti]** – [Team Member]
- **[Padmaja Kadali]** – [Team Member]
- **[Sasi Kiran Podalada]** – [Team Member]

Final Year B.Tech Project – \[BVCITS/JNTUK]

---

## 📝 License

This project is licensed under the terms of the `LICENSE` file.

