from django.urls import path
from . import views

urlpatterns = [
  path('upload-image/', views.upload_image, name='upload-image'),
  path('extract-text/', views.extract_text, name='extract-text'),
  path('generate-document/', views.generate_document, name='generate-document')
]