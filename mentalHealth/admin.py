from django.contrib import admin
from .models import LifestyleData

admin.site.register(LifestyleData)


from .models import Sentiment

admin.site.register(Sentiment)
