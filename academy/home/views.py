from django.shortcuts import render
from . models import Course, Blog, Testimonial, Gallery, Slider
# Create your views here.

def index(request):
    course = Course.objects.all()
    gallery = Gallery.objects.all()
    testi = Testimonial.objects.all()
    blog = Blog.objects.all()
    slider = Slider.objects.all()
    return render(request, 'index.html', {'course': course, 'gallery': gallery, 'testi': testi, 'blog': blog, 'slider': slider})