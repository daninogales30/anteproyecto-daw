from rest_framework import serializers
from persons.models import Person


class LeaderboardSerializer(serializers.ModelSerializer):
    total_workouts = serializers.IntegerField()

    class Meta:
        model = Person
        fields = ['username', 'total_workouts']