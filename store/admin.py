from django.contrib import admin
from django.utils.html import format_html
from .models import Property, Testimonial, TeamMember, Partner

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'formatted_price', 'property_type')
    list_filter = ('property_type', 'location', 'is_featured')
    search_fields = ('name', 'location')
    ordering = ['-price']

    def formatted_price(self, obj):
        return format_html("{} {}", obj.price.amount, obj.price.currency)

    formatted_price.short_description = 'Price'

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    search_fields = ('name',)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

admin.site.register(Property, PropertyAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Partner, PartnerAdmin)
