from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = 'id','url','username','email','first_name','last_name'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')

    class Meta:
        model = Address
        fields = ('id','url','address', 'landmark', 'city', 'state', 'pin', 'country')
        # fields = '__all__'


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users-detail')
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserSignup
        fields = 'id','url','user','contact_number'


class UsersProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="usersprofile-detail")
    user = SignupSerializer(read_only=True)
    address = AddressSerializer(read_only=True,many=True)

    class Meta:
        model = UsersProfile
        # fields = '__all__'
        fields = ('id','url','user','date_of_birth','gender','website','bio','address')


class ArtistAccountSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="artistaccount-detail")

    class Meta:
        model = ArtistAccount
        # fields = '__all__'
        fields = ('id','url','user','email2','specialist_In')


class UserSignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=60)
    email = serializers.CharField(max_length=60)
    password = serializers.CharField(max_length=60)
    contact_number = serializers.CharField()
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = User.objects.filter(email=data['email'])
        if email.exists():
            raise ValidationError('email already exists')
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        ins = UserSignup(
            user=user,
            contact_number = validated_data['contact_number']
        )
        ins.save()
        token_object, created = Token.objects.get_or_create(user=user)
        validated_data['token'] = token_object.key
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=60, read_only=True)
    last_name = serializers.CharField(max_length=60, read_only=True)
    email = serializers.EmailField(label='Email address', allow_blank=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('email','password','token')

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data['password']
        if not email and not email:
            raise ValidationError("An email or username is required to login")

        user = User.objects.filter(email=email).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials please try again.')
        data['first_name'] = user_obj.first_name
        data['last_name'] = user_obj.last_name
        email = data.get("email")
        password = data.get("password")
        user = authenticate(username=email, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return data