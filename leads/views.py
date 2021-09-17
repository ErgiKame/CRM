from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

# CRUD+L - CREATE READ UPDATE DELETE LIST

class LandingPageView(TemplateView):
    template_name = "landing.html"



def landing_page(request):
    return render(request, "landing.html")

# CLASS BASED
class LeadListView(ListView):
    #Provide django the template name
    template_name = "leads/lead_list.html"
    #Provide django the queryset
    queryset = Lead.objects.all()

    #Just like the function based views but it automatically passes the context in return
    #Less code to write

    # KEEP IN MIND! queryset default key for context is object_list (replace on html mappings)
    # WE CAN CUSTOMIZE BY USING context_object_name
    context_object_name = "leads"

# FUNCTION BASED
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    # DOESN'T NEED QUERYSET. WE NEED TO PASS FORM CLASS
    form_class = LeadModelForm

    # After form completed successfully we
    def get_success_url(self):
        # Hard coded way
        return "/leads"
        # Best practise (dynamic)
        return reverse("leads:lead-list")


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    # NEEDS A QUERYSET AND FORM CLASS
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    # After form completed successfully we
    def get_success_url(self):
        # Hard coded way
    #    return "/leads"
        # Best practise (dynamic)
        return reverse("leads:lead-list")


def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        print('Receiving a post request')
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form" : form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)



class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    # NEEDS A QUERYSET ONLY
    queryset = Lead.objects.all()

    # NEED SUCCESS URL ALSO
    def get_success_url(self):
        return reverse("leads:lead-list")




def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form" : form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)


# def lead_create(request):
#     if request.method == "POST":
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(first_name=first_name,
#                                 last_name=last_name,
#                                 age=age,
#                                 agent=agent)
#             return redirect("/leads")
#     context = {
#         "form": LeadForm()
#     }
#     return render(request, "leads/lead_create.html", context)

