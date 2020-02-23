from typing import Any, Dict

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from hoarding.forms import ItemForm


class BaseView(View):
    def render_template(self, request, context=None, template=None):
        return render(request, template or self.template, {**(context or {})})

    def render_json(self, json_dict: Dict[str, Any], **kwargs):
        return JsonResponse(json_dict, **kwargs)


class Home(BaseView):
    template = 'core/home.html'

    def get(self, request):
        context = {
            'form': ItemForm()
        }
        return self.render_template(request, context=context)

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect home with a success banner
            # send email with item overview link (add small link to request cancellation)
            return self.render_json({'success': True})
        return self.render_json({'success': False})
