from django.core.management.base import BaseCommand

from remo.models import SensorValue
from remo.modules.api import NatureRemoApi

class Command(BaseCommand):
    def handle(self, *args, **options):
        # 追記
        # センサーの値をAPIで取得し、SensorValueモデルを1件新たに保存
        temperature, humidity, illuminate = NatureRemoApi().fetch_sensor_values()
        sensor_value = SensorValue()
        sensor_value.temperature = temperature
        sensor_value.humidity = humidity
        sensor_value.illumination = illuminate
        sensor_value.save()
        
        