from django.urls import path
from django.views.generic import TemplateView

app_name = "vehiculo"

urlpatterns = [
    path("", TemplateView.as_view(template_name="vehiculo/index.html"), name="home"),
]