from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from users.forms import CommentForm, PostForm, UpdateForm, CatForm
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-date_posted')
        context = {'posts': posts}
        return render(request, 'blogapp/home.html', context)


class AboutView(View):
    def get(self, request):
        context = {'title': 'about'}
        return render(request, 'blogapp/about.html', context)


class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {'post': post}
        return render(request, 'blogapp/post_detail.html', context)


class NewPostView(LoginRequiredMixin, View):
    def get(self, request):
        new_post_form = PostForm()
        return render(request, 'blogapp/post_create.html', {'new_post_form': new_post_form})

    def post(self, request):
        new_post_form = PostForm(
            request.POST, request.FILES)
        new_post_form.instance.author = self.request.user
        if new_post_form.is_valid():
            new_post_form.save()
            return redirect('blog-home')


class UpdatePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post_update_form = UpdateForm(use_required_attribute=False,
                                      instance=Post.objects.get(id=pk))  # get former knowledge of the post
        return render(request, 'blogapp/post_update.html', {'post_update_form': post_update_form})

    def post(self, request, pk):
        post_update_form = UpdateForm(
            request.POST, request.FILES, use_required_attribute=False, instance=Post.objects.get(id=pk))
        if post_update_form.is_valid():
            post_update_form.save()
            return redirect(reverse('post-detail', kwargs={'pk': pk}))


class DeletePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        deleted_post = get_object_or_404(Post, id=pk)
        context = {'deleted_post': deleted_post}
        return render(request, 'blogapp/post_delete.html', context)

    def post(self, request, pk):
        deleted_post = get_object_or_404(Post, id=pk)
        if deleted_post.author != request.user:
            return False
        deleted_post.delete()
        return redirect('blog-home')


class AddCommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment_form = CommentForm()
        post = get_object_or_404(Post, id=pk)
        return render(request, 'blogapp/add_comment.html', {'post': post,
                                                            'comment_form': comment_form})

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        comment_form = CommentForm(data=request.POST)
        new_comment = None
        if comment_form.is_valid():
            new_comment = comment_form.save()
            new_comment.post = post
            new_comment.save()
        return redirect('.')


class AddCategoryView(LoginRequiredMixin, View):
    def get(self, request):
        new_category_form = CatForm(use_required_attribute=False)
        context = {'new_category_form': new_category_form}
        return render(request, 'blogapp/add_category.html', context)

    def post(self, request):
        new_category_form = CatForm(request.POST)
        if new_category_form.is_valid():
            new_category_form.save()
            return redirect('blog-home')
        return render(request, 'blogapp/add_category.html', {'new_category_form': new_category_form})


class CategoryListView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'blogapp/categories.html', context)

    def post(self, request):
        categories = Category.objects.all()
        category = Category.objects.create(
            name=request.POST.get('name')
        )
        category.save()
        return render(request, 'blogapp/categories.html', {'categories': categories})


class CategoryView(View):
    def get(self, request, pk):
        required_posts = Post.objects.filter(category_id=pk)
        context = {'required_posts': required_posts}
        return render(request, 'blogapp/each_category.html', context)

