from django.shortcuts import render
from notification.models import Notification


def notification_view(request):
    notifications = Notification.objects.filter(receiver=request.user)
    notifications_count = 0
    new_notifications = []
    for notify in notifications:
        if notify.notification_flag == False:
            notifications_count += 1
            new_notifications.append(notify.message_content)
            notify.notify_flag = True
            notify.save()
    return render(request, 'notification_detail.html', {
        "new_notifications": new_notifications,
        "notifications_count": notifications_count})
