from django.core.management.base import BaseCommand
from remo.models import SensorValue
from remo.modules.api import NatureRemoApi

def testhoge():
    temperature, humidity, illuminate = NatureRemoApi().fetch_sensor_values()
    sensor_value = SensorValue()
    sensor_value.temperature = sensor_values['te']['val']
    sensor_value.humidity = sensor_values['hu']['val']
    sensor_value.illumination = sensor_values['il']['val']
    sensor_value.save()











