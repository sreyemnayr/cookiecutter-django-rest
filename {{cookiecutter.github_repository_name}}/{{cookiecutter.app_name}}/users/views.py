from rest_framework import viewsets, mixins

from .models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        return super(UserViewSet, self).create(self, request, *args, **kwargs)