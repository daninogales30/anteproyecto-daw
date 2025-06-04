from rest_framework import serializers
from persons.models import Person


class TopBloggerSerializer(serializers.ModelSerializer):
    entry_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'username', 'entry_count', 'profile_picture')
