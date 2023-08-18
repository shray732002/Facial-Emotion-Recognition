# Facial Emotion Recognition

Welcome to the Facial Emotion Recognition GitHub repository! This repository contains a VGG-based deep learning model that predicts the emotion of a human from input images. Additionally, it showcases the results of testing the model on a set of seven sample images.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Predicting Emotions](#predicting-emotions)
- [Results](#results)
- [License](#license)
- [Contact](#contact)

## About the Project

The Facial Emotion Recognition project is aimed at utilizing the power of deep learning to predict the emotions of humans from input images. The VGG model used in this project is a convolutional neural network architecture known for its effectiveness in image classification tasks.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python 3.x
- TensorFlow (or TensorFlow-GPU) library
- Keras (or Keras-GPU) library
- Numpy library

### Installation

1. Clone the repository:
   ```sh
   git clone [https://github.com/your-username/Facial-Emotion-Recognition.git](https://github.com/shray732002/Facial-Emotion-Recognition.git)
   cd vgg-emotion-predictor
2. Create a virtual environment (optional but recommended):

```sh
conda create --name env_name python=python_version
conda activate env_name
```
  Install required packages:
 ```sh
pip freeze > requirements.txt
```
### Usage
 #### Predicting Emotions
  Just run opencv.py
    ```sh
    python run opencv.py
    ```
  It will run video capture driver in which it will scan your face and predict your emotions.

### Results
   
   The Facial Emotion Recognition model achieved pretty good results in predicting emotions from images. The accuracy 
   and performance metrics can be found in the ipynb file but it can be improved which I will add to this repository.

### License

  This project is licensed under the MIT License.
   
### Contact

  If you have any questions or need assistance, you can reach out to the project maintainer at your@email.com.
