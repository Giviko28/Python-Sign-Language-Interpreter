import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import cv2
import mediapipe as mp
from keras.models import load_model
import numpy as np
import pandas as pd

filepath = os.path.dirname(__file__)
model = load_model(f'{filepath}/smnist.h5')

mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils

letterpred = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

def analyze_frame(frame):
    if frame is None:
        return {"error": "No frame provided"}
    
    h, w, c = frame.shape
    framergbanalysis = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultanalysis = hands.process(framergbanalysis)
    hand_landmarksanalysis = resultanalysis.multi_hand_landmarks
    if hand_landmarksanalysis:
        for handLMsanalysis in hand_landmarksanalysis:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lmanalysis in handLMsanalysis.landmark:
                x, y = int(lmanalysis.x * w), int(lmanalysis.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            y_min -= 20
            y_max += 20
            x_min -= 20
            x_max += 20 

        analysisframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        analysisframe = analysisframe[y_min:y_max, x_min:x_max]
        analysisframe = cv2.resize(analysisframe, (28, 28))
        nlist = []
        rows, cols = analysisframe.shape
        for i in range(rows):
            for j in range(cols):
                k = analysisframe[i, j]
                nlist.append(k)
        
        datan = pd.DataFrame(nlist).T
        colname = [val for val in range(784)]
        datan.columns = colname

        pixeldata = datan.values
        pixeldata = pixeldata / 255
        pixeldata = pixeldata.reshape(-1, 28, 28, 1)
        prediction = model.predict(pixeldata)
        predarray = np.array(prediction[0])
        letter_prediction_dict = {letterpred[i]: predarray[i] for i in range(len(letterpred))}
        predarrayordered = sorted(predarray, reverse=True)
        high1 = predarrayordered[0]
        high2 = predarrayordered[1]
        high3 = predarrayordered[2]
        result = {}
        for key, value in letter_prediction_dict.items():
            if value == high1:
                result["Predicted Character 1"] = key
                result["Confidence 1"] = 100 * value
            elif value == high2:
                result["Predicted Character 2"] = key
                result["Confidence 2"] = 100 * value
            elif value == high3:
                result["Predicted Character 3"] = key
                result["Confidence 3"] = 100 * value
        return result

    return {"error": "No hand landmarks detected"}
