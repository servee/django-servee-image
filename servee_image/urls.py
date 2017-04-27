from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^upload/$", views.upload_photos, name="servee_image_upload_photos"),
    url(r"^recent/$", views.recent_photos, name="servee_image_recent_photos")
]
