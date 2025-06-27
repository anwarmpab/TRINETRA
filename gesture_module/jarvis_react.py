# gesture_module/jarvis_react.py

from sub_systems.speech import speak
from sub_systems.gui import update_ui
from sub_systems.analytics import log_event
from sub_systems.hardware import control_device
from datetime import datetime

def trigger_action(gesture, brain_state="neutral"):
    time_hour = datetime.now().hour

    if gesture == "Fist":
        speak("System activated")
        update_ui("Activating protocols")
        control_device("motor", True)
        log_event("gesture", "Fist gesture triggered full activation")

    elif gesture == "Thumbs Up":
        speak("All systems go")
        control_device("led", True)
        log_event("gesture", "Thumbs Up gesture triggered LED on")

    elif gesture == "Peace":
        speak("Engaging stealth mode")
        update_ui("Stealth enabled")
        log_event("gesture", "Peace gesture triggered stealth mode")

    elif gesture == "Open Palm" and brain_state == "drowsy" and time_hour >= 21:
        speak("You seem tired. Suggesting shutdown.")
        update_ui("Entering power-saving mode")
        log_event("eeg", "Open Palm with drowsy brain after 9 PM triggered power save")

    else:
        speak("No defined action for this gesture.")
        update_ui("Idle")
        log_event("gesture", f"No action mapped for gesture: {gesture}")
