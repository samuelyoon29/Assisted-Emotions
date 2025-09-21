# Project Clarity

An AI-powered accessibility tool that provides real-time feedback on facial expressions, helping individuals with NVLD or ASD better understand social cues.

---

## 🚀 Demo
[Live Demo](https://samuelyoon29.github.io/Project-Clarity/) | [Devpost Submission](https://devpost.com/software/project-clarity-x8n7ko)  
<img width="1545" height="1006" alt="image" src="https://github.com/user-attachments/assets/0b029441-8686-4eaa-b5f7-a253c87d4e36" />

---

## 🛠 Tech Stack
- **Backend:** Python, Flask, OpenCV, FER (Facial Emotion Recognition), TensorFlow  
- **Frontend:** HTML5, Tailwind CSS, JavaScript  
- **Deployment:** GitHub Pages (Frontend), Render (Backend)

---

## ⚙️ Project Architecture
1. Webcam feed captured in the browser  
2. Sent to Flask backend for analysis with FER model  
3. Response returned with predicted emotion  
4. Frontend displays emoji + label and can trigger audio feedback  

*(Insert diagram if you have one)*

---

## 📦 Installation

### Prerequisites
- Python 3.8+  
- A webcam  

### Clone Repository
```bash
git clone https://github.com/samuelyoon29/Assisted-Emotions.git
cd Assisted-Emotions
