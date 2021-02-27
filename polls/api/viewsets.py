from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from polls.models import *
class myfirstViewset(mixins.ListModelMixin, viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    def list(self, request, *args, **kwargs):
        serializer = UserPrettySerializer(request.user)
        return Response(serializer.data)
class SignupViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(id = serializer.data["id"])
        user.set_password(serializer.data["password"])
        user.is_active = True
        user.save()
        headers = self.get_success_headers(serializer.data)
        serializer = UserPrettySerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    