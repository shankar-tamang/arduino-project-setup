import tkinter as tk
import requests

ESP_IP = "192.168.23.48"  # Replace with your ESP32's IP address
ESP_PORT = 80  # Typically port 80 for HTTP

def turn_on():
    url = f"http://{ESP_IP}:{ESP_PORT}/on"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("LED turned ON")
        else:
            print(f"Failed to turn LED ON (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to ESP32: {e}")

def turn_off():
    url = f"http://{ESP_IP}:{ESP_PORT}/off"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("LED turned OFF")
        else:
            print(f"Failed to turn LED OFF (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to ESP32: {e}")

# Create the main window
root = tk.Tk()
root.title("ESP32 LED Control")

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create buttons to control LED
on_button = tk.Button(frame, text="Turn ON", width=10, command=turn_on)
on_button.grid(row=0, column=0, padx=10, pady=10)

off_button = tk.Button(frame, text="Turn OFF", width=10, command=turn_off)
off_button.grid(row=0, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
