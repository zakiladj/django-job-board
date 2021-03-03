from django.urls import path,include
from . import views

urlpatterns = [    
    path('',views.job_list,name="job_list"),
    path('<int:id>',views.job_details,name="job_details"),
]
