from playsound import playsound
from gtts import gTTS
import os
import PyPDF2

def convert_to_audio(text):
    audio = gTTS(text=text, lang= 'hu')
    audio.save("textaudio.mp3")
    playsound("textaudio.mp3")
    os.remove("textaudio.mp3")

book = open('vuk.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.getPage(1)
text = page.extractText()

convert_to_audio(text)