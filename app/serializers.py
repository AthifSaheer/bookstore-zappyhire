from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, BookReview


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create(
                email=validated_data['email'],
                username=validated_data['username']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ["id", "title", "author", "price", "quantity_in_stock", "genre", "isbn", "created_at"]


class BookReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookReview
        fields = ["id", "user", "book", "review", "rating", "created_at"]
