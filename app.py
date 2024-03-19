# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences


# sentence=[
#     "I am Vignesh",
#     "its me Vignesh",
#     "I am Akash",
#     "Akash send a gmail to Vignesh"
# ]

# tokenize = Tokenizer(num_words=100,oov_token="<OOV>")
# tokenize.fit_on_texts(sentence)
# word_index=tokenize.word_index
# sequences=tokenize.texts_to_sequences(sentence)
# padded = pad_sequences(sequences, maxlen=10)
# print("\nWord Index = " , word_index)
# print("\nSequences = " , sequences)
# print("\nPadded Sequences:")
# print(padded)

# # test_data = [
# #     'vignesh really mad',
# #     'Akash dog passed away'
# # ]

# # test_seq = tokenize.texts_to_sequences(test_data)
# # print("\nTest Sequence = ", test_seq)

# # padded = pad_sequences(test_seq, maxlen=10)
# # print("\nPadded Test Sequence: ")
# # print(padded)

###############################################################################################

# import speech_recognition as sr
# import pyttsx3

# # Initialize the recognizer and the text-to-speech engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Function to perform speech recognition
# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio_data = recognizer.listen(source)  # Listen for audio input

#     try:
#         # Use recognizer to perform speech recognition
#         text = recognizer.recognize_google(audio_data)
#         print(text)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand audio")
#         return None
#     except sr.RequestError as e:
#         print("Error fetching results; {0}".format(e))
#         return None

# # Function to speak the given text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Example usage
# if __name__ == "__main__":
#     text = recognize_speech()
#     if text:
#         # Process the recognized text and generate a response using your chatbot logic
#         print("Your chatbot response here")
#         speak(text)
#########################################################################################

# from vosk import Model, KaldiRecognizer
# import pyaudio
# import pyttsx3
# import json

# model = Model('C:\\Users\\zealzoft pvt ltd\\Desktop\\AI Modal\\vosk-model-small-hi-0.22')
# recognizer = KaldiRecognizer(model, 16000)

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# audio = pyaudio.PyAudio()
# stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()

# while True: 
#     data = stream.read(4096)
#     if len(data) == 0:
#         break
#     if recognizer.AcceptWaveform(data):
#         result = recognizer.Result()
#         print(result)
#         # Extracting the recognized text from the result
#         result_text = json.loads(result)['text']
#         print("Recognized Text:", result_text)
        
#         # Speak the recognized text
#         engine.say(result_text)
#         engine.runAndWait()

#*****************************************************************
# import tkinter as tk
# from vosk import Model, KaldiRecognizer
# import pyaudio
# import pyttsx3

# hindi_model = Model(r'C:\Users\Zeal\Desktop\Vignesh\L&T Demo\AI Modal\vosk-model-hi-0.22')
# english_model=Model(r'C:\Users\Zeal\Desktop\Vignesh\L&T Demo\AI Modal\vosk-model-small-en-in-0.4')

# mic = pyaudio.PyAudio()
# engine = pyttsx3.init()
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM')

# def get_command(language):
#     recognizer = KaldiRecognizer(hindi_model if language=='hi' else english_model ,16000)
#     listening = True
#     stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
#     while listening:
#         stream.start_stream()
#         try:
#             data = stream.read(4096)
#             if recognizer.AcceptWaveform(data):
#                 result = recognizer.Result()
#                 response = result[14:-3]
#                 print("Recognized response:", response)
#                 listening = False
#                 stream.close()
#                 return response
#         except OSError:
#             pass

# def greet_user(language):
#     if language == 'hi':
#         engine.say("नमस्ते, L&T में आपका स्वागत है। मैं कैसे मदद कर सकता हूँ?")
#     else:
#         engine.say("Hello, welcome to L&T. How can I help you?")
#     engine.runAndWait()

# def listen_hindi():
#     command = get_command('hi')
#     if command == "":
#         engine.say("मैं आपकी सहायता कैसे कर सकता हूँ? कृपया अपने प्रश्न बताएं।")
#         engine.runAndWait()
#     elif command == "हथौड़ा" or command == "हथौड़े का उपयोग":
#         engine.say('हथौड़ा एक उपकरण है, जो अक्सर एक हाथ का उपकरण होता है, जिसमें एक वजनदार "सिर" होता है जो एक लंबे हैंडल से जुड़ा होता है जिसे किसी वस्तु के एक छोटे से क्षेत्र पर प्रभाव डालने के लिए घुमाया जाता है। यह, उदाहरण के लिए, लकड़ी में कील ठोकना, धातु को आकार देना (फोर्ज की तरह), या चट्टान को कुचलना हो सकता है।')
#         engine.runAndWait()
#     else:
#         engine.say("मुझे अपने प्रश्न बताएं")
#         engine.runAndWait()

# def listen_english():
#     command = get_command('en')
#     if command == "":
#         engine.say("How may I help you, Please tell me your queries")
#         engine.runAndWait()
#     elif command == "hammer" or command == "hammer uses":
#         engine.say('A hammer is a tool, often a hand tool, consisting of a weighted "head" attached to a long handle that is swung to impact a small area of an object. This could be, for example, hammering nails into wood, shaping metal (like a forge), or crushing rock.')
#         engine.runAndWait()
#     else:
#         engine.say("Tell me your questions")
#         engine.runAndWait()

# def listen():
#     language = language_var.get()
#     if language == 'hi':
#         listen_hindi()
#     elif language == 'en':
#         listen_english()
#     else:
#         print("select the Language")


# # Create the Tkinter application window
# root = tk.Tk()
# root.title("Voice Assistant")

# # Function to handle language selection
# def set_language(language):
#     greet_user(language)

# # Add a dropdown to select language
# language_var = tk.StringVar()
# language_var.set('hi')

# language_dropdown = tk.OptionMenu(root, language_var, 'hi', 'en', command=set_language)
# language_dropdown.pack()

# # Add a button to start listening for commands
# listen_button = tk.Button(root, text="Listen", command=listen)
# listen_button.pack()

# # Start the Tkinter event loop
# root.mainloop()
#**************************************************************



# from flask import Flask, request, jsonify
# from vosk import Model, KaldiRecognizer
# import pyaudio
# import pyttsx3

# app = Flask(__name__)

# model = Model(r'C:\Users\Zeal\Desktop\Vignesh\L&T Demo\AI Modal\vosk-model-hi-0.22')
# recognizer = KaldiRecognizer(model, 16000)

# mic = pyaudio.PyAudio()
# engine = pyttsx3.init()
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM')

# @app.route('/greet', methods=['GET'])
# def greet_user():
#     speak("नमस्ते, L&T में आपका स्वागत है। मैं कैसे मदद कर सकता हूँ?")
#     return jsonify({"message": "Greeting sent."})

# @app.route('/listen', methods=['POST'])
# def listen():
#     content = request.json
#     command = content['command']
    
#     if command == "":
#         speak("मैं आपकी सहायता कैसे कर सकता हूँ? कृपया अपने प्रश्न बताएं।")
#     elif command == "हथौड़ा" or command == "हथौड़े का उपयोग":
#         speak('हथौड़ा एक उपकरण है, जो अक्सर एक हाथ का उपकरण होता है, जिसमें एक वजनदार "सिर" होता है जो एक लंबे हैंडल से जुड़ा होता है जिसे किसी वस्तु के एक छोटे से क्षेत्र पर प्रभाव डालने के लिए घुमाया जाता है। यह, उदाहरण के लिए, लकड़ी में कील ठोकना, धातु को आकार देना (फोर्ज की तरह), या चट्टान को कुचलना हो सकता है।')
#     else:
#         speak("मुझे अपने प्रश्न बताएं")

#     return jsonify({"message": "Response sent."})

# def speak(text):
#     engine.say(text)
#     engine.ru()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, request, jsonify
# import pyttsx3
from flask_cors import CORS
import psycopg2




app = Flask(__name__)
CORS(app)

conn = psycopg2.connect("postgresql://postgres:12345@localhost:5432/L&T")
cur=conn.cursor()    


# @app.route('/greet', methods=['POST'])
# def greet_user():
#     data=request.json
#     language=data['language']
#     if language=='hi':
#        res='नमस्ते, L&T में आपका स्वागत है। मैं कैसे मदद कर सकता हूँ?'
#        speak(res)
#     else:
#         res='Welcome to L&T,How May I help you?'
#         speak(res)
#     return jsonify({"message": res})


# def listen_hindi(command):
#     commands_dataset = {
#         "": "मैं आपकी सहायता कैसे कर सकता हूँ? कृपया अपने प्रश्न बताएं।",
#         "हथोड़ा" or 'हथौड़े का उपयोग': "हथौड़ा एक उपकरण है, जो अक्सर एक हाथ का उपकरण होता है, जिसमें एक वजनदार 'सिर' होता है जो एक लंबे हैंडल से जुड़ा होता है जिसे किसी वस्तु के एक छोटे से क्षेत्र पर प्रभाव डालने के लिए घुमाया जाता है। यह, उदाहरण के लिए, लकड़ी में कील ठोकना, धातु को आकार देना (फोर्ज की तरह), या चट्टान को कुचलना हो सकता है।",
#     }
    
#     res = commands_dataset.get(command, 'मुझे अपने प्रश्न बताएं')
#     speak(res)
#     return {"message": res, "response": res}  # Return response along with message

# def listen_english(command):
#     commands_dataset = {
#         "": "How may I help you, Please tell me your queries",
#         "hammer" or 'hammer uses': 'A hammer is a tool, often a hand tool, consisting of a weighted "head" attached to a long handle that is swung to impact a small area of an object. This could be, for example, hammering nails into wood, shaping metal (like a forge), or crushing rock.',
#     }
#     res = commands_dataset.get(command, 'Plese tell me Your Queries')
#     speak(res)
#     return {"message": res, "response": res}  # Return response along with message

# @app.route('/listen', methods=['POST'])
# def listen():
#     content = request.json
#     language = content['language']
#     command = content['command']
#     print("command", command)
#     if language == 'hi':
#         response = listen_hindi(command)  
#     elif language == 'en':
#         response = listen_english(command)  
#     else:
#         return jsonify({'error': 'Invalid language'})
    
#     response['message'] = 'Listening completed.'
#     return jsonify(response)  

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/check', methods=['POST'])
def Check():
    content = request.json
    language = content['language']
    cur = conn.cursor()  # Assuming 'conn' is your database connection object

    if language == 'hi':
        cur.execute('SELECT * FROM "Hindi_Data"')
    else:
        cur.execute('SELECT * FROM "English_Data"')

    data = cur.fetchall()
    flat = [inner for outer in data for middle in outer for inner in middle]
    print("data", flat)
    return jsonify(flat)





# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM')
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


