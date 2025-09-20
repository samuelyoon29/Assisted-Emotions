# Project Clarity: The AI-Powered Social Cue Assistant

A real-time digital coach helping individuals with non-verbal learning disorder (NVLD), such as Autisum Spectrum Disorder, to navigate the social world with confidence.

## Problem

While many of us may not realize it, we are constantly using social cues, such as a subtle smile, a brief frown, a look of surpriseto, to help us understand one another. For many people, however, especially those with conditions like Nonverbal Learning Disorder (NVLD) or Autism Spectrum Disorder (ASD), it can be challenging to communicate with others as they may struggle to pick up on social cues. This can lead to misunderstandings, social anxiety, and challenges in forming meaningful relationships.

## Our Solution

Project Clarity is a web-first tool that acts as a real-time social cue interpreter. It uses a webcam to analyze the facial expressions of the person you are interacting with and provide either textual or auditory feedback to help you understand the emotional context of the conversation.


## Key Features

- Real-Time Facial Expression Analysis: Project Empath uses the FER Computer Vision AI model to instantly analyze the face of the person on camera and identify key emotions like happiness, sadness, or neutrality.

- Discreet and Simple Feedback: The interface contains a real-time video feed and an icon with a one-word description of the detected emotion (Happy or Sad).

- Accessible Anywhere: As a browser-based tool, Project Clarity requires no installation and can be used on any laptop or tablet.

## Scalability & Real-World Deployment

While our project is just a web-developed tool, we believe it could be deployed in other technologies. Below we have listed a deployment strategy:

### Phase 1
- The current application serves as a powerful training tool. Users can build their skills and confidence by analyzing faces in a controlled, low-stakes environment. It can be used in therapy sessions or for at-home practice.

### Phase 2
- The next logical step is a browser extension that integrates with video conferencing platforms like Google Meet, Zoom, and Microsoft Teams. The extension would overlay a discreet analysis panel directly onto the video call, providing real-time cues during online classes, remote work meetings, and virtual social events.

### Phase 3
- The ultimate vision for Project  is integration with AR (Augmented Reality) glasses. Imagine receiving subtle, heads-up display cues about a person's emotional state during an in-person conversation. This would be a life-changing tool, seamlessly blending digital assistance with the real world.

## Future Features Roadmap:

- Tone of Voice Analysis: Incorporate microphone input to analyze vocal tones (e.g., excited, calm, concerned) for a more complete picture of social cues

- Contextual Learning Prompts: Provide helpful, educational tips based on detected cues, such as, "This person is smiling. This often means they are happy or agree with you."

## Tech Stack
- Backend: Python, Flask, OpenCV, FER (Face Emotion Recognition), TensorFlow
- Frontend: HTML5, Tailwind CSS, JavaScript
- Deployment: GitHub Pages (Frontend), Render (Backend)

## Documentation

Below are some instructions to deploy Project Clarity

### Prerequisites
- Python 3.8+
- A webcam



1. Backend Setup

Clone the repository, navigate to the project folder, and install the required dependencies.

### Clone the repository
```git clone https://github.com/samuelyoon29/Assisted-Emotions.git```

### Install Python libraries
```pip install -r requirements.txt```

### Run the Flask server
```python app.py```
