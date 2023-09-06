from django.db import models

# Create your models here.
class ImageModel(models.Model):
  title = models.CharField(max_length=255, blank=True, null=True)  # Optional title or description
  file = models.ImageField(upload_to='images/')  # Field to store the image file
  created_at = models.DateTimeField(auto_now_add=True)  # Timestamp indicating when the image was uploaded

  def __str__(self):
    return self.title if self.title else f"Image {self.id}"
  
class Document(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title for the document
    content = models.TextField()  # Text content of the Word document
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp indicating when the document was generated

    def __str__(self):
        return self.title if self.title else f"Document {self.id}"