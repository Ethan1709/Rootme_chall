import base64
import pytesseract
import base64
from PIL import Image
from io import BytesIO
from selenium import webdriver

captcha_url = "http://challenge01.root-me.org/programmation/ch8/"

driver = webdriver.Firefox()

driver.get(captcha_url)

for i in range(0, 100):

    input_field = driver.find_element("name", "cametu")
    submit_button = driver.find_element("xpath", "//input[@value='Try']")

    response_content = driver.page_source.encode("utf-8").decode("utf-8")
    split_content = response_content.split('"')
    captcha_image = split_content[17][22:]

    try:
        captcha_bytes = base64.b64decode(captcha_image)
        image_stream = BytesIO(captcha_bytes)
        captcha_image = Image.open(image_stream)
        captcha_text = pytesseract.image_to_string(captcha_image)
        print(captcha_text)
        input_field.send_keys(captcha_text)
        submit_button.click()
    except Exception as e:
        print(f"Error: {e}")


