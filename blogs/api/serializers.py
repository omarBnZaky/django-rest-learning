from rest_framework import serializers
from blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title', 'message', 'user', 'date_updated','slug','image']
