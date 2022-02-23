from rest_framework import pagination

class SmallPagination(pagination.PageNumberPagination):
    page_size=6

class LargePagination(pagination.PageNumberPagination):
    page_size=10
    page_query_param="sayfa"