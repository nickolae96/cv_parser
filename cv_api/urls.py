from django.urls import path

from cv_api.views import CVDataAPIView

urlpatterns = [
    path('personal/', CVDataAPIView.as_view(), name='personal'),
    path('experience/', CVDataAPIView.as_view(), name='experience'),
    path('education/', CVDataAPIView.as_view(), name='education'),
    path('all/', CVDataAPIView.as_view(), name='all'),
]
