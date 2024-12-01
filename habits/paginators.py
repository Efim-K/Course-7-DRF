from rest_framework.pagination import PageNumberPagination


class ViewPagination(PageNumberPagination):
    """
    Класс для пагинации результатов вывода списка
    """

    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 5
