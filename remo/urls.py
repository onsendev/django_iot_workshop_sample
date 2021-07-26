from django.urls import path

from . import views

app_name = 'remo'

urlpatterns = [
    # dashboard と invoke/アクションの名前　でアクセスできるようにしましょう

    # 追記 トップページ
    path('dashboard/', views.dashboard, name='index'),
    # 追記 家電の操作
    path('invoke/<str:action_name>', views.invoke, name='invoke'),
]
