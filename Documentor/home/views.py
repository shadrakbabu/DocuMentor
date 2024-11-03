
# importing section starts
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages # type: ignore
from .models import CommunityPost, Resource, Tutorial

from .forms import CommunityPost, Resource, Tutorial
from .forms import PostForm   # Import PostForm
from .forms import DocumentForm
from .forms import VideoForm  # Make sure to import the VideoForm here

from .models import Tutorial
from .models import CommunityComment

from django.shortcuts import render, get_object_or_404


# importing section ends

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or another page after saving
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import PostForm, DocumentForm  # Ensure DocumentForm is included


# Create your views here.

def landingpage(request):
    return render(request, 'landingpage.html')

def login(request):
    return render(request,'login.html')

def temp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect')
                return redirect('login')
        else:
            messages.error(request, 'Username and password are required')
            return redirect('login')
    else:
        return redirect('login')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def Signup(request):
    return render(request,'Signup.html')

def pemp1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            return redirect('Signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used')
            return redirect('Signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('home')
    else:
        return redirect('Signup')
    
def home(request):
    return render(request, 'base.html', )

def recommendations(request):
    return render(request, 'recommendations.html')

def resources(request):
    return render(request, 'resources.html')

def log(request):
    return render(request, 'log.html')

def file1(request):
    return render(request, 'file1.html')

def ask(request):
    return render(request, 'ask.html')

def upload(request):
    return render(request, 'upload.html')

def newvideo(request):
    return render(request, 'newvideo.html')

def comment(request):
    return render(request, 'comment.html')







# View for Community Section
def community_view(request):
    posts = CommunityPost.objects.all().order_by('-timestamp')  # Get posts ordered by newest first
    return render(request, 'community.html', {'posts': posts})

# View for Resources Section
def resources_view(request):
    resources = Resource.objects.all().order_by('-timestamp')
    return render(request, 'resources.html', {'resources': resources})

# View for Tutorials Section
def tutorials_view(request):
    tutorials = Tutorial.objects.all().order_by('-timestamp')
    return render(request, 'tutorials.html', {'tutorials': tutorials})


# forms code for creating data 


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Ensure the user is set to the current logged-in user
            post.save()
            return redirect('community')  # Redirect after saving
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


# resources
def resources_view(request):
    resources = Resource.objects.all()  # Fetch all resources
    return render(request, 'resources.html', {'resources': resources})


# View for uploading a document
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.user = request.user  # Set the user to the current logged-in user
            resource.save()
            return redirect('resources')  # Adjust the redirect as necessary
    else:
        form = DocumentForm()

    return render(request, 'upload_document.html', {'form': form})


# video referring
def refer_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # If you have a user field
            video.save()
            return redirect('tutorials')  # Replace with your desired redirect
    else:
        form = VideoForm()
    return render(request, 'refer_video.html', {'form': form})

def list_tutorials(request):
    tutorials = Tutorial.objects.all()  # Fetch all tutorial objects
    return render(request, 'tutorials.html', {'tutorials': tutorials})



# views.py


from django.contrib.auth.decorators import login_required


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(CommunityPost, id=post_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            CommunityComment.objects.create(
                post=post,
                user=request.user,
                comment=content
            )
            return redirect('community_detail', post_id=post.id)
    
    return HttpResponse('Invalid request', status=400)



# community view function

from django.shortcuts import render
from .models import CommunityPost

def community_view(request):
    posts = CommunityPost.objects.prefetch_related('comments').all()  # Correct related name
    return render(request, 'community.html', {'posts': posts})


# file view or plus button page

def file1_view(request):
    # Your logic for handling the request
    return render(request, 'file1.html')
 # Make sure the template exists


from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


# search working

from django.http import JsonResponse
from .models import CommunityPost, Resource, Tutorial

def search(request):
    query = request.GET.get('q', '')
    community_posts = CommunityPost.objects.filter(heading__icontains=query)
    resources = Resource.objects.filter(file_name__icontains=query)  # Updated to file_name
    tutorials = Tutorial.objects.filter(topic__icontains=query)  # Assuming Tutorial has a title field

    data = {
        'community_posts': list(community_posts.values('id', 'heading')),
        'resources': list(resources.values('id', 'file_name')),  # Update to file_name
        'tutorials': list(tutorials.values('id', 'topic')),  # Ensure this is correct
    }

    return JsonResponse(data)



# Resource detail view
def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return render(request, 'resource_detail.html', {'resource': resource})

# Tutorial detail view
def tutorial_detail(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    return render(request, 'tutorial_detail.html', {'tutorial': tutorial})



def community_detail(request, post_id):
    post = get_object_or_404(CommunityPost, id=post_id)
    comments = post.comments.all()
    return render(request, 'community_detail.html', {'post': post, 'comments': comments})

# terms and conditions

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')
