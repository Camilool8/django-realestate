from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Property, Testimonial, TeamMember, Partner

def home(request):
    properties = Property.objects.all()
    testimonials = Testimonial.objects.all()
    team_members = TeamMember.objects.all()
    partners = Partner.objects.all()

    context = {
        'properties': properties,
        'testimonials': testimonials,
        'team_members': team_members,
        'partners': partners,
    }

    return render(request, 'home.html', context)

class PropertyDetailView(DetailView):
    model = Property
    template_name = "property_detail.html"
    context_object_name = "property"