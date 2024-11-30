import streamlit as web
from PIL import Image

web.subheader("Color to Grayscale Converter")

with web.expander("Start camera"):
    camera_image = web.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L') #turns the image black and white
    web.image(gray_camera_img)