from django.contrib import admin

# Register your models here.
from home.models import Gallery, Course, Blog, Testimonial, Slider

admin.site.register(Gallery)
admin.site.register(Course)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Slider)