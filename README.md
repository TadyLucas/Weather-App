# CS50P Today forecast
### Video URL: https://youtu.be/ot9ZEuGZhvs


## Introduction
The __CS50P Weather App__ is a user-friendly application developed to provide real-time weather information for any location around the world.

This app utilizes data from the __OpenWeatherMap__ API to deliver:

-    _Accurate forecasts_
-    _Current weather conditions_
-    _Other meteorological details_

The application is built using __Python__ with a graphical user interface powered by __CustomTkinter__, making it:

-    _Visually appealing_
-    _Easy to use_
## Features
-       Current Weather: Access up-to-date weather information for any specified location.
-       Temperature Units: Option to view temperature in Celsius or Fahrenheit.
-       Search Functionality: Easily search for weather information by entering a city name.
-       Default City: Set a default city to display weather information on startup.
-       Appearance Mode: Switch between light and dark modes for a comfortable viewing experience.
-       Detailed Information: View additional weather details such as minimum and maximum temperatures,
        sunrise and sunset times, and wind speed.
-       Responsive Interface: The application adjusts smoothly to different screen sizes and resolutions.

## Preview
![Weather app preview](/assets/weather_app.png "Weather app") 
#### TO FIND LOCATION - YOU MUST ENTER THE LOCATION AND PRESS ENTER
## Libraries & everything that I use to, built this app

    CustomTkinter: A modern and customizable version of Tkinter used for creating the graphical user interface.
    
    PIL (Pillow): A Python Imaging Library used for handling and displaying weather icons.
    
    Requests: A simple HTTP library for making API requests.
    
    OpenWeatherMap API: A reliable weather data provider that the app uses to fetch weather information.

    io.BytesIO: A module that allows you to handle bytes data in memory.

    datetime: Provides classes for manipulating dates and times.
## What each function is doing

- read and make more interesting the Introduction text

- ### app_header(): 
  - Sets up the header part of the application, including the title label, an entry field for the location, and an option menu for choosing temperature units
- ### on_enter_key(event, entry):
  - __event__ = represents the event that triggered that function
  - __entry__ = this var represents the widget from gui application(you can get from it value by this line of code entry.get())
  - Handles the Enter key event to search for the weather of the entered location
- ### get_weather(location):
  - __location__ = takes name of the city that someone writes to the entry
  - Sends a request to the OpenWeatherMap API to fetch weather data for the specified location and stored in the info dictionary
- ### error(location):

  - __location__
  - Displays an error message in a new window if the specified location is invalid
- ### search(info):
  
  - __info__ = dictionary with values from OpenWeatherAPI
  - Displays the weather information, including the weather icon, temperature, and additional details. It also sets up buttons for more details and setting the default city
- ### default_city_get():
  - Retrieves the default city from the text file. If the file doesn't exist, it creates it with the default city (Prague)
- ### see_more(info):

  - Displays additional weather information(minimum, maximum temperatures, sunrise, sunset times, wind speed)
- ### convert functions
  - __convertUnix(uTime):__
  
    - __uTime__ = is time in Unix timestamp
    - Converts Unix timestamp to a human-readable time format
  - __kmhToMs(ms):__
  
    - __ms__ = the number that you want to convert, number must be (_int, float, short_) parameter 
    - Converts wind speed from meters per second to kilometers per hour
  - __convertKelvin(temp=0):__
  
    - Needs global variable names units that has value "__C__"(_Celsius_) or "__F__"(_Fahrenheit_)
    - Returns rounded value by 1 digit, with __°C__ or __°F__ 
    - __temp__ = temperature must be number 
    - Converts temperature from Kelvin to Celsius or Fahrenheit based on the selected unit

#### Contact
    Name of the project: CS50P Today forecast
    Name: Lukáš Zavadil
    GitHub: TadyLucas 
    edx: TadyLucas
    City: Czech Republic, Havlíčkův Brod
    Date: 18/7/2024
