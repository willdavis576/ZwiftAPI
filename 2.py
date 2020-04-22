import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2


img = cv2.imread('testImage.PNG')
cv2.imshow("test", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey", gray)
cv2.waitKey(0)
# img = Image.open('testImage.PNG')
text = tess.image_to_string(gray)

print(text)
