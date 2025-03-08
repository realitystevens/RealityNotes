from django.db import models
from decouple import config
from django.utils.timezone import datetime
from django.utils.html import strip_tags
from project.utils import hash_generate, handle_image_upload , generate_image_caption, get_content_description
from ckeditor.fields import RichTextField



# Fix migration issue in .0001_initial.py
def random_digits():
    return ""

class Tag(models.Model):
    tag_name = models.CharField(default='', max_length=50, blank=False, null=False,)
    tag_hash = models.CharField(default="", max_length=5, primary_key=True, unique=True, blank=True, null=False,)

    def save(self, *args, **kwargs):
        if not self.tag_hash:
            self.tag_hash = hash_generate(5)
        super(Tag, self).save(*args, **kwargs)


    class Meta:
        ordering = ('tag_name', 'tag_hash',)
        verbose_name_plural = 'Tags'


    def __str__(self):
        return self.tag_name




class Article(models.Model):
    url_hash = models.SlugField(max_length=5,  default="", primary_key=True, unique=True, help_text='Unique URL path for the Article', blank=True, null=False,)
    title = models.CharField(max_length=1000, blank=False, null=False, default='', help_text='Title of the Article')
    description = models.TextField(max_length=1000, blank=True, default='', help_text='Description of the Article. Autogenerated (via Gemini AI) if not provided')
    image = models.ImageField(upload_to='assets/article', blank=True, default='', help_text='Image field for use in Development Environment')
    image_url = models.URLField(max_length=1000, blank=True, default='', help_text='Image URL field for use in Production Environment')
    image_alt = models.CharField(max_length=500, blank=True, null=False, default='', help_text='Image Alternative Text (autogenerating from image if not provided). Autogeneration is done using AI') 
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    content = RichTextField()
    is_featured = models.BooleanField(default=False, help_text='Featured Article? (Will display as first Article on Homepage)')
    published_at = models.DateTimeField(default=datetime.now, editable=True, null=False, blank=False)

    
    def mins_read(self):
        """
        Calculate the estimated reading time for the article.
        """
        words_per_minute = 150
        num_of_words = len(strip_tags(self.content).split())
        mins_read = max(1, round(num_of_words / words_per_minute))
        return f'{mins_read} Min Read' if mins_read == 1 else f'{mins_read} Mins Read'


    def save(self, *args, **kwargs):
        if not self.url_hash:
            self.url_hash = hash_generate(5)

        if self.image:
            raw_image = self.image
            if config('ENV') == 'PROD':
                image_url = handle_image_upload(raw_image)
                self.image_url = image_url
                """
                If the image is uploaded to the cloud and url is saved in self.image_url, 
                the image field (self.image) is set to empty.
                """
                self.image = ""
            else:
                self.image = raw_image
            
            if not self.image_alt:
                if self.image_url:
                    self.image_alt = generate_image_caption(self.image_url, False)
                else:
                    self.image_alt = generate_image_caption(self.image, True)

        if not self.description:
            self.description = get_content_description(self.title, self.content)
        super(Article, self).save(*args, **kwargs)


    @property
    def final_image_url(self):
        return self.image.url if self.image else self.image_url

    
    class Meta:
        ordering = ('title', 'published_at', 'url_hash',)
        verbose_name_plural = 'Articles'


    def __str__(self):
        return self.url_hash



class WebsiteDescription(models.Model):
    content = models.TextField(max_length=9000, blank=False, null=False, default='')
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Website Description'

    def __str__(self):
        return self.content
    