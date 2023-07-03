import base64
import requests

# URL of the CAPTCHA image
captcha_url = "http://challenge01.root-me.org/programmation/ch8/captcha.php"

# Request the CAPTCHA image
response = requests.get(captcha_url)
captcha_data = response.content

# Decode the base64 image data
captcha_image = base64.b64decode(captcha_data)

# Save the CAPTCHA image to a file (optional)
with open("captcha.png", "wb") as image_file:
    image_file.write(captcha_image)

# TODO: Implement your CAPTCHA solving logic here
# You can use libraries like OpenCV or Tesseract to process and solve the CAPTCHA image

# Example: Print the base64 data of the CAPTCHA image
print(captcha_data)
