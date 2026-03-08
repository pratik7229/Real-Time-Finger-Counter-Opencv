# Hand Gesture Finger Counter (Computer Vision using OpenCV)

Real-time hand gesture finger counting system built using classical computer vision techniques. The system detects a hand inside a region of interest, segments it from the background, and counts the number of raised fingers using contour analysis and convex hull geometry.

---

# Overview

This project demonstrates a real-time hand gesture recognition pipeline using OpenCV. The system captures video from a webcam, performs background modeling, and segments the hand region from the frame.

Once the hand is segmented, the algorithm analyzes the contour of the hand and uses geometric properties such as convex hull and circular region analysis to estimate the number of extended fingers.

The pipeline performs:

* Webcam video capture  
* Background modeling using running average  
* Hand segmentation through background subtraction  
* Contour detection  
* Convex hull analysis  
* Finger counting using geometric constraints  

The goal is to demonstrate how classical computer vision methods can be used to interpret hand gestures in real time.

---

# Features

* Real-time webcam hand gesture detection  
* Background subtraction using running average  
* Hand segmentation using contour extraction  
* Convex hull based finger detection  
* Circular ROI based finger counting algorithm  
* Modular and structured Python project  
* Lightweight classical computer vision pipeline  

---

# Algorithm Pipeline

The system follows the steps below:

- Capture frames from the webcam  
- Define a Region of Interest (ROI) where the hand will be detected  
- Build a background model using frame averaging  
- Perform background subtraction to isolate the hand  
- Extract the largest contour representing the hand  
- Compute the convex hull of the hand contour  
- Analyze the circular region around the hand center  
- Count the number of visible fingers  

---

# Installation

Clone the repository

```bash
git clone https://github.com/pratik7229/hand-gesture-finger-counter.git
```
Move into the project directory

```bash
cd hand-gesture-finger-counter
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Running the Application

```bash
python3 main.py
```
The webcam will open and display the finger counting interface.

Make sure your hand is placed inside the Region of Interest (ROI) shown on the screen.


# Demo 

![](https://dummyimage.com/468x300?text=App+Screenshot+Here)

# Performance Considerations

To improve performance and detection stability:

- Keep the background plain and stable  
- Avoid shadows in the ROI  
- Ensure consistent lighting conditions  
- Keep the hand clearly visible inside the ROI  
- Allow the background calibration to complete before placing the hand  

Classical computer vision methods are sensitive to lighting and segmentation noise, so environment conditions affect accuracy.

---

# Applications

This project demonstrates techniques useful in:

- Human-computer interaction  
- Gesture-based control systems  
- Robotics interfaces  
- Touchless interaction systems  
- Computer vision learning and research  

---

# Future Improvements

Possible improvements include:

- MediaPipe-based hand landmark detection  
- Multi-hand gesture recognition  
- Deep learning based gesture classification  
- Real-time gesture command systems  
- Integration with robotics or IoT control systems  

---

# Author

Pratik Walunj  
Robotics Engineer | Robot Perception | Computer Vision | Autonomous Systems  

---

# License

This project is licensed under the Apache License 2.0.