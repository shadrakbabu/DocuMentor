from django import forms
from .models import CommunityPost, CommunityComment,Resource
from .models import Tutorial

# Form for creating a community post
class PostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['heading', 'community','content']
        widgets = {
            'heading': forms.TextInput(attrs={'placeholder': 'Enter topic of the post'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter your comment...', 'rows': 4}),
            'community': forms.TextInput(attrs={'placeholder': 'Enter community name'}),
        }


  # Ensure these fields exist in the model


from django import forms
from .models import CommunityPost, CommunityComment, Resource, Tutorial


# Form for uploading a document link




# Form for uploading a document link
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['file_name', 'link']
        widgets = {
            'file_name': forms.TextInput(attrs={'placeholder': 'Enter file name'}),
            'link': forms.URLInput(attrs={'placeholder': 'Enter link to document'}),
        }

# Form for referring a video
class VideoForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['topic', 'video_link']
        widgets = {
            'topic': forms.TextInput(attrs={'placeholder': 'Enter topic of the video'}),
            'video_link': forms.URLInput(attrs={'placeholder': 'Enter video link'}),
        }
