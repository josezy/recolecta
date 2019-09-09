from django.views import View
from django.shortcuts import render

from hoarding.forms import ItemForm


class BaseView(View):
    def render_template(self, request, context=None, template=None):
        return render(request, template or self.template, {**(context or {})})


class Home(BaseView):
    template = 'core/home.html'

    def get(self, request):
        context = {
            'form': ItemForm()
        }
        return self.render_template(request, context=context)
