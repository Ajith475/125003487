import speech_recognition as sr
import pyttsx3
import sys

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(Text):
    eng = pyttsx3.init()
    eng.say(Text)
    eng.runAndWait()

# Function to process the audio file
def process_audio_file(file_path):
    try:
        # Load the audio file
        with sr.AudioFile(file_path) as source:
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            # Record the audio
            audio_data = r.record(source)
            
            # Recognize the audio using Google Web Speech API
            Text = r.recognize_google(audio_data)
            Text = Text.lower()

            print(Text)
            SpeakText(Text)
            
    except sr.RequestError as e:
        print("Error with the request; {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unknown error occurred")

# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python voice.py sample.wav")
        sys.exit(1)

    audio_file = sys.argv[1]
    process_audio_file(audio_file)
