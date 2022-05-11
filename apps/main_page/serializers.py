from rest_framework import serializers
from .models import MainPage, Slider, Worker


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
