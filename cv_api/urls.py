from django.urls import path

from cv_api.views import CVDataAPIView

urlpatterns = [
    path('<str:section>/', CVDataAPIView.as_view(), name='section.detail'),
]
