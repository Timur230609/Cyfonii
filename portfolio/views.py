from django.shortcuts import render


def contact_view(request):
 return render(request,'contact.html')

def index_view(request):
 return render(request,'index.html')

def carousel_view(request):
 return render(request,'33dcarousel.html')

def about_view(request):
 return render(request,'about.html')

def advisor_view(request):
 return render(request,'advisor.html')

def author02_view(request):
 return render(request,'author02.html')

def blogdetail_view(request):
 return render(request,'blog-detal.html')

def blog_view(request):
 return render(request,'blog.html')

def cardcarousel_view(request):
 return render(request,'cardcarousel.html')

def coverflowcarousel_view(request):
 return render(request,'cowerflowcarousel.html')

def helpcenter_view(request):
 return render(request,'help-server.html')

# def homev2_view(request):
#  return render(request,'home-v2.html')

# def homev3_view(request):
#  return render(request,'home-v3.html')

def trid_view(request):
 return render(request,'3dcarousel.html')

def iteamcarousel_view(request):
 return render(request,'iteamcarousel.html')

def nft_view(request):
 return render(request,'nft.html')

def partiasset_view(request):
 return render(request,'parti-asset.html')

def partner_view(request):
 return render(request,'partner.html')

def roadmap_view(request):
 return render(request,'roadmap.html')

def team_view(request):
 return render(request,'team.html')

def visionmission_view(request):
 return render(request,'vision-mission.html')

def zigzagcarousel_view(request):
 return render(request,'zigzagcarousel.html')







def project_list(request):
    projects = [
        {"id": 1, "title": "3D Digital Artwork", "image": "/assets/images/layouts/project-01.png"},
        {"id": 2, "title": "King Of Pirates", "image": "/assets/images/layouts/project-02.png"},
    ]
    return render(request, 'project.html', {"projects": projects})
