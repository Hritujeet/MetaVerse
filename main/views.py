from django.shortcuts import render, redirect, HttpResponse
from .models import Post, Comment
from django.contrib import messages


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Create your views here.
def homeFeed(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        allPosts = Post.objects.order_by('-id')

        params = {'posts': allPosts}
    return render(request, 'main/homeFeed.html', params)


def createPost(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        print(request.FILES)

        file_objs = request.FILES.getlist('uploadImage')
        for file_obj in file_objs:
            print(file_obj)

        if allowed_file(file_obj) != None:
            newPost = Post(content=content, user=request.user, img=file_obj, likes=0, views=0)
            newPost.save()
            messages.add_message(request, messages.SUCCESS, 'Post has been created Successfully')
            return redirect('feed')

    return render(request, 'main/createPost.html')


def yourAccount(request):
    posts = Post.objects.filter(user=request.user)

    params = {'posts': posts}
    return render(request, 'main/yourAccount.html', params)


def like(request):
    if request.method == "POST":
        id = request.POST.get('like')

        post = Post.objects.filter(id=id).first()
        post.likes = post.likes + 1
        print(post.likes)

        post.save()

        messages.add_message(request, messages.SUCCESS, 'Post has been liked succesfully')
        return redirect('feed')
    return HttpResponse("This is like page")


def viewPost(request, slug):
    if request.method == 'POST':
        content = request.POST.get('comment')
        id = request.POST.get('post')

        post = Post.objects.filter(id=id).first()

        comment = Comment(user=request.user, post=post, content=content)
        comment.save()
        messages.add_message(request, messages.SUCCESS, 'Comment has been posted succesfully')

    post = Post.objects.filter(id=slug).first()
    allComments = Comment.objects.filter(post=post)

    params = {'p': post, 'allComments': allComments}

    post.views = post.views + 1
    post.save()
    return render(request, 'main/post.html', params)
