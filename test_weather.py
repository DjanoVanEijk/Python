# als dit cold zou zijn zou de test falen, omdat we verwachten dat het hot is bij 35 graden
from weather import get_weather
def test_get_weather():
    assert get_weather(35) == "hot"
