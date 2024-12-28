import os

if __name__ == "__main__":
    print("Welcom to RoboSpeaker 1.1.1 Created by Anurag Singh")

while True:
    x = input("Enter the text you want to speak: ")
    if x == "q":
        break
    command = f"say{x}"
    os.system("command")
