import os
import pyautogui
import pyaudio
import speech_recognition as sr
import time


def find_exe_path(filename):
    for root, dir, files in os.walk(r'C:\\'):
        for file in files:
            if file.lower().startswith(filename.lower()) and file.lower().endswith(".exe"):
               return os.path.join(root, file)

            
def get_key_words(voice):
    key_word = {
        'on':1,
        'play':2,
        'text': 3,
        'call': 4,
        'by': 5, 
        'start': 6,
        'open': 7
    }

    keywords_with_values = {}

    words = voice.split()

    current_keyword = None
    current_value = ''

    for word in words:
        if word.lower() in key_word:
            if current_keyword is not None:
                keywords_with_values[current_keyword] = current_value.strip()
                current_value = ''

            current_keyword = word.lower()
        elif current_keyword is not None:
            current_value += word + " "

    if current_keyword is not None:
        keywords_with_values[current_keyword] = current_value.strip()

    return keywords_with_values


def open_app(voice):
    start_words = ["open", 'start', 'on']
    action_words = ['play']

    for words in start_words:
        if words in voice:
            path = find_exe_path(voice[words])
            os.startfile(path)
            time.sleep(3)

    if "spotify" in path.lower():
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(2)

            for word in action_words:
                if word in voice:
                    pyautogui.write(voice[word])

            for key in ['enter','pagedown','tab','enter','enter']:
                    time.sleep(2)
                    pyautogui.press(key) 

    

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What would you like to do? ")
        audio = r.listen(source)
        try:
            voice = r.recognize_google(audio)
            print(f"I Beleive you said: {voice}")
            return voice
        
        
        except sr.UnknownValueError:
            print("I did not understand what you said")

if __name__ == "__main__":
    words = get_key_words(get_voice())

    open_app(words)
