from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Car
from .forms import (
    CarCreateForm,
    CarUpdateForm,
)


def index(request):
    return render(request, "index.html")


class CarList(LoginRequiredMixin, generic.ListView):

    model = Car
    paginate_by = 10

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CarList, self).get_context_data(**kwargs)
        context["title"] = "Lista samochodów"
        return context


class CarDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):

    model = Car

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner

    def get_context_data(self, **kwargs):
        context = super(CarDetail, self).get_context_data(**kwargs)
        context["title"] = "Informacje o samochodzie"
        return context


class CarCreate(LoginRequiredMixin, generic.edit.CreateView):

    model = Car
    form_class = CarCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CarCreate, self).get_context_data(**kwargs)
        context["title"] = "Dodaj nowy samochód"
        return context


class CarUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):

    model = Car
    form_class = CarUpdateForm

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CarUpdate, self).get_context_data(**kwargs)
        context["title"] = "Zmień dane"
        return context


class CarDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):

    model = Car
    success_url = "/breeding/cars"

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner

    def get_context_data(self, **kwargs):
        context = super(CarDelete, self).get_context_data(**kwargs)
        context["title"] = "Usuń samochód"
        return context
