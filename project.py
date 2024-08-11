import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from io import BytesIO
import datetime

fontLabel = "Comic Sans MS"
info = {}
value = 0
app = ctk.CTk()
icon_label = None
location_label = None
other_info = None
see_more_info_frame = None
button = None
set_default_city = None
btn_frame = None
switch = None
units = "C"
default = "Prague"
selected_option = ctk.StringVar()
def main():
    app.geometry("400x500")
    app.title("CS50P Weather App")
    app.resizable(width=False, height=False)
    ctk.set_appearance_mode("system")
    app_header()
    # Get default loc
    while True:
        try:
            info, resp_code = get_weather(default_city_get())
            search(info)
            break
        except:
            continue

    app.mainloop()

def app_header():

    # H1
    label = ctk.CTkLabel(app, text="CS50P Today forecast", font=(fontLabel, 25))
    label.pack(pady=5)

    header_frame = ctk.CTkFrame(app, fg_color="transparent")
    header_frame.pack()
    # Where to write location
    location_entry = ctk.CTkEntry(header_frame, placeholder_text="Enter Location", width=200)
    location_entry.pack(pady=10, side="left")
    location_entry.bind("<Return>", lambda event: on_enter_key(event, location_entry))

    chooseMetrics = ctk.CTkOptionMenu(header_frame, variable=selected_option, values=["C", "F"], width=70, command=convertTemp)
    chooseMetrics.pack(pady=10, side="right")
    chooseMetrics.set("C")
def on_enter_key(event, entry):
    # When press enter it entry it will redirect there
    locationIn = entry.get().lower().strip()
    if locationIn == "" or locationIn == " ":
        raise ValueError("Is Empty")
    entry.delete(0, ctk.END)
    info, resp_code = get_weather(locationIn)
    search(info)
def mode(v):
    # Change theme based on switch
    ctk.set_appearance_mode(v)
def get_weather(loc):
    global info
    # Send API request to openWeatherAPI and gets the reponse
    api_key = open("api_key.txt", "r").read().strip()
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={loc}&appid={api_key}")

    if response.status_code == 200:
        print(response.status_code)
        # Format json to dict
        weather = response.json()
        info = {
            "temp": weather['main']['temp'],
            "feels_like": weather['main']['feels_like'],
            "temp_min": weather['main']['temp_min'],
            "temp_max": weather['main']['temp_max'],
            "description": weather['weather'][0]['description'],
            "weather_icon": weather['weather'][0]['icon'],
            "weather_location": weather["name"],
            "wind_speed": weather['wind']['speed'],
            "sunrise": weather['sys']['sunrise'],
            "sunset": weather['sys']['sunset'],
            "update_dt": weather['dt']
        }
        return info, response.status_code
    else:
        if __name__ == "__main__":
            error(loc)
        # When location is't found it will pop up TopLevelCTK window
def error(loc):
    # The error window
    err = ctk.CTkToplevel()
    err.geometry("300x150")
    err.title("Invalid Location")

    label = ctk.CTkLabel(err, text=f"Can't find {loc}")
    label.pack(pady=20)

    button = ctk.CTkButton(err, text="OK", command=err.destroy)
    button.pack(pady=10)
def search(info):
    global icon_label, location_label, other_info, button, see_more_info_frame, set_default_city, btn_frame, switch

    # Check if the objects exists and if the exists it will remove them. To prevent object multiplication
    if icon_label:
        icon_label.destroy()
        location_label.destroy()
        other_info.destroy()
    if see_more_info_frame:
        see_more_info_frame.destroy()

    # Get icon from response
    icon_url = f"https://openweathermap.org/img/wn/{info['weather_icon']}@2x.png"
    response = requests.get(icon_url)

    # Open the image
    image = Image.open(BytesIO(response.content))
    image = image.resize((120, 120), Image.LANCZOS)  # Resize the image
    icon = ImageTk.PhotoImage(image)

    # Create a new icon label
    icon_label = ctk.CTkLabel(app, image=icon, text="")
    icon_label.image = icon  # Keep a reference to avoid garbage collection
    icon_label.pack(pady=0)

    # Weather info and convert unix time
    weather_info = f"\nTemperature: {convertKelvin(info['temp'])}\nFeels like: {convertKelvin(info['feels_like'])}\n{info['description'].capitalize()}"
    weather_header = f"{info['weather_location']}"
    weather_time = datetime.datetime.fromtimestamp(info['update_dt'])

    # Display the place
    location_label = ctk.CTkLabel(app, text=weather_header, font=(fontLabel, 15), pady=0)
    location_label.pack(pady=0)

    # Display tempeture, feels like
    other_info = ctk.CTkLabel(app, text=weather_info, font=(fontLabel, 12))
    other_info.pack(pady=0)

    # Check if the objects exists and if the exists it will remove them. To prevent object multiplication
    if button:
        button.destroy()
    if set_default_city:
        set_default_city.destroy()
    if btn_frame:
        btn_frame.destroy()
    if switch:
        switch.destroy()

    # Setup the frame for buttons to be side by side
    btn_frame = ctk.CTkFrame(app, fg_color="transparent")
    btn_frame.pack(pady=10)

    # Create the SEE MORE button
    button = ctk.CTkButton(btn_frame, text="SEE MORE", command=lambda: see_more(info), width=20)
    button.pack(side='left', pady=2)

    # Button for setting default city
    set_default_city = ctk.CTkButton(btn_frame, text="Default city", command=lambda: default_city_set(info["weather_location"]), width=20)
    set_default_city.pack(side="left", pady=2)

    # Theme switcher
    switch = ctk.CTkSwitch(app, text="Mode", command=lambda: mode(switch.get()), onvalue="light", offvalue="dark")
    switch.pack(pady=0)
def default_city_set(loc):
    # Write the default city to the txt file
    with open("default.txt", "w") as file:
        file.write(loc)
    print("Default city set to " + loc)

def default_city_get():
    # Read the location from a file. If it not exists it will create as default value is Praha
    try:
        with open("default.txt", "r") as file:
            loc = file.readline()
        return loc
    except FileNotFoundError:
        with open("default.txt", "w") as file:
            file.write(default)
        return open("default.txt", "r")
def see_more(info):
    global see_more_info_frame

    # Check if the objects exists and if the exists it will remove them. To prevent object multiplication
    if see_more_info_frame:
        see_more_info_frame.destroy()
        see_more_info_frame = None
    else:
        # Create a frame to hold the additional info
        see_more_info_frame = ctk.CTkFrame(app, border_width=2, border_color="black")
        see_more_info_frame.pack(pady=20, padx=10, fill='both', expand=True)


        see_more_info = f"Min: {convertKelvin(info['temp_min'])} Max: {convertKelvin(info['temp_max'])}\n🌅Sun rise: {convertUnix(info['sunrise'])}\n🌇Sun set: {convertUnix(info['sunset'])}\nWind: {kmhToMs(info['wind_speed'])} km/h"
        see_more_info_label = ctk.CTkLabel(see_more_info_frame, text=see_more_info, font=(fontLabel, 12))
        see_more_info_label.pack(pady=10, padx=5)

def convertUnix(uTime):
    return datetime.datetime.fromtimestamp(uTime).strftime("%H:%M")
def kmhToMs(ms):
    return round(float(ms) * 3.6, 2)
def convertKelvin(temp = 0):
    if units == "C":
        return f"{round(float(temp) - 273.15, 1)} °C"
    elif units == "F":
        return f"{round(((float(temp) - 273.15) * 1.8) + 32, 1)} °F"

def convertTemp(param):
    global units
    units = param
    update()

def update():
    search(info)
if __name__ == "__main__":
    main()
