from django.urls import path
from . import views


urlpatterns = [
    path("signup/",views.userSignup.as_view()),
    path("getMembership/<email>",views.userMembership.as_view())
]
