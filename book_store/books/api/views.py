
from rest_framework.generics import GenericAPIView
from books.models import Book,Comment
from books.api.serializers import BookSerializer,CommentSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin

# Concrete Views
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,CreateAPIView



#Permissions

from rest_framework import permissions

from books.api.permissions import IsAdminorStafforReadOnly,IsCommentOwnerorReadOnly


from rest_framework.exceptions import ValidationError

from books.api.pagination import SmallPagination,LargePagination



class BooklistCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookSerializer
    permission_classes=[IsAdminorStafforReadOnly]
    pagination_class=LargePagination




class BookDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAdminorStafforReadOnly]




class CommentCreateAPIView(CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



    def perform_create(self, serializer):
        book_id=self.kwargs.get('book_id')

        check_comments = Comment.objects.filter(book=book_id,owner_of_comment=self.request.user)

        if check_comments.exists():
            raise ValidationError('You cannot make more than one comment on a book')



        serializer.save(book_id=book_id,owner_of_comment=self.request.user)

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[IsCommentOwnerorReadOnly]









# class BooklistCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    

#     #Listing

#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     #Creating

#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)


