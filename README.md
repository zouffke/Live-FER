Here’s the updated README with enhanced Docker-related instructions and a more polished structure:

---

# Deep Learning Project: Facial Recognition

This project was developed as part of the *Data & AI* course, focusing on implementing a Deep Learning model for facial recognition. The project includes data preprocessing, model training, testing, and deployment within a Flask-based web application that provides real-time webcam facial expression predictions. Additionally, it is containerized using Docker for easy deployment.

---

## 📋 Table of Contents

1. [Introduction](#introduction)  
2. [Setup and Installation](#setup-and-installation)  
3. [Running the Application](#running-the-application)  
4. [Docker Deployment](#docker-deployment)  
5. [Project Notebooks](#project-notebooks)  
6. [Usage Notes](#usage-notes)

---

## 🧠 Introduction

This project aims to create a Convolutional Neural Network (CNN) for facial recognition. It involves several stages, including data preprocessing, training, testing, and deploying the model. The final web application allows users to test the model via live webcam input, recognizing and predicting facial expressions in real-time.

---

## 🛠️ Setup and Installation

Before running the project, ensure that all required dependencies are installed. You can install them by running the following command in the project’s root directory:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries and dependencies to run the project.

---

## 🚀 Running the Application

To launch the live facial recognition prediction app, you can run it in two ways:

### 1. **Directly via Flask**

- Navigate to the `scripts` directory:
  ```bash
  cd scripts
  ```

- Start the Flask application:
  ```bash
  flask --app app run
  ```

- Once the server is running, open your browser and navigate to [http://localhost:5000](http://localhost:5000).

  - Here, you can use your webcam to test the live facial expression recognition feature.

### 2. **Using Docker (Recommended for Easy Setup)**

For easier setup and deployment, you can run the application inside a Docker container. This method ensures that all dependencies and environment settings are pre-configured.

- **Build the Docker image:**
  ```bash
  docker build -t facial-recognition .
  ```

- **Run the Docker container:**
  ```bash
  docker run -p 5000:5000 facial-recognition
  ```

- Once the container is running, open your browser and navigate to [http://localhost:5000](http://localhost:5000) to access the live webcam prediction feature.

Docker provides a consistent environment, ensuring that the app runs the same way regardless of your local setup.

---

## 📁 Project Notebooks

The project is structured into several Jupyter notebooks, each focused on a specific task:

1. **[Data Preprocessing](notebooks/01_preprocess.ipynb):**  
   Prepares the raw data by performing tasks like resizing, normalization, and augmentation.

2. **[Balancing the Dataset](notebooks/02_balancing.ipynb):**  
   Addresses class imbalances in the dataset to ensure fair training.

3. **[Convolutional Neural Network (CNN)](notebooks/03_CNN.ipynb):**  
   Defines the architecture of the CNN used for facial recognition.

4. **[Training](notebooks/04_training.ipynb):**  
   Covers the model training process with visualizations of performance during training.

5. **[Testing](notebooks/05_testing.ipynb):**  
   Evaluates the model's accuracy and performance on a test dataset.

6. **[Testing with Color Images](notebooks/06_testing_color.ipynb):**  
   Investigates the model's ability to handle color images for facial recognition.

7. **[Livestream Prediction](notebooks/07_livestream.ipynb):**  
   Demonstrates the live facial expression prediction using webcam input.

---

## ⚠️ Usage Notes

- **Flask Application Directory:**  
  If running the Flask app directly (not via Docker), ensure you are in the `scripts` directory to avoid file path issues.

- **Webcam Access:**  
  The live prediction feature requires access to your webcam. Make sure your browser has webcam permissions enabled.

- **Python Version:**  
  This project has been tested with Python 3.11 or later. Using earlier versions may lead to compatibility issues.

- **Docker Considerations:**  
  Running the app via Docker is recommended for easier setup, as it avoids issues related to dependencies or system-specific configurations.

---

By following this setup, you can easily run the facial recognition model either directly through Flask or within a Docker container, streamlining the process and ensuring consistency across different environments.