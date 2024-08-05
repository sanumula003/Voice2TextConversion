
import pyttsx3
import speech_recognition as sr 
import webbrowser
from datetime import datetime  
import pyjokes
import googlemaps  # Import the googlemaps library for location-based services

# Function to recognize speech input
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing.....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()  # Return the recognized text in lowercase
        except sr.UnknownValueError:
            print("Not Understanding")
            return ""  

# Function to convert text to speech
def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Function to get current weather information
def get_weather():
    import pyowm

    # Replace 'your-owm-api-key' with your actual OWM API key
    owm = pyowm.OWM('your-owm-api-key')

    # Replace 'your-city-name' with your city name
    observation = owm.weather_at_place('Hyderabad,IN')

    # Get the weather information
    weather = observation.get_weather()
    status = weather.get_detailed_status()
    temperature = weather.get_temperature('celsius')['temp']

    # Return the weather information as a string
    return f"The weather in Hyderabad, India is {status} with a temperature of {temperature} degrees Celsius."

# Function to get nearby places
def get_nearby_places(location, place_type):
    #gmaps = googlemaps.Client(key='your-google-places-api-key') 
    # Replace 'your-google-places-api-key' with your actual API key
    gmaps = googlemaps.Client(key='your-google-places-api-key')
    places = gmaps.places_nearby(location=location, radius=1000, type=place_type)
    nearby_places = [place['name'] for place in places['results']]
    return nearby_places

if __name__ == '__main__':
    while True:
        recognized_text = sptext()

        if "your name" in recognized_text:
            name = "My name is Sonus"
            speechtx(name)
        elif "old are you" in recognized_text:
            age = "I don't possess personal characteristics such as age or physical presence. I exist to assist you with information and tasks to the best of my abilities. So, in a sense, you could say I'm ageless! How can I assist you further?"
            speechtx(age)
        elif 'time' in recognized_text:
            current_time = datetime.now().strftime("%I:%M %p")  
            speechtx(current_time)
        elif 'youtube' in recognized_text:
            webbrowser.open("https://www.youtube.com/")
        elif 'google' in recognized_text:
            webbrowser.open("https://www.google.com/")
        elif "joke" in recognized_text:
            joke = pyjokes.get_joke(language="en", category="neutral")
            speechtx(joke)
        elif "weather" in recognized_text:
            weather_info = get_weather()
            speechtx(weather_info)
        elif "nearby" in recognized_text:
            location = "17.3850,78.4867"  # Hyderabad's coordinates
            place_type = "restaurant"   # You can change the place type to any desired category (e.g., gas_station, hospital, etc.)
            nearby_places = get_nearby_places(location, place_type)
            if nearby_places:
                speechtx("Here are some nearby " + place_type + "s:")
                for place in nearby_places:
                    speechtx(place)
            else:
                speechtx("No nearby " + place_type + "s found.")
        elif "exit" in recognized_text or "stop" in recognized_text:
            speechtx("Exiting the program. Goodbye!")
            break
