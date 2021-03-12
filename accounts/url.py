from django.urls import path,include
from . import views

urlpatterns = [    
    path('signup/',views.signup,name="signup"),
    path('signup/profile',views.profile_view,name="profile"),
    path('signup/edit/',views.profile_edit,name="edit"),

    
]
app_name='accounts'