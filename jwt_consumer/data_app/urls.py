from django.urls import path
from .views import SecureDataView

urlpatterns = [
    path('secure-data/', SecureDataView.as_view(), name='secure_data'),
]
