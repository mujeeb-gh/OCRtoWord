from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from PIL import Image, ImageFilter
from docx import Document
import base64, pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create your views here.
# Image upload endpoint
@api_view(['POST'])
def upload_image(request):
  if request.method == 'POST':
    image_file = request.data.get('image')
    if image_file:
      try:
        image = ImageModel(file = image_file)
        image.save()
        global image_id
        image_id = image.id
        return Response({'message': 'Uploaded Successfully', 'image_id' : image_id}, status=status.HTTP_201_CREATED)
      except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
      return Response({'error': 'No image data provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
# Text extraction endpoint
@api_view(['POST'])
def extract_text(request):
  if request.method == 'POST':
    if image_id:
      try:
        image = ImageModel.objects.get(pk=image_id)
        if image.file.name.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')):
          with open(image.file.path, 'rb') as image_file:
            global extracted_text
            extracted_text = pytesseract.image_to_string(Image.open(image_file))
          extracted_text = extracted_text.replace('\n', ' ')
        else:
          return Response({'error': 'Unsupported image format.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'text': extracted_text}, status= status.HTTP_200_OK)
      except Exception as e:
        return Response({'error': f'Text extraction error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return Response({'error': 'No image identifier provided.'}, status=status.HTTP_400_BAD_REQUEST)   
      
# word document generation endpoint
@api_view(['POST'])
def generate_document(request):
  if request.method == 'POST':
    if extracted_text:
      document = Document()
      document.add_heading('Extracted Text', level)