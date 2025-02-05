# import os

# if __name__ == "__main__":
#     print("Welcom to RoboSpeaker 1.1.1 Created by Anurag Singh")

# while True:
#     x = input("Enter the text you want to speak: ")
#     if x == "q":
#         break
#    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
#     os.system(command)


import os
import platform


def speak(text):
    system_platform = platform.system()
    if system_platform == "Windows":
        # Use PowerShell's built-in speech synthesis
        command = f"powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}');\""
    else:
        print("Unsupported operating system.")
        return
    os.system(command)


if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1.1 Created by Anurag Singh")

    while True:
        x = input("Enter the text you want to speak (or 'q' to quit): ")
        if x.lower() == "q":
            print("Exiting RoboSpeaker. Goodbye!")
            break
        speak(x)
