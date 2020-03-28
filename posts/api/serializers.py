from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # 只读字段

    class Meta:
        model = Post
        fields = ('title', 'content', 'is_featured', 'owner', 'date_created', 'date_modified',)
        read_only_fields = ('date_created', 'date_modified',)  # 只读字段
