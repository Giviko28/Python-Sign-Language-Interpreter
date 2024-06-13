import cv2
import numpy as np
import os

def get_images_dict():
    current_dir = os.path.dirname(__file__)
    base_path = os.path.join(current_dir, "images")
    return {letter: os.path.join(base_path, f"{letter}.png") for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


# here by default the english alphabet dictionary is passed, but we can swap it with gesture images if we'd like
def replace_letters_with_paths(sentences, image_paths_dict = get_images_dict()):
    updated_sentences = []
    for sentence in sentences:
        updated_sentence = []
        for char in sentence:
            if char.upper() in image_paths_dict:
                updated_sentence.append(image_paths_dict[char.upper()])
            else:
                updated_sentence.append(char)
        updated_sentences.append(updated_sentence)
    return updated_sentences

def display_sentence(sentence):
    for element in sentence:
        img = cv2.imread(element)

        if img is None:
            print("error")
        else:
            cv2.imshow('Display', img)

            cv2.waitKey(5000)  # Display for 5 seconds

            # Close the window after 5 seconds
            cv2.destroyAllWindows()


        
    cv2.destroyAllWindows()