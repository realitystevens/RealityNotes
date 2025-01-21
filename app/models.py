import random
from django.db import models
from django.utils.timezone import datetime
from django.utils.html import strip_tags
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField
from decouple import config




def random_digits():
    return ''.join(random.choice('23456789') for i in range(5))

def hash_generate():
    return ''.join(random.choice('23456789') for x in range(3))



class Tag(models.Model):
    tag_name = models.CharField(default='', max_length=50, blank=False, null=False,)
    tag_hash = models.CharField(default=hash_generate, max_length=5, primary_key=True, unique=True, blank=False, null=False,)

    class Meta:
        ordering = ('tag_name', 'tag_hash',)

    def __str__(self):
        return self.tag_name




class Article(models.Model):
    url_hash = models.SlugField(max_length=5,  default=random_digits, primary_key=True, unique=True, help_text='Unique URL path for the Article', blank=False, null=False,)
    title = models.CharField(max_length=1000, blank=False, null=False, default='', help_text='Title of the Article')
    description = models.TextField(max_length=1000, blank=False, default='')
    image = CloudinaryField('image') if config('ENV') == 'PROD' else models.ImageField(upload_to='assets/article', blank=False, null=False, default='')
    image_alt = models.CharField(max_length=100, blank=False, null=False, default='') 
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    content = RichTextUploadingField()
    is_featured = models.BooleanField(default=False, help_text='Featured Article? (Will display as first Article on Homepage)')
    published_at = models.DateTimeField(default=datetime.now, editable=True, null=False, blank=False)

    def mins_read(self):
        """
            strip_tags() removes HTML tags from the content.
            split() splits the content into a list of words.
            len() returns the length of the list.
        """
        words_per_minute = 150
        num_of_words = len(strip_tags(self.content).split())

        mins_read = num_of_words / words_per_minute

        if mins_read < 1:
            mins_read = '1 Min Read'
        else:
            mins_read = f'{round(mins_read)} Mins Read'

        return mins_read

    class Meta:
        ordering = ('title', 'published_at', 'url_hash',)

    def __str__(self):
        return self.url_hash

