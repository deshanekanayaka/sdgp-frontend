from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.local_account_login, name="local_account_login"),
    path("success/", lambda request: render(request, "success.html"), name="success"),
]
