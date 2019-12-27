from django.urls import path,include
from .views import PermissionsView

urlpatterns = [
    path('updateTree/',PermissionsView.as_view()),
    path('getTreeData/',PermissionsView.as_view()),
    path('delTreeData/',PermissionsView.as_view()),
]