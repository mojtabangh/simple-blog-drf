from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Article

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ('__all__')
        # exclude = ('created', 'updated')

        def validate_title(self, value):
            if 'django' not in value.lower():
                raise serializers.ValidationError("Blog post is not about Django")
            return value
           

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'