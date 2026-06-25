from django.shortcuts import render, get_object_or_404, redirect
from .models import Announcement
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import AnnouncementForm

def announcement_list(request):
    announcements = Announcement.objects.filter(is_published=True)
    return render(request, "announcements/list.html", {"announcements": announcements})


def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk, is_published=True)
    return render(request, "announcements/detail.html", {"announcement": announcement})

@login_required
def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user  
            announcement.save()
            return redirect('announcements:detail', pk=announcement.pk)
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/form.html', {'form': form, 'title': 'Створити оголошення'})

@login_required
def announcement_edit(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    
    if announcement.author != request.user and not request.user.is_staff and not request.user.is_superuser:
        raise PermissionDenied  

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcements:detail', pk=announcement.pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/form.html', {'form': form, 'title': 'Редагувати оголошення'})

@login_required
def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if announcement.author != request.user and not request.user.is_staff and not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        announcement.delete()
        return redirect('announcements:list')
        
    return render(request, 'announcements/confirm_delete.html', {'announcement': announcement})