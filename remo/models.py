from django.db import models


class SensorValue(models.Model):
    # https://swagger.nature.global/
    temperature = models.FloatField('摂氏')
    humidity = models.IntegerField('湿度')
    illumination = models.IntegerField('照度')
    created_at = models.DateTimeField('取得日時', auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.created_at} te:{self.temperature}, hu:{self.humidity}"