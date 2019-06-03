
from rest_framework import status, mixins, generics, filters, viewsets, permissions, serializers
from rest_framework.response import Response
from rest_framework.decorators import action

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from ..models import User
from ..permissions import IsAuthorOrReadOnly
from ..serializers import UserSerializer, GroupSerializer, UserAdminSerializer

class UserListView(generics.ListCreateAPIView):
    
    lookup_field = 'email'
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('is_active', 'gender')
    search_fields = ('email', 'first_name', 'last_name', 'mobile', '=gender', '=is_active')
    ordering_fields = '__all__'

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user.user_id)
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserAdminSerializer
         
        return UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'email'
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('is_active', 'gender')
    search_fields = ('email', 'first_name', 'last_name', 'mobile', '=gender', '=is_active')
    ordering_fields = '__all__'

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user.user_id)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserAdminSerializer
         
        return UserSerializer

class GroupListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
