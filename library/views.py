from django.db.transaction import atomic
from django.http import Http404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Library, Book, UserLibrary, LibraryActivity, LibraryBook
from library.serializers import LibrarySerializer, BookSerializer, LibraryBookSerializer, LibraryActivitySerializer, \
    UserLibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [AllowAny]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class UserLibraryViewSet(viewsets.ModelViewSet):
    queryset = UserLibrary.objects.all()
    serializer_class = UserLibrarySerializer
    permission_classes = [AllowAny]


class LibraryBookViewSet(viewsets.ModelViewSet):
    queryset = LibraryBook.objects.all()
    serializer_class = LibraryBookSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query_set = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        library_id = self.request.query_params.get('library_id')
        if user_id:
            query_set = query_set.filter(last_library_activity__user_id=user_id)

        if library_id:
            query_set = query_set.filter(last_library_activity__library_book__library_id=library_id)

        return query_set


class ActivityList(APIView):
    """
    When an activity is created it means its making a check-out from the library
    """

    def set_last_activity(self, library_book_id, activity):
        LibraryBook.objects.filter(pk=library_book_id).update(last_library_activity=activity)

    #  todo: delete method
    def get(self, request, format=None):
        activty = LibraryActivity.objects.all()
        serializer = LibraryActivitySerializer(activty, many=True)
        return Response(serializer.data)

    @atomic
    def post(self, request, format=None):
        serializer = LibraryActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.set_last_activity(request.data['library_book'], serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityDetail(APIView):
    """
    When an activity is updated it means its making the check-in of a book
    """

    def set_object(self, pk):
        try:
            activity = LibraryActivity.objects.get(pk=pk)
            activity.checked_in_at = timezone.now()
            activity.save()
            return activity
        except LibraryActivity.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        activity = self.set_object(pk)
        serializer = LibraryActivitySerializer(activity)
        return Response(serializer.data)
