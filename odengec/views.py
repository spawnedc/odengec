from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Payment
from .forms import PaymentForm


class PublicBaseView(View):
    """ A base class for all views """

    class Meta:
        abstract = True

    def get_context_data(self, *args, **kwargs):
        context = super(PublicBaseView, self).get_context_data(*args, **kwargs)

        context['section'] = self.section_name or ''

        return context


class PublicBasicPageView(PublicBaseView, TemplateView):
    """ Basic page view """
    pass


class PublicDetailView(PublicBaseView, DetailView):
    """ Basic detail page view """
    pass


class PublicListView(PublicBaseView, ListView):
    """ Basic list view """
    pass


class PublicCreateView(PublicBaseView, CreateView):
    """ Basic create view """
    pass


class PublicUpdateView(PublicBaseView, UpdateView):
    """ Basic update view """
    pass


class Dashboard(PublicBasicPageView):

    template_name = 'dashboard.html'
    section_name = 'dashboard'

    def get_context_data(self):
        context = super(Dashboard, self).get_context_data()

        context['payments'] = Payment.objects.all().order_by('-start_date')

        return context

dashboard = Dashboard.as_view()


class CreatePayment(PublicCreateView):

    form_class = PaymentForm

    template_name = 'create_payment.html'
    section_name = 'create_payment'

    success_url = '/'

create_payment = CreatePayment.as_view()


class EditPayment(PublicUpdateView):

    model = Payment
    form_class = PaymentForm
    template_name = 'create_payment.html'
    section_name = 'create_payment'
    success_url = '/'

edit_payment = EditPayment.as_view()
