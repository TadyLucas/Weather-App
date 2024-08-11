from project import get_weather, convertKelvin, convertUnix, kmhToMs

def test_api_response():
    info, resp = get_weather("Prague")
    assert resp == 200

def test_kelvinToCelsius():
    units = "C"
    assert convertKelvin(294) == '20.9 °C'
    assert convertKelvin(300) == '26.9 °C'
def test_convertUnix():
    assert convertUnix(1721114173) == "09:16"
def test_kmhToMs():
    assert kmhToMs(3) == 10.8
