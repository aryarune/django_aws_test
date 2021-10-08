from django.urls import path
from .views import Stub

urlpatterns = [
    path('stub/', Stub.as_view())
]