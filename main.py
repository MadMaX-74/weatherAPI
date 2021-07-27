from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

apikey = 'd814489c3d2cd56301f7fd51d55fd532'
owm = OWM(apikey)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Moscow,RUS')
w = observation.weather
temperature = w.temperature('celsius')
temp_moscow = temperature['temp']
print(f'В москве {temp_moscow} градус тепла')