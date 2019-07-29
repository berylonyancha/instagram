from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
      image = models.ImageField(upload_to='images/')
      name = models.CharField(max_length =30)
      image_caption = HTMLField()
      post_date = models.DateTimeField(auto_now_add =True)
      user=models.ForeignKey(User)
      likes=models.IntegerField(default=0)

      def __str__(self):
          return self.name
      
      class Meta:
          ordering =['-post_date']
      
      def save_image(self):
          self.save()

      def delete_image(self):
          self.delete()

      @classmethod
      def all_images(cls):
          images = cls.objects.all()
          return images
      @classmethod
      def search_by_users(cls,term):
          result=cls.objects.filter(user__username__icontains=term)
          return result


