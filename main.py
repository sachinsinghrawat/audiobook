import pyttsx3
import PyPDF2
import tkinter  as tk
from tkinter.filedialog import askopenfilename
from tkinter import  filedialog


def speak(file_path):
  book = open(file_path, "rb")
  pdf_converter = PyPDF2.PdfReader(book)

  total_pages = len(pdf_converter.pages)

  speaker = pyttsx3.init()
  speaker.setProperty("rate" , 130)

  voices = speaker.getProperty("voices")
  speaker.setProperty("voice" , voices[1].id)
  content = ""

  for nums in range(total_pages):
    page = pdf_converter.pages[nums]
    text = page.extract_text()
    content = content + text;
    speaker.say(text)
    speaker.runAndWait()


  speaker.save_to_file(content , 'audio.mp3')
  speaker.runAndWait()



def browse():
  filetype = (("pdf files" , "'*.pdf") , ("all files" , "*.*"))
  filepath = filedialog.askopenfilename(initialdir='/' , title="select a pdf", filetypes=filetype)
  print(filepath)
  speak(filepath)



root = tk.Tk()

root.geometry("500x500")

root.title("Pdf - Reader ")

label_text = tk.Label(text="Browse Pdf to read ")
label_text.pack(padx = 20 , pady = 30)

btn = tk.Button(text="browse files" , command=browse)
btn.pack(padx=20  , pady = 20)


# file_path = browse()

root.mainloop()



