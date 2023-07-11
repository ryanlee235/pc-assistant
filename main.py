import os
import pyautogui
import pyaudio
import speech_recognition as sr
import time

            
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
        #if there is a word thats in the dick
        if word.lower() in key_word:
            #if pointer points to current word
            if current_keyword is not None:
                #adding key, with value pair
                keywords_with_values[current_keyword] = current_value.strip()
                current_value = ''

            current_keyword = word.lower()
        elif current_keyword is not None:
            current_value += word + " "

    if current_keyword is not None:
        keywords_with_values[current_keyword] = current_value.strip()

    return keywords_with_values

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("what would you like to do?")
        audio = r.listen(source)

        try:
            voice = r.recognize_google(audio)
            print(f"I beleive you said:  {voice}")
            return voice
        except sr.UnKnownValueError:
            print("I did not understand what you said, please try again! ")



def main(filename):
    start_words = ["on" ,'start']
    os.chdir('/Users/ryanlee/Desktop')

    current_directory = os.getcwd()

    files = os.listdir()
    for word in start_words:
        for file in files:
            if word in filename:
                if file.lower().startswith(filename[word].lower()):
                    os.startfile(file)
                    time.sleep(2)
                    
    
                    if filename[word].lower() == 'spotify':
                        play_music(filename)


def play_music(music):
    start_words = ["on" ,'start']
    action_words = ["play", "look up", "text"]
    
    for word in start_words:
        if word in music:
            pyautogui.hotkey("ctrl", 'l')
            time.sleep(3)

        for words in action_words:
            if words in music:
                pyautogui.write(music[words])
                time.sleep(2)

        for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
            pyautogui.press(key)
            

                

if __name__ == "__main__":
    word = get_key_words(get_voice())

    main(word)
