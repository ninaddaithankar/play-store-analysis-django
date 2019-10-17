from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_dashboard, name='home-page'),
    path('predictor/', views.PredictorView.as_view(), name='predictor'),
]
