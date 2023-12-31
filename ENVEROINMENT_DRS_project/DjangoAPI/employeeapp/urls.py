from django.urls import path

from .views import departmentlist,deletedept,employeeview,deleteemployee,savefile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('department/',departmentlist),
    path('department/<int:id>/',deletedept),
    path("employee/",employeeview),
    path('employee/<int:id>/',deleteemployee),
    path('employee/savefile/',savefile),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)