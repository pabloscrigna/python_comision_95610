from django.urls import path
from django.contrib.auth.views import LogoutView

from Main.views import login_request, registrar_usuario 


urlpatterns = [
    path("login/", login_request, name="login"),
    path("register/", registrar_usuario, name="registrarse"), 
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
]