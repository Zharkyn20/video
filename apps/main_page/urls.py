from .views import MainPageViewSet, SliderViewSet, WorkerViewSet


"""This variable used in video/urls as media app's urls.
Then registering in Api Root"""
routeList = (
    (r'main_page', MainPageViewSet),
    (r'slider', SliderViewSet),
    (r'worker', WorkerViewSet),
)
