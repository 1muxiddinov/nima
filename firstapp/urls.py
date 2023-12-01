from django.urls import path
from .views import index,about,courses,team,testimonial,contact,index1,rus_tili,koreys_tili,ingliz_tili

urlpatterns = [
    path('', index, name="index"),
    path("about/",about, name="about"),
    path("courses/",courses, name="courses"),
    path("team/",team, name="team"),
    path("testimonial/", testimonial,name="testimonial"),
    path("contact/", contact,name="contact"),
    path("index1/", index1, name="index1"),
    path("rus_tili/", rus_tili, name="rus_tili"),
    path("koreys_tili/", koreys_tili, name="koreys_tili"),
    path("ingliz_tili/", ingliz_tili, name="ingliz_tili"),
]
