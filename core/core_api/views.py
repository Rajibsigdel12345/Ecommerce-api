
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from core.core_api.mixins import ReadWriteSerializerMixin
from . import permissions
from core.core_api.serializers import UserReadSerializer, UserWriteSerializer


class UserViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    read_serializer_class = UserReadSerializer
    write_serializer_class = UserWriteSerializer
    permission_classes = [permissions.UserPermission]
