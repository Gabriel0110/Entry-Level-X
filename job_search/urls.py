from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_search_index, name="job_search_index"),
    path("<int:pk>/", views.job_detail, name="job_detail"),
    #path("job_search_result/", views.)
]