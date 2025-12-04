from django.contrib import admin
from .models import MainBanner, Product, Review, Category, Event, InstagramSettings, InstagramPost

admin.site.register(MainBanner)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(InstagramSettings)
admin.site.register(InstagramPost)