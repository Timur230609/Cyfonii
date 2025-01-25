from django.shortcuts import render
from .models import Contact ,Blog,Team
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Form uchun class
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=50, required=True, label="Name")
#     email = forms.EmailField(required=True, label="Email") 
#     phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
#     message = forms.CharField(widget=forms.Textarea, required=True, label="Message")
def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_contact = Contact(name=name, email=email, content=content)
            new_contact.save()
            messages.success(request, "Your message successfully sent!")
            return HttpResponseRedirect(reverse('home-page'))
        except:
            pass

    return render(request, 'contact.html')


# # Contact sahifasi uchun view
# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Validatsiya muvaffaqiyatli bo'lsa
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone_number = form.cleaned_data['phone_number']
#             message = form.cleaned_data['message']

#             # Xabar yuborish (send_mail uchun konfiguratsiya kerak)
#             send_mail(
#                 f"New Contact Form Submission from {name}",
#                 message,
#                 email,
#                 ['your_email@example.com'],  # O'zingizning emailingizni kiriting
#             )
#             return JsonResponse({'status': 'success', 'message': 'Thank you for your message!'})
#         else:
#             return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
#     else:
#         form = ContactForm()
#     return render(request, "contact.html", {'form': form})

def index_view(request):
 return render(request,'index.html')

def about_view(request):
 return render(request,'about.html')

def blogdetail_view(request):
 return render(request,'blog-details.html')

def blog_view(request):
 return render(request,'blog.html')

def team_view(request):
 return render(request,'team.html')

def nft_view(request):
 return render(request,'nft.html')




class BlogDetailView(HitCountDetailView):
    model = Blog       
    count_hit = True   
    context_object_name = 'blog'
    template_name = 'publication.html'
    slug_field = 'slug'
    

