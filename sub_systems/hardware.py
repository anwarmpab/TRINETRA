# sub_systems/hardware.py

def control_device(device_name, state):
    print(f"[HARDWARE] Controlling {device_name}: {'ON' if state else 'OFF'}")
    # Add your GPIO, serial or simulation code here
