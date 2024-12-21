from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt"))
]