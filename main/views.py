from django.shortcuts import render
from django.contrib import messages
from .models import (
		ContactInfo,
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
		Skill
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.FormView):
	template_name = "main/index.html"
	form_class = ContactForm
	# //! if  for is vaild the user is redirected to 
	success_url = "/"

	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		skills = Skill.objects.filter(is_key_skill=False)
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		keyskills= Skill.objects.filter(is_key_skill=True)
  
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		context["skill"] = skills
		context["keyskills"] = keyskills
  
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
 # //! if  for is vaild the user is redirected to 
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

 
class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"
 
 
 
 
def list_view(request):
	skills = Skill.objects.filter(is_key_skill=False)
	testimonials = Testimonial.objects.filter(is_active=True)
	certificates = Certificate.objects.filter(is_active=True)
	contactinfo = ContactInfo.objects.all()
	blogs = Blog.objects.filter(is_active=True)
	portfolio = Portfolio.objects.filter(is_active=True)
	keyskills= Skill.objects.filter(is_key_skill=True)


  
	if request.method == "POST":
		contactform = ContactForm(data=request.POST)
		if contactform.is_valid():
			contactform.save()
	else:
		contactform = ContactForm()

	context={	
	'skill':skills,
	'testimonials':testimonials,
	'keyskills':keyskills,
	'form':contactform,
	'contactinfo':contactinfo
	}
	print(contactinfo)
	print(skills)
	return render(request, "main/index.html", context)

 