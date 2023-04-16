from rest_framework.pagination import PageNumberPagination


class UserViewSetPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'


class GroupViewSetPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'


class PermissionViewSetPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'
    

class ArticlesViewSetPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'
    
    # def __init__(self, page_size=10) -> None:
    #     super().__init__()
    #     self.page_size = page_size