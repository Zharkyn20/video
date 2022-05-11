from rest_framework import viewsets
from .models import MainPage, Slider, Worker
from .serializers import MainPageSerializer,\
    SliderSerializer, WorkerSerializer


class MainPageViewSet(viewsets.ModelViewSet):
    """
    Get main page
    """
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    http_method_names = ['get']


class SliderViewSet(viewsets.ModelViewSet):
    """
    Get main page's slider
    """
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    http_method_names = ['get']


class WorkerViewSet(viewsets.ModelViewSet):
    """
    Get workers
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    http_method_names = ['get']
