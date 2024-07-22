import win32com.client
import sys

def speak_text(text):
    # Initialize the SAPI.SpVoice object
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # Speak the provided text
    speaker.Speak(text)

if __name__ == "__main__":
    # Check if a command line argument was provided
    if len(sys.argv) != 2:
        print("Usage: python speech.py \"text_to_speak\"")
        sys.exit(1)

    # Retrieve the text from the command line arguments
    text = sys.argv[1]
    
    # Speak the text
    speak_text(text)
