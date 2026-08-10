from django.urls import path
from .import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('saveprofile/',views.save_profile,name='save_profile'),
    path('<int:id>/',views.resume,name='resume'),
    path('download/<int:id>/',views.download_resume,name='download_resume'),
    path('delete/<int:id>/',views.delete_profile,name='delete_profile'),
    path('update/<int:id>/',views.update_profile,name='update_profile'),
]