from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('username', 'start_year', 'revenue', 'founder', 'investment_round')
    search_fields = ('username__username', 'start_year', 'founder', 'investment_round')
    list_filter = ('start_year', 'investment_round')

admin.site.register(Company, CompanyAdmin)



from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'from_user', 'message', 'created_at')
    search_fields = ('to_user__username', 'from_user__username', 'message')
    list_filter = ('created_at',)

admin.site.register(Message, MessageAdmin)
