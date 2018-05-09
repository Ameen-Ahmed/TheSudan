from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'newsfeed/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post.published, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'newsfeed/post/detail.html', {'post': post})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        # Retrieve form data, storing it in the variable form
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            # Create a dictionary of all the form attributes that are valid (should be all of them now)
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@mynewsfeed.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'newsfeed/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


def post_comment(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        # Form was submitted
        # Retrieve form data, storing it in the variable form
        form = CommentForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            # Create a dictionary of all the form attributes that are valid (should be all of them now)
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@mynewsfeed.com', [cd['to']])
            sent = True
    else:
        form = CommentForm()
    return render(request, 'newsfeed/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
