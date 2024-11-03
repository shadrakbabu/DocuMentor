from django.db import models
from django.contrib.auth.models import User  # For linking users with posts/comments

# Community Section Model
class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

# community comment model definition

class CommunityComment(models.Model):
    post = models.ForeignKey(CommunityPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment[:20]}"
    

# Resources Section Model

class Resource(models.Model):
    file_name = models.TextField(max_length=255)  # Ensure this field exists
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name





# Tutorials Section Model
class Tutorial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    video_link = models.URLField(max_length=200)  # Link to videos (YouTube, Vimeo, etc.)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
    

