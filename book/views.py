from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Name
from .serializers import BookSerializers, NameSerializers
from rest_framework import generics


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


@api_view(['OPTIONS'])
def get_options(request):
    # Bu funksiya OPTIONS so'rovi uchun javob qaytaradi
    allowed_methods = ["GET", "POST", "PUT", "DELETE"]
    return Response(allowed_methods)


@api_view(['HEAD'])
def get_headers(request):
    # Bu funksiya GET bilan bir xil ishlaydi, lekin sirasida ma'lumotlar yo'q
    return Response(status=200)


class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        if books:
            serializers = BookSerializers(books, many=True)
            success = {
                "data": serializers.data
            }
            return Response(success)
        problem = {
            "Message": "Nothing"
        }
        return Response(problem)


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializers(data=data)

        title = data.get('title', None)
        author = data.get('author', None)
        price = data.get('price', None)

        if not title.isalpha():
            problem = {
                "Status": False,
                "Messgae": "Kitob sarlavhasi raqam bulmasligi kerak"
            }
            return Response(problem)

        if Book.objects.filter(title=title, author=author).exists():
            problem = {
                "Status": False,
                "Messgae": "Bu kitib bazada bor"
            }
            return Response(problem)

        if 1000 >= price <= 100000:
            problem = {
                "Status": False,
                "Messgae": "Narx qimmat yoki arzon"
            }
            return Response(problem)

        if serializer.is_valid():
            serializer.save()
            success = {
                "Status": True,
                "Book": serializer.data
            }
            return Response(success)
        problem = {
            "Status": False,
            "Messgae": "Error"
        }
        return Response(problem)


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            json_data = BookSerializers(book).data

            success = {
                "Status": True,
                "Book": json_data
            }
            return Response(success)
        except Exception:
            problem = {
                "Status": False,
                "Messgae": "Book Not found"
            }
            return Response(problem)


class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            success = {
                "Status": True,
                "Message": "Book deleted"
            }
            return Response(success)
        except Exception:
            problem = {
                "Status": False,
                "Messgae": "Book Not found"
            }
            return Response(problem)


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            data = request.data
            json_data = BookSerializers(instance=book, data=data, partial=True)
            if json_data.is_valid(raise_exception=True):
                json_data.save()
                success = {
                    "Status": True,
                    "Resalt": json_data.data
                }
            return Response(success)
        except Exception:
            problem = {
                "Status": False,
                "Messgae": "Book Not found"
            }
            return Response(problem)
