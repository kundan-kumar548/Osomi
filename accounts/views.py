from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.reverse import reverse
from django.db.models import Q
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import (
                                    LimitOffsetPagination,
                                    PageNumberPagination,
                                    PageLink
                                    )
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAdminUser,\
                                    IsAuthenticatedOrReadOnly,\
                                    IsAuthenticated,AllowAny
from rest_framework.generics import (CreateAPIView,ListAPIView,UpdateAPIView,
                                     RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView)


class UserDetailView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     queryset = User.objects.all()[1]
    #     return queryset


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer


class UserListView(viewsets.ModelViewSet):
    queryset = UserSignup.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SignupSerializer


class UserProfileView(viewsets.ModelViewSet):
    queryset = UsersProfile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UsersProfileSerializer


class ArtistAccountView(viewsets.ModelViewSet):
    queryset = ArtistAccount.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistAccountSerializer


class UserSignupView(CreateAPIView):
    model = UserSignup
    permission_classes = (AllowAny,)
    serializer_class = UserSignupSerializer


class LoginLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request):
        data = request.data
        print(data,type(data))
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            print(serializer,type(serializer))
            print(new_data,type(new_data))
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)












