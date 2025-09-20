Project Empath: The AI-Powered Social Cue Tutor

A real-time digital coach helping individuals with NVLD and ASD navigate the social world with confidence.

    The Problem: When the Social World is a Foreign Language

    For many people, especially those with conditions like Nonverbal Learning Disorder (NVLD) or Autism Spectrum Disorder (ASD), the social world can feel like a constant puzzle. Essential social cues that many of us take for granted—a subtle smile, a brief frown, a look of surprise—can be incredibly difficult to interpret. This can lead to misunderstandings, social anxiety, and challenges in forming meaningful relationships. How can you build connections when you're struggling to read the emotional subtitles of a conversation?

Our Solution: Real-Time Subtitles for Social Cues

Project Empath is a revolutionary web tool that acts as a private, real-time social cue interpreter. It uses a standard webcam to analyze the facial expressions of the person you are interacting with, providing simple, discreet feedback to help you understand the emotional context of the conversation.

It's a practice tool, a confidence booster, and a live assistant, all designed to empower users to engage in social situations more effectively and with less anxiety.
✨ Key Features & "Wow" Factor

    Real-Time Facial Expression Analysis: Project Empath uses an advanced AI model to instantly "read" the face of the person on camera and identify key emotions like happiness, sadness, or neutrality.

    Discreet & Simple Feedback: The interface is designed to be a private coach, not a distraction. A clean, simple panel sits next to the video feed, providing an unobtrusive icon and a one-word description of the detected emotion (e.g., "😊 Happy," "😟 Sad").

    Practice Mode for Skill Building: Users can practice in a safe environment by watching videos, movies, or talking with a friend or family member to learn and associate facial expressions with their corresponding emotions.

    Accessible Anywhere: As a browser-based tool, Project Empath requires no installation and can be used on any laptop or tablet, making it a highly accessible solution.

🚀 Scalability & Real-World Deployment

This project is not just a proof-of-concept; it's the first step towards a comprehensive suite of assistive social tools.

Realistic Deployment Strategy:

    Phase 1 (The Practice Tool - Deployed Now): The current application serves as a powerful training tool. Users can build their skills and confidence by analyzing faces in a controlled, low-stakes environment. It can be used in therapy sessions or for at-home practice.

    Phase 2 (The Live Assistant - Browser Extension): The next logical step is a browser extension that integrates with video conferencing platforms like Google Meet, Zoom, and Microsoft Teams. The extension would overlay a discreet analysis panel directly onto the video call, providing real-time cues during online classes, remote work meetings, and virtual social events.

    Phase 3 (The Future - AR Integration): The ultimate vision for Project Empath is integration with AR (Augmented Reality) glasses. Imagine receiving subtle, heads-up display cues about a person's emotional state during an in-person conversation. This would be a life-changing tool, seamlessly blending digital assistance with the real world.

Future Features Roadmap:

    Tone of Voice Analysis: Incorporate microphone input to analyze vocal tones (e.g., excited, calm, concerned) for a more complete picture of social cues.

    Contextual Learning Prompts: Provide helpful, educational tips based on detected cues, such as, "This person is smiling. This often means they are happy or agree with you."

    Personalized Profiles: Allow users to track their progress and customize the tool's sensitivity and interface to their specific needs.

🛠️ Tech Stack

    Backend: Python, Flask, OpenCV, FER (Face Emotion Recognition), TensorFlow

    Frontend: HTML5, Tailwind CSS, JavaScript

    Deployment: GitHub Pages (Frontend), Render (Backend)

✅ Functionality: How to Run Project Empath

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

