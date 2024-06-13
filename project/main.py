from helper import *
import os
import cv2

sentences = [
    "hello world",
    "goodbye world",
    "i dont wanna be with you heinrichs",
    "come on heinrichs"
]

sentences_to_images = replace_letters_with_paths(sentences)


display_sentence(sentences_to_images[0])


