from rest_framework import serializers
from ...models import Task
from accounts.models import User

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title", "description", "done", "created_date", "updated_date"]

    def create(self, validated_data):
        validated_data["user"] = User.objects.get(
            id=self.context.get("request").user.id
        )
        return super().create(validated_data)