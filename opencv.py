import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained VGG model
vgg_model = load_model('emotion_recognition_model_vgg.h5')  # Replace with your model's path
input_shape = (224, 224)

# Load Haarcascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

classes = ['angry','disgust','fear','happy','neutral','sad','surprise']

while True:
    ret, frame = cap.read()  # Read a frame from the video capture
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]  # Extract the face region
        resized_face = cv2.resize(face, input_shape)  # Resize the face to (224, 224)
        resized_face = resized_face / 255.0  # Normalize pixel values
        
        # Reshape the image to match the model's input shape
        input_image = np.reshape(resized_face, (1, *input_shape, 3))
        
        predictions = vgg_model.predict(input_image)


        predicted_class_index = np.argmax(predictions)

        # You can also get the actual predicted probability for the predicted class:
        predicted_probability = predictions[0, predicted_class_index]

        # Now you can display the predicted class and probability on the frame
        predicted_label = "Class {}".format(classes[predicted_class_index])
        cv2.putText(frame, predicted_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Assuming your VGG model outputs probabilities for various classes
        # You can process the predictions as needed here
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a rectangle around the detected face
        
    cv2.imshow('Face Detection', frame)  # Display the frame with detected faces
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
