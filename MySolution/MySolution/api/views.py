from .serializer import Serializer
from .models import Courses
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend


# Create view for single course view
class CoursesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = Serializer
    lookup_url_kwarg = 'id'


# Create view for list course view
class CoursesListView(ListAPIView, CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = Serializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['start_date', 'end_date']
    ordering_fields = ['start_date']
