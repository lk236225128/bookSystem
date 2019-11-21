from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Book


# Create your views here.

def index(request):
    # return HttpResponse("hello")
    return render(request, 'bookList.html')


class BookListView(View):
    def get(self, request):
        all_books = Book.objects.all()
        # .order_by("xxx")[:3]

        return render(request, 'bookList.html', {
            "all_books": all_books,
        })


class BookDetailView(View):
    def get(self, request):
        id = request.GET.get('id', None)
        if id:
            book = Book.objects.get(pk=id)

            return render(request, 'bookDetail.html', {
                "book": book,
            })
        else:
            return render(request, '404.html')


class AddBookView(View):
    def get(self, request):
        return render(request, 'addBook.html')

    def post(self, request):
        bookName = request.POST.get('bookName', None)
        authorName = request.POST.get('authorName', None)
        introduction = request.POST.get('introduction', None)
        book = Book()
        book.bookName = bookName
        book.authorName = authorName
        book.introduction = introduction
        book.save()
        return HttpResponse('图书添加成功')

class UpdateBookView(View):
    def get(self, request):
        id = request.GET.get('id', None)
        if id:
            book = Book.objects.get(pk=id)
            return render(request, 'updateBook.html', {
                "book": book,
            })
        else:
            return HttpResponse('未查询到图书ID')

    def post(self, request):
        id = request.GET.get('id', None)
        bookName = request.POST.get('bookName', None)
        authorName = request.POST.get('authorName', None)
        introduction = request.POST.get('introduction', None)
        if id:
            book = Book.objects.get(pk=id)
            book.bookName = bookName
            book.authorName = authorName
            book.introduction = introduction
            book.save()
            return HttpResponse('图书添加成功')
        else:
            return HttpResponse('未查询到图书ID')



class DelBookView(View):
    def get(self, request):
        id = request.GET.get('id', None)
        book=Book.objects.get(pk=id)
        book.delete()
        return HttpResponse('图书删除成功')


