# Copyright 2010 Cristian Esquivias

# This file is part of django-memorize.

# django-memorize is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# django-memorize is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General Public License
# along with django-memorize.  If not, see <http://www.gnu.org/licenses/>.

from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
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
    practices = Practice.objects.filter(user=request.user).order_by('next_practice')
    if len(practices) == 0:
        return direct_to_template(request, template, {
                'errors': ['No items to practice']})
    practice = practices[0]
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

@login_required
def practice_list(request, template='memorize/practice_list.html',
                  paginate_by=None, page=None, allow_empty=True):
    practice_list = Practice.objects.filter(user=request.user)\
        .order_by('next_practice')

    if paginate_by:
        paginator = Paginator(practice_list, paginate_by,
                              allow_empty_first_page=allow_empty)
        if not page:
            page = request.GET.get('page', 1)
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                # Page is not 'last', nor can it be converted to an int.
                raise Http404
        try:
            page_obj = paginator.page(page_number)
        except InvalidPage:
            raise Http404

        return direct_to_template(request, template, {
                'paginator': paginator,
                'page_obj': page_obj,})

    return direct_to_template(request, template, {
            'practice_list': practice_list})

@login_required
def add_to_practice(request, object_id=None, slug=None, slug_field=None,
                    model=None, post_save_redirect=None):
    if object_id:
        obj = get_object_or_404(model, pk=int(object_id))
    elif slug and slug_field:
        obj = get_object_or_404(model, **{slug_field: slug})
    else:
        return HttpResponseBadRequest()

    practice = Practice(item=obj, user=request.user).save()
    if post_save_redirect:
        return HttpResponseRedirect(post_save_redirect)
    else:
        return HttpResponseRedirect(reverse('memorize.views.practice_list'))
