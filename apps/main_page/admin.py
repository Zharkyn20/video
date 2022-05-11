from django.contrib import admin
from django.utils.html import format_html
from .models import MainPage, Slider, Worker


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.image.url,
            width=150,
            height=150))

    image_tag.short_description = 'Фото'

    readonly_fields = ['image_tag', ]


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.image.url,
            width=150,
            height=150))

    image_tag.short_description = 'Фото'

    readonly_fields = ['image_tag', ]


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and MainPage.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = MainPage
