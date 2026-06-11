from django.shortcuts import render, get_object_or_404
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.filter(is_published=True)
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk, is_published=True)
    return render(request, 'announcements/detail.html', {'announcement': announcement})