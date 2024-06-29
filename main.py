import speech_recognition as sr  # Importing the SpeechRecognition library
import webbrowser  # Importing the webbrowser module for opening URLs
import pyttsx3  # Importing pyttsx3 for text-to-speech conversion
import musicLibrary  # type: ignore # Assuming this is a custom module for music library management
import requests  # Importing requests for making HTTP requests
import google.generativeai as genai  # Importing a module for AI interaction
import sys  # Importing sys for system-specific parameters and functions
import os  # Importing os for interacting with the operating system

# Initializing the SpeechRecognition recognizer and pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for AI interaction using generative AI
def ai_process(command):
    genai.configure(api_key="AIzaSyBu-gDKnUkpPIQNcuO6IYck-8y0HXTV22A")

    # Configuration for AI model generation
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Creating a generative AI model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat = model.start_chat(history=[])

    while True:
        # Sending user command to the AI model
        response = chat.send_message(command, stream=True)
        response.resolve()
        ans = response.text.replace("*", "")  # Cleaning up response text

        print(ans)  # Printing AI-generated response
        speak(ans)  # Speaking AI-generated response

        # Listening for user's next command
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")

        try:
            # Recognizing user's speech using Google Speech Recognition
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")

            # Exiting AI interaction loop if user says 'exit'
            if command == 'exit':
                speak("Exiting.")
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("I didn't catch that. Please repeat.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, there was an error with the speech recognition service.")

# Function to fetch and speak weather information
def get_weather(location):
    api_key = "0556eaaf4a67643fad3f63570015a807"
    if not api_key:
        error_message = "Weather API key is not set."
        print(error_message)
        speak(error_message)
        return

    # Constructing URL for weather API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        # Parsing weather data from API response
        weather_data = response.json()
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        pres = weather_data['main']['pressure']
        hum = weather_data['main']['humidity']
        weather_report = f"The current temperature in {location} is {temp} degrees Celsius with {description}. The Air Pressure is {pres}. The Humidity is {hum}"
        print(weather_report)
        speak(weather_report)
    else:
        error_message = "Sorry, I couldn't fetch the weather details. Please try again."
        print(error_message)
        speak(error_message)

# Function to process user commands
def process_command(command):
    if command == 'stop':
        sys.exit(0)

    # Opening various websites based on user commands
    if "open google" in command:
        print("Opening Google.")
        speak("Opening Google.")
        webbrowser.open("http://www.google.com")

    elif "open facebook" in command:
        print("Opening Facebook.")
        speak("Opening Facebook.")
        webbrowser.open("http://www.facebook.com")

    elif "open instagram" in command:
        print("Opening Instagram.")
        speak("Opening Instagram.")
        webbrowser.open("http://www.instagram.com")

    elif "open youtube" in command:
        print("Opening YouTube.")
        speak("Opening YouTube.")
        webbrowser.open("http://www.youtube.com")

    # Opening system applications based on user commands
    elif "open notepad" in command:
        os.system("notepad.exe")

    elif "open calculator" in command:
        os.system("calc.exe")

    elif "open command prompt" in command:
        os.system("cmd.exe")

    # Playing music based on user command using a custom music library
    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            print(f"Song '{song}' not found in the music library.")
            speak(f"Sorry, I couldn't find the song '{song}'.")

    # Fetching and speaking news headlines
    elif "news" in command:
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f062292942e6411cb7c447c91568f217")
        if req.status_code == 200:
            news_data = req.json()
            articles = news_data.get('articles', [])
            for article in articles:
                print(article['title'])
                speak(article['title'])
        else:
            print("Failed to fetch news articles")
            speak("Failed to fetch news articles")

    # Fetching weather information based on user command
    elif command.startswith("weather"):
        location = command.split(" ")[1]
        get_weather(location)

    else:
        # Processing user command using AI interaction function
        ai_process(command)


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            # Listening for wake word 'jarvis'
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                print("Recognizing...")

            word = recognizer.recognize_google(audio).lower()
            print(f"Heard: {word}")

            if word == 'jarvis':
                speak("Yes?")

                # Listening for user command after wake word detection
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    speak("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=1)
                    print("Recognizing command...")
                    speak("Recognizing command...")

                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")

                # Processing user command based on recognized speech
                process_command(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
