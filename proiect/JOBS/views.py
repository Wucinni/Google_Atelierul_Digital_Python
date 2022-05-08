from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from JOBS.models import Jobs


class JOBSView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'JOBS/jobs_index.html'

class CreateJOBSView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'JOBS/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_jobs')


class UpdateJOBSView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'JOBS/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_jobs')

@login_required
def delete_JOBS(request, pk):
    Jobs.objects.filter(id=pk).update(activ=0)
    return redirect('jobs:lista_jobs')

@login_required
def activate_JOBS(request, pk):
    Jobs.objects.filter(id=pk).update(activ=1)
    return redirect('jobs:lista_jobs')