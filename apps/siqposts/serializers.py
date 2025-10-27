from rest_framework import serializers
from .models import CivicPost, Comment, Poll, PollOption

# 💬 Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'likes']

# 📝 CivicPost Serializer
class CivicPostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = CivicPost
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'likes', 'views', 'shares']

# 📊 Poll Option Serializer
class PollOptionSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()

    class Meta:
        model = PollOption
        fields = ['id', 'text', 'vote_count']

    def get_vote_count(self, obj):
        return obj.votes.count()

# 📊 Poll Serializer
class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'question', 'created_at', 'options']
