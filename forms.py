from django.forms import ModelForm
from .models import Post
import django_filters
class shop(ModelForm):
    class Meta:
        model = Post
        fields = ['title']

        

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']