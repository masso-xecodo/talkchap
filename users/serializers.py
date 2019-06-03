from rest_framework import serializers
from django.contrib.auth.models import Group

from .models import User

# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """

#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)

#         # Instantiate the superclass normally
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)

# class UserSerializer(DynamicFieldsModelSerializer):
    
#     class Meta:
#         model = User
#         #fields = ('url', 'username', 'email', 'firstname', 'lastname', 'mobile', 'status')

class UserSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='user-detail',
                                              lookup_field='email')

    class Meta:
        model = User
        fields = ['url', 'user_id', 'email', 'first_name', 'last_name', 'date_of_birth', 'password', 'mobile', 'is_active', 'author']
        read_only_fields = ['user_id', 'is_active', 'author']

class UserAdminSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail',
                                              lookup_field='email')

    class Meta:
        model = User
        fields = ['url', 'user_id', 'email', 'first_name', 'last_name', 'date_of_birth', 'password', 'mobile', 'is_active', 'author']
        read_only_fields = ['user_id', 'author']

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('name',)
