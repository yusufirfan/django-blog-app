from rest_framework import serializers

class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)
    
from .models import Category, Post, Comment, Like
    
class CategorySerializer(FixSerializer):
    category_total = serializers.SerializerMethodField()

    def get_category_total(self, obj):
        return Category.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Category
        exclude = []

class PostSerializer(FixSerializer):
    category = serializers.StringRelatedField()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    like_total = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return Like.objects.filter(id=obj.id)
    
    def get_comments(self, obj):
        return Comment.objects.filter(id=obj.id)

    def get_like_total(self, obj):
        return Like.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Category
        exclude = []

class CommentSerializer(FixSerializer):
    
    class Meta:
        model = Comment
        exclude = []

class LikeSerializer(FixSerializer):
    
    class Meta:
        model = Like
        exclude = []