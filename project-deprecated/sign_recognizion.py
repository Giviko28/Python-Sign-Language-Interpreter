import cv2
import numpy as np
import keras
from helper import *
#from keras.models import load_model
from tensorflow import keras
from skimage.transform import resize, pyramid_reduce
import PIL
import os
from PIL import Image
from time import sleep

curFkingDir = os.path.dirname(__file__)

print(os.path.curdir)
model = keras.models.load_model(f'{curFkingDir}/model.keras')


def prediction(pred):
    return(chr(pred+ 65))


def keras_predict(model, image):
    data = np.asarray( image, dtype="int32" )
    
    pred_probab = model.predict(data)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class

def keras_process_image(img):
    
    image_x = 28
    image_y = 28
    img = cv2.resize(img, (1,28,28), interpolation = cv2.INTER_AREA)
  
    return img
 

def crop_image(image, x, y, width, height):
    return image[y:y + height, x:x + width]

def main():
    l = []
    cam_capture = cv2.VideoCapture(0)    
    sentence = "Iello".upper()
    letter = 0
    sentence_to_image = replace_letters_with_paths([sentence, "boink"])[0]


    while True:
        _, image_frame = cam_capture.read()  
    # Select ROI
        im2 = crop_image(image_frame, 300,300,300,300)
        image_grayscale = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    
        image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (15,15), 0)
        im3 = cv2.resize(image_grayscale_blurred, (28,28), interpolation = cv2.INTER_AREA)


    
        im4 = np.resize(im3, (28, 28, 1))
        im5 = np.expand_dims(im4, axis=0)

        img = cv2.imread(sentence_to_image[letter])
        if img is not None:
            cv2.imshow("letter", img)

    

        pred_probab, pred_class = keras_predict(model, im5)
        curr = prediction(pred_class)
        print(f"the letter is : {curr} with precision of {pred_probab}")


        
        cv2.putText(image_frame, curr, (700, 300), cv2.FONT_HERSHEY_COMPLEX, 4.0, (255, 255, 255), lineType=cv2.LINE_AA)
        
        
            
        
 
    # Display cropped image
        cv2.rectangle(image_frame, (300, 300), (600, 600), (255, 255, 00), 3)
        cv2.imshow("frame",image_frame)
        
        
        # cv2.imshow("Image4",resized_img)

        cv2.imshow("Image3",image_grayscale_blurred)

             

        if cv2.waitKey(0) & 0xFF == ord('q') or letter > len(sentence):
                break

        if (curr == sentence[letter]):
             letter += 1
        else:
            continue


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
