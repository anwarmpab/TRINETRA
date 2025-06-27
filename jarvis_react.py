import os
import pyttsx3
import datetime
import webbrowser

class JarvisReact:
    def __init__(self):
        self.speaker = pyttsx3.init()
        self.command_map = {
            "fist": self.launch_notepad,
            "palm": self.minimize_all,
            "thumbs up": self.motivate,
            "peace": self.say_status,
            "victory": self.say_time,
            "three fingers": self.open_youtube,
            "ok": self.shutdown_prompt,
            "rock": self.say_energy_status,
            "call me": self.initiate_call_simulation,
            "stop": self.shutdown_all_systems,
        }

    def react(self, gesture_label):
        action = self.command_map.get(gesture_label.lower())
        if action:
            action()
        else:
            print(f"⚠️ No action mapped for gesture: {gesture_label}")
            self.speak(f"Gesture {gesture_label} is not yet mapped.")

    def speak(self, message):
        print(f"🗣️ JARVIS: {message}")
        self.speaker.say(message)
        self.speaker.runAndWait()

    # Gesture Action Methods
    def launch_notepad(self):
        self.speak("Opening Notepad.")
        os.system("notepad.exe")

    def minimize_all(self):
        self.speak("Minimizing all windows.")
        os.system("powershell -command \"(new-object -com shell.application).minimizeall()\"")

    def motivate(self):
        self.speak("Hello Anwar, you're doing great! Keep it up.")

    def say_status(self):
        self.speak("Vision system is stable and tracking gestures.")

    def say_time(self):
        now = datetime.datetime.now()
        self.speak(f"The current time is {now.strftime('%I:%M %p')}.")

    def open_youtube(self):
        self.speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    def shutdown_prompt(self):
        self.speak("Should I shut down the system? Awaiting confirmation.")

    def say_energy_status(self):
        self.speak("Power reserves are at full capacity, Anwar.")

    def initiate_call_simulation(self):
        self.speak("Simulating call request. Unfortunately, mobile access is restricted here.")

    def shutdown_all_systems(self):
        self.speak("All systems going offline. Goodbye.")
        os.system("shutdown /s /t 5")


# Utility functions for external calls
engine = pyttsx3.init()

def speak(message):
    print(f"🗣️ {message}")
    engine.say(message)
    engine.runAndWait()

def trigger_action(gesture):
    jarvis = JarvisReact()
    jarvis.react(gesture)
