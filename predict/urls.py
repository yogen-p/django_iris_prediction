from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
	path('', views.index, name='predict'),
	path('predict/', views.make_prediction,name='make_prediction'),
	path('history/', views.show_history, name='history'),
]
