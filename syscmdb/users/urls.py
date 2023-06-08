from django.urls import path, re_path
from users.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('testdata', TestDataView.as_view()),
    re_path(r'^list', UserListView.as_view(), name='user_list'),
    path('add', UserAddView.as_view(), name='user_add'),
    path('update', UserUpdateView.as_view(), name='user_update'),
    path('delete', UserDeleteView.as_view(), name='user_delete'),
    path('status', UserStatusView.as_view(), name='user_status'),
]
