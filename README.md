# DIPProject
digital image processing project to process the image and extracting text and numbers.


developed in: python


libraries:
opencv
numpy
pytesseract
goslate
unicodedata

when the OCR is applied directly to a unprocessed image the result might not be too accurate.
inorder to improve accuracy before applying OCR on an digital image certain processing needs to be done on the image. the project deals with the same.

an application of the project is also implemented which is to translate the extracted text to any other language in utf-8 format.

so the project takes the image processes it and saves the image after each process is applied, then an OCR is used to extract text with relatively high accuracy(due to image processing) and then the text is translated to the desired language.
