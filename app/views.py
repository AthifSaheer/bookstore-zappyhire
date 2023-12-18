from .serializers import UserSerializer, BookSerializer, BookReviewSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from .models import Book


class RegisterView(APIView):
    def post(self, request):
        """
        Given user basic details such as username, email and password. Create a new user.
        """

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BookView(APIView):
    def get(self, request):
        """
        List all books.
        """

        book_objects = Book.objects.filter(
            is_active=True
        ).order_by(
            '-bookreview__rating'
        ).distinct()
        serializer = BookSerializer(book_objects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        Given book details title, author, price, quantity_in_stock, genre, isbn.
        Create a new book.
        """

        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BookDetailedView(APIView):
    def put(self, request, pk):
        """
        Update book by given details like title, author, price, quantity_in_stock, genre, isbn.
        """

        try:
            book_object = Book.objects.get(id=pk, is_active=True)
        except Book.DoesNotExist:
            return Response(
                {"messsge": "Invalid book ID!"},
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = BookSerializer(book_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a book by given id.
        """

        try:
            book_object = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response(
                {"messsge": "Invalid book ID!"},
                status=status.HTTP_204_NO_CONTENT
            )

        book_object.is_active = False
        book_object.save()
        return Response({"messsge": "Successfully deleted."}, status=status.HTTP_200_OK)
        
class BookReview(APIView):
    def post(self, request, pk):
        """
        Submit a book review by review text and rating.
        """

        serializer = BookReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
