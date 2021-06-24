from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    self = serializers.HyperlinkedIdentityField(view_name="users:user-detail")

    class Meta:
        model = User
        fields = (
            "self",
            "id",
            "username",
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        )
        extra_kwargs = {"password": {"write_only": True}}
        URL_FIELD_NAME = "self"

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
