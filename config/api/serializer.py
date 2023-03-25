from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


class AuthorUsernameField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.first_name} {value.last_name}, username : {value.username}"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorUsernameField(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        filter_list = ["javascript", "c#", "golang"]

        for i in filter_list:
            if i in value:
                raise serializers.ValidationError(f"Don't use this word: {value}")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"


