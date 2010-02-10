from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from forms import RatingsForm
from models import Practice

def post_required(view):
    @wraps(view)
    def view_wrapper(request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponseNotAllowed(['POST'])
        return view(request, *args, **kwargs)
    return view_wrapper

@login_required
def next_practice_item(request, template):
    practice = Practice.objects.filter(user=request.user).order_by('next_practice')[0]
    form = RatingsForm(initial={"id": practice.id})
    item = practice.item
    return direct_to_template(request, template, {
            'practice': practice, 'item': item, 'form': form})

@post_required
@login_required
def process_rating(request, post_save_redirect):
    form = RatingsForm(request.POST)
    if form.is_valid():
        practice_item = get_object_or_404(Practice,
                                          pk=int(form.cleaned_data['id']))
        practice_item.set_next_practice(int(form.cleaned_data['rating']))
        practice_item.save()
        return HttpResponseRedirect(post_save_redirect)

@post_required
@login_required
def skip_practice(request, practice_id, redirect):
    practice = Practice.objects.get(pk=int(practice_id))
    practice.delay()
    practice.save()
    return HttpResponseRedirect(reverse(redirect))
