from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

from remo.modules.api import NatureRemoApi
from remo.modules.wbgt import Wbgt

from .models import SensorValue

# dashboard関数を書きましょう
# /remo/dashboard
@require_GET
def dashboard(request):
    # センサーの値のうち、最新20件を取得しましょう
    sensor_values = SensorValue.objects.order_by('-created_at')[:20]

    # 熱中症指数を計算しましょう
    latest_wbgt = None
    if sensor_values.exists():
        latest_wbgt = Wbgt.of(sensor_values[0].temperature, sensor_values[0].humidity)
    
    return render(request, 'remo/dashboard.html', {
        'title': 'Dashboard',
        'sensor_values': sensor_values,
        'latest_wbgt': latest_wbgt,
    })

@require_POST
def invoke(request, action_name):
    # 本来は例外がraiseされることを見越してtry-exceptを書くべきですが、
    # 今回は省略しています。
    NatureRemoApi().invoke_remo_action(action_name)
    return redirect('remo:dashboard')
