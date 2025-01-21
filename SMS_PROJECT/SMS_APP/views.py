from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import NewsPost,Announcement,Student

class NewsPostView(View):
    def get(self, request):
        posts = NewsPost.objects.all().order_by('-created_at')
        response = [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.name,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
            }
            for post in posts
        ]
        return JsonResponse(response, safe=False)

    @method_decorator(login_required)
    def post(self, request):
        data = request.POST
        author = get_object_or_404(Student, user=request.user)
        post = NewsPost.objects.create(
            author=author,
            title=data.get('title'),
            content=data.get('content'),
        )
        return JsonResponse({"message": "Post created", "post_id": post.id})


class AnnouncementView(View):
    def get(self, request):
        announcements = Announcement.objects.all().order_by('-created_at')
        response = [
            {
                "id": announcement.id,
                "title": announcement.title,
                "content": announcement.content,
                "author": announcement.author.username,
                "created_at": announcement.created_at,
                "notify_all": announcement.notify_all,
            }
            for announcement in announcements
        ]
        return JsonResponse(response, safe=False)

    @method_decorator(login_required)
    def post(self, request):
        if not request.user.is_staff:
            return JsonResponse({"error": "Unauthorized"}, status=403)

        data = request.POST
        announcement = Announcement.objects.create(
            author=request.user,
            title=data.get('title'),
            content=data.get('content'),
            notify_all=data.get('notify_all', False),
        )
        return JsonResponse({"message": "Announcement created", "announcement_id": announcement.id})
