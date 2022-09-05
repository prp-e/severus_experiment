from fuzzywuzzy import fuzz
from fuzzywuzzy import process

commented_code = """import cv2
camera = cv2.VideoCapture(0)
while True:
    # Getting input from user and show webcam's image
"""

ai_code = """import cv2
camera = cv2.VideoCapture(0)
while True:
    # Getting input from user and show webcam's image
    ret, frame = camera.read()
    cv2.imshow('frame', frame)
"""
