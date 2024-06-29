Voice-Controlled Assistant (Jarvis)

This project implements a voice-controlled assistant using Python, integrating various functionalities like speech recognition, text-to-speech conversion, web browsing, API interactions for weather and news, and AI-based interaction.

- Features :-

1. Speech Recognition : Utilizes the SpeechRecognition library to convert spoken commands into text.
2. Text-to-Speech : Implements pyttsx3 for converting text responses into spoken language.
3. Web Browsing : Opens websites such as Google, Facebook, Instagram, and YouTube based on user commands.
4. Application Control : Launches system applications like Notepad, Calculator, and Command Prompt.
5. Music Playback : Plays music from a custom music library using web browser integration.
6. Weather Information : Retrieves current weather conditions for a specified location using OpenWeatherMap API.
7. News Headlines : Fetches top news headlines using News API.
8. AI Interaction : Engages in conversation using a generative AI model (Google's GenerativeAI) for open-ended responses.

- Requirements :-

- Python 3.x
- Required Python libraries:
  - speech_recognition
  - pyttsx3
  - requests
  - google.generativeai
  - (Ensure dependencies are installed, e.g., `pip install -r requirements.txt`)
 
- Obtaining API Keys
1. Google Generative AI API [Google AI Studio](https://ai.google.dev/aistudio)
  Visit Google AI Studio and sign in with your Google account.
  Navigate to the Generative AI section and create a new project.
  Obtain the API key and replace "YOUR_GEN_AI_API_KEY" in ai_process function with your actual API key.
2. OpenWeatherMap API
  Sign up for a free account on [OpenWeatherMap](https://openweathermap.org/).
  After registration, obtain the API key from your account dashboard.
  Replace "YOUR_WEATHER_API_KEY" in get_weather function with your actual API key.
3. News API
  Register for a free API key at [NewsAPI](https://newsapi.org/).
  Copy your API key from the dashboard.
  Replace "YOUR_NEW_API_KEY" in process_command function where fetching news headlines with your actual API key.

- Usage :-

1. Clone the repository:
   ```
   git clone https://github.com/your-username/voice-controlled-assistant.git
   cd voice-controlled-assistant
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the program:
   ```
   python assistant.py
   ```

4. Activate Jarvis by saying "Jarvis" and issue commands such as opening websites, playing music, fetching weather, and more.

- Contributing :-

Contributions are welcome! If you have any suggestions, improvements, or new features to add, please open an issue or a pull request.

- License :-

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
