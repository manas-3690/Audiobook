import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
page = pdfReader.getPage(7)
text = page.extractText()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()