# Assisted Emotions

Project Iris: The AI-Powered Accessibility Communicator

A real-time, non-verbal communication bridge for those who need it most.

    The Problem: A Silent Gap in Communication

    For millions of individuals with non-verbal conditions—resulting from ALS, a stroke, severe autism, or other medical challenges—expressing fundamental needs and emotions is a daily struggle. Caregivers and loved ones are often left to guess, leading to frustration, misunderstanding, and a diminished quality of life for everyone involved. How can you communicate "I'm in pain" or "I'm happy" when you cannot speak?

Our Solution: Giving a Voice to the Voiceless

Project Iris is a web-based application that transforms a standard webcam into an intelligent communication aid. By leveraging the power of real-time computer vision and AI, Iris analyzes facial expressions and simple colored cards to provide a clear, immediate, and accessible "status board" for caregivers.

It's a simple, elegant solution that closes the communication gap, requiring no specialized hardware—just a browser and a camera.
✨ Key Features & "Wow" Factor

    Real-time Emotion Detection: Using a sophisticated facial emotion recognition model, Iris instantly detects the user's emotional state (Happy/Content vs. Sad/Distressed) and displays it with a clear, intuitive icon.

    Color Card Communication: We've created a simple, universal language using colored cards. A user can simply hold up a card to convey a specific need:

        🔴 Red Card: "I need help" or "I'm in pain."

        🟢 Green Card: "Yes" or "I'm okay."

        🔵 Blue Card: "I'm thirsty/hungry."

    Zero-Install, Accessible UI: The interface is clean, high-contrast, and designed to be understood at a glance from across a room. Because it runs in any modern web browser, it's instantly accessible on a tablet, laptop, or dedicated monitor.

    Instant Feedback Loop: The live video feed is displayed alongside the AI's analysis, providing immediate confirmation that the user's expression or card has been correctly interpreted.

🚀 Scalability & Real-World Deployment

This isn't just a hackathon prototype; it's the foundation for a tool that could be deployed in homes, hospitals, and care facilities tomorrow.

Realistic Deployment Strategy:

    Phase 1 (Immediate): Deploy the application on a dedicated tablet or laptop in a patient's room. The static URL means caregivers can check the "status board" from a nursing station or their own phone on the same network.

    Phase 2 (Mid-Term): Develop a secure, HIPAA-compliant cloud version. This allows families to remotely and passively check in on their loved one's emotional state, providing peace of mind without being intrusive.

    Phase 3 (Long-Term): Integrate with smart home and hospital systems. For example, detecting a "distressed" face or a "red card" could automatically trigger an alert to a caregiver's pager or turn on a smart light in the hallway.

Future Features Roadmap:

    Customizable Cards: Allow caregivers to define their own meanings for different colors or even objects (e.g., holding up a favorite mug means "I want coffee").

    Emotional Logging: Track emotional state over time to provide caregivers with valuable data on a patient's well-being, helping to identify patterns or triggers for distress.

    Auditory Feedback: Add optional sound cues for users with visual impairments.

🛠️ Tech Stack

    Backend: Python, Flask, OpenCV, FER (Face Emotion Recognition), TensorFlow

    Frontend: HTML5, Tailwind CSS, JavaScript

    Deployment: GitHub Pages (Frontend), Render (Backend)

✅ Functionality: How to Run Project Iris

We've designed the project to be simple to set up and run.
Prerequisites

    Python 3.8+

    A webcam

1. Backend Setup

Clone the repository, navigate to the project folder, and install the required dependencies.

# Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

# Install Python libraries
pip install -r requirements.txt

# Run the Flask server
python app.py

The server will start on http://127.0.0.1:5000. The first time you run it, the FER model will be downloaded automatically.
2. Frontend Setup

    Open the index.html file in your browser.

    IMPORTANT: Ensure the API_URL constant in index.html points to your backend server's address (either your local address for testing or the deployed Render URL).

    Grant the browser permission to access your webcam.

The application is now running! You can test its functionality by smiling, looking sad, or showing red, green, and blue objects/cards to the camera.

Presented by:
[Your Name(s) Here]

Hackathon:
[Name of Hackathon Here]
