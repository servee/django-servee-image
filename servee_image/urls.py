from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^upload/$", "servee_image.views.upload_photos", name="servee_image_upload_photos"),
    url(r"^recent/$", "servee_image.views.recent_photos", name="servee_image_recent_photos")
)
