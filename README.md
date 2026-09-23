
### AI Vision Assistant for Visually Impaired Users

VisionGuide is an AI-powered computer vision project designed to help visually impaired users understand their surroundings through **real-time object detection and directional feedback**.

The project is being developed in stages, starting with a local **OpenCV + YOLO baseline** and progressing toward a **COOL-optimized deployment on AWS Graviton**.

---

# 🎯 Project Goal

The goal is to build a system that can:

1. Capture the user's surroundings using a camera.
2. Detect objects in real time.
3. Identify where an object is located.
4. Determine whether the object is on the left, ahead, or right.
5. Convert the information into an understandable message.
6. Provide the information through audio.
7. Optimize the vision-processing workload using **COOL**.
8. Deploy the optimized workload on **AWS Graviton**.
9. Measure the performance difference between the baseline and optimized implementations.

Example:

```text
Camera sees:

        Person
          🚶

                    Car
                     🚗

System output:

"Person ahead"
"Car on your right"
```

---

# 🏗️ Current Architecture

At the current stage, the system works approximately like this:

```text
             Webcam
                │
                ▼
             OpenCV
                │
                ▼
          Camera Frame
                │
                ▼
        Pre-trained YOLO
                │
                ▼
        Object Detection
                │
                ▼
        Bounding Boxes
                │
                ▼
       Direction Detection
        Left / Center / Right
```

### Current technology stack

```text
Python
OpenCV
Ultralytics YOLO
PyTorch
VS Code
Git / GitHub
```

---

# ✅ What Has Been Completed

## 1. Project Environment

The initial Python project environment has been created.

Development is currently being done using:

* Python
* VS Code
* Virtual environment
* Git/GitHub

---

## 2. Webcam Input

OpenCV is being used to access the webcam and capture frames.

```python
cap = cv2.VideoCapture(0)
```

The application can continuously read frames from the camera.

---

## 3. YOLO Object Detection

A **pre-trained YOLO model** is being used.

The project does **not currently require training a model from scratch**.

The pre-trained model already contains learned weights and can detect supported object classes.

Conceptually:

```text
Camera Frame
     ↓
YOLO
     ↓
Person
Car
Bicycle
Chair
...
```

---

## 4. Bounding Box Detection

YOLO provides bounding boxes for detected objects.

For example:

```text
Person
Confidence: 0.94

Bounding box:
(x1, y1, x2, y2)
```

The bounding box tells the system approximately where the object is located in the camera frame.

---

## 5. Direction Detection

The center of the bounding box is used to determine the object's approximate horizontal position.

The frame is divided into three regions:

```text
┌────────────┬────────────┬────────────┐
│            │            │            │
│    LEFT    │   CENTER   │   RIGHT    │
│            │            │            │
└────────────┴────────────┴────────────┘
```

For example:

```text
Person → LEFT
Car    → CENTER
Chair  → RIGHT
```

This allows the system to produce directional information.

---

# 🟡 Current Status

### The current working pipeline is:

```text
Webcam
   ↓
OpenCV
   ↓
Pre-trained YOLO
   ↓
Object Detection
   ↓
Bounding Box
   ↓
Direction
```

### Current status:

**🟢 Working prototype**

The project can currently run locally through the VS Code terminal using the OpenCV + YOLO pipeline.

---

# 🚧 What Has NOT Been Implemented Yet

The following components are still planned:

* [ ] Text-to-Speech
* [ ] COOL integration
* [ ] AWS Graviton deployment
* [ ] ARM64 environment
* [ ] Docker deployment
* [ ] Baseline benchmarking
* [ ] COOL vs OpenCV comparison
* [ ] CPU utilization measurements
* [ ] Latency measurements
* [ ] Throughput/FPS measurements
* [ ] Cloud cost comparison
* [ ] Object prioritization
* [ ] Distance estimation
* [ ] Mobile camera integration

These will be implemented incrementally.

---

# 🔜 Next Development Stage

## Stage 1 — Complete the Local Assistant

The next step is to complete the local application:

```text
Webcam
   ↓
OpenCV
   ↓
YOLO
   ↓
Object Detection
   ↓
Direction
   ↓
Text
   ↓
Text-to-Speech
```

Example:

```text
YOLO detects:

Person
Confidence = 0.94
Direction = Left

↓

System generates:

"Person on your left"

↓

TTS

🔊 Person on your left
```

---

# 🔜 Stage 2 — COOL Integration

After the baseline is stable, the project will introduce the **Cloud-Optimized OpenCV Library (COOL)**.

The purpose is to optimize supported image/video processing operations.

The project will **not replace YOLO with COOL**.

Instead:

```text
Baseline:

Camera
 ↓
OpenCV
 ↓
YOLO


Optimized:

Camera
 ↓
COOL-supported optimized operations
 ↓
YOLO
```

The exact COOL operations will be selected according to the supported COOL APIs and deployment requirements.

---

# ☁️ Stage 3 — AWS Graviton

The COOL-enabled workload will then be deployed on an **AWS Graviton ARM64 environment**.

Target architecture:

```text
              AWS
               │
               ▼
        Graviton ARM64
               │
        ┌──────┴──────┐
        │             │
       COOL          YOLO
        │             │
        └──────┬──────┘
               │
        Vision Processing
               │
               ▼
        Detection Result
```

The objective is to ensure that the **COOL workload actually executes on the Arm/Graviton path**.

---

# 🐳 Stage 4 — Docker

Docker will be used to create a reproducible deployment environment.

Planned architecture:

```text
VS Code
   ↓
Docker
   ↓
ARM64 Container
   ↓
AWS Graviton
   ↓
COOL + OpenCV + YOLO
```

This will make the deployment environment easier to reproduce.

---

# 📊 Stage 5 — Benchmarking

This is one of the most important parts of the project.

Two implementations will be compared.

### Baseline

```text
OpenCV + YOLO
```

### Optimized

```text
COOL + OpenCV + YOLO
on AWS Graviton
```

The same workload and input data will be used where practical.

The following measurements will be collected:

| Metric           | Baseline | COOL + Graviton |
| ---------------- | -------: | --------------: |
| Average latency  |      TBD |             TBD |
| Throughput / FPS |      TBD |             TBD |
| CPU utilization  |      TBD |             TBD |
| Memory usage     |      TBD |             TBD |
| Cloud cost       |      TBD |             TBD |

**No performance numbers will be claimed until they are measured experimentally.**

---

# 🧠 Stage 6 — Advanced Features

After the core system is working, additional features may be added.

### Possible improvements

```text
Object Detection
       ↓
Direction
       ↓
Distance Estimation
       ↓
Object Priority
       ↓
Alert Management
       ↓
Voice Output
```

Possible features include:

* Approximate distance estimation
* Obstacle prioritization
* Repeated-alert suppression
* Object tracking
* Additional accessibility features
* Mobile camera support
* Edge/cloud hybrid processing

---

# 🗺️ Complete Project Roadmap

```text
                 VISIONGUIDE
                     │
                     ▼
          ┌────────────────────┐
          │ 1. Project Setup   │
          │       ✅ DONE      │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 2. Webcam + OpenCV │
          │       ✅ DONE      │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 3. YOLO Detection  │
          │       ✅ DONE      │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 4. Direction Logic │
          │       ✅ DONE      │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 5. Voice Output    │
          │       🔜 NEXT      │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 6. COOL Integration│
          │       🔜           │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 7. Graviton ARM64 │
          │       🔜           │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 8. Docker Deploy   │
          │       🔜           │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 9. Benchmarking    │
          │       🔜           │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ 10. Optimization   │
          │       🔜           │
          └────────────────────┘
```

---

# 📁 Planned Repository Structure

```text
VisionGuide/
│
├── app/
│   ├── main.py
│   ├── detector.py
│   ├── direction.py
│   └── speech.py
│
├── models/
│   └── README.md
│
├── benchmark/
│   ├── baseline.py
│   ├── cool_version.py
│   └── results/
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

The repository structure will evolve as new components are added.

---

# 🔬 Development Strategy

The project follows an incremental approach.

```text
Working baseline
       ↓
Add accessibility
       ↓
Add COOL
       ↓
Move workload to Graviton
       ↓
Benchmark
       ↓
Optimize
       ↓
Document results
```

The original baseline will be maintained in Git so that each improvement can be compared with previous versions.

---

# ⚠️ Safety

VisionGuide is an experimental assistive-technology prototype.

Computer vision models can make incorrect predictions or fail to detect objects. The system should not be considered a guaranteed safety mechanism or a replacement for established mobility and navigation aids.

---

# 📌 Current Project Status

**Overall:** 🟢 Early working prototype

### Completed

* ✅ Python environment
* ✅ VS Code development setup
* ✅ Webcam capture
* ✅ OpenCV integration
* ✅ Pre-trained YOLO model
* ✅ Object detection
* ✅ Bounding boxes
* ✅ Basic direction detection
* ✅ Local terminal execution

### Currently working on

* 🔄 Voice feedback
* 🔄 Preparing the baseline for COOL integration

### Planned

* ⏳ COOL
* ⏳ AWS Graviton
* ⏳ ARM64 deployment
* ⏳ Docker
* ⏳ Benchmarking
* ⏳ Performance optimization
* ⏳ Advanced accessibility features

---

## Project Vision

> **From seeing objects to understanding surroundings.**

VisionGuide aims to combine computer vision, accessibility, cloud optimization, and AWS Graviton to explore how an AI vision system can provide useful environmental information through audio feedback.

