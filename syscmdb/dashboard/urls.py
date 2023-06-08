from django.urls import path
from dashboard.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'/', IndexView.as_view(),name='index')
]
