from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
from langdetect import detect

# Initialize the Tkinter window
root = Tk()
root.geometry('1100x420')
root.resizable(0, 0)
root['bg'] = 'skyblue'

root.title('Language Translator')

# Add Label for input text
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)

# Input text field
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

# Add Label for output text
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)

# Output text field
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=130)

# Create an instance of GoogleTranslator to get the supported languages
translator = GoogleTranslator()

# Get supported languages from the Google Translator instance
languages = translator.get_supported_languages(as_dict=True)
language_names = list(languages.keys())  # List of language codes

# Dropdown for selecting target language
dest_lang = ttk.Combobox(root, value=language_names, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('choose language')

# Translation function
def Translate():
    input_text = Input_text.get()  # Get the input text from the entry box
    if input_text:
        # Step 1: Language Detection (using langdetect)
        detected_language = detect(input_text)  # Detect the language of the input text

        # Step 2: Translate using deep-translator (deep learning-based)
        target_language = dest_lang.get()  # Get the target language from the dropdown
        if target_language in languages:
            try:
                # Perform the translation using deep learning-powered Google Translator
                translated_text = GoogleTranslator(source=detected_language, target=target_language).translate(input_text)
                Output_text.delete(1.0, END)
                Output_text.insert(END, translated_text)  # Display translated text in the output box
            except Exception as e:
                Output_text.delete(1.0, END)
                Output_text.insert(END, f"Error: {str(e)}")
        else:
            Output_text.delete(1.0, END)
            Output_text.insert(END, "Please select a valid target language!")

# Translate button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180)

# Run the Tkinter main loop
root.mainloop()
