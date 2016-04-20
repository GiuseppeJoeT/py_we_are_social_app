import arrow
from django import template
from django.core.urlresolvers import reverse

# Arrow package: better dates and times for Python

register = template.Library()  # ???


@register.filter
def get_total_subject_posts(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
    return total_posts


@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('-created_at')
    return posts.first().user.username

