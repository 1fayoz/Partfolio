from django.shortcuts import render
from.models import Profile,Skils,About,Servies,Project,Catigory,Blog,Tool
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    profile = Profile.objects.last()
    skils = Skils.objects.order_by('order')
    about = About.objects.first()
    servies = Servies.objects.all()
    catigory = Catigory.objects.all()
    project = Project.objects.all()
    blog = Blog.objects.all()

    P = Paginator(blog, 6)
    page_number = request.GET.get('page')
    try:
        page_object = P.get_page(page_number)
    except PageNotAnInteger :
        page_object = P.page(1)
    except EmptyPage:
        page_object = P.page(P.num_pages)

    return render(request, 'index.html',
                   {'profile': profile, 
                    'skills': skils, 
                    'about': about, 
                    'servies': servies,
                    'project':project, 
                    'catigory':catigory, 
                    'blog':page_object }

                   )


def project_detail(request, pk):
    project_s = get_object_or_404(Project, id=pk)
    tool = Tool.objects.all()
    return render(request, 'portfolio-details.html', {'project_s': project_s, 'tool': tool})

def SingleBlog(request, pk):
    blogs = get_object_or_404(Blog, id=pk)
    url = reverse('blog', kwargs={'pk': 1})
    blogs.view += 1
    blogs.save()

    return render(request, 'single-blog.html', {'blogs': blogs})

def AboutUs(request, ):
    about = get_object_or_404(About)
    servis = Servies.objects.all()
    skill = Skils.objects.all()
    return render (request, 'about-us.html', {'about': about, 'servis':servis,'skill':skill } )


def Posrtfolio(request):
    portfoly = Project.objects.all()
    catigory = Catigory.objects.all()
    return render(request, 'portfolio.html', { 'portfoly':portfoly, 'catigory':catigory } )

# def Blog_detail(request, pk):
#     blogs = get_object_or_404(Blog, id=pk)
#     url = reverse('blog', kwargs={'pk': 1})
#     blogs.view += 1
#     blogs.save()
#     return render(request, 'blog.html', {'blogs': blogs})

def BlogPath(request):
    blog = Blog.objects.all() 
    profile = Profile.objects.last()
    blogs = Blog.objects.order_by('-view')

    if request.method == 'POST':
        search = request.POST.get('search')
        blogs = Blog.objects.filter(title__icontains = search)

    P = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    try:
        page_objects = P.get_page(page_number)
    except PageNotAnInteger :
        page_objects = P.page(1)
    except EmptyPage:
        page_objects = P.page(P.num_pages) 


    # ------------------------------This is for searching --------------------------------------------
    if request.method == 'POST':
        search = request.POST.get('search')
        blog = Blog.objects.filter(title__icontains = search)
    

    P = Paginator(blog, 2)
    page_number = request.GET.get('page')
    try:
        page_object = P.get_page(page_number)
    except PageNotAnInteger :
        page_object = P.page(1)
    except EmptyPage:
        page_object = P.page(P.num_pages) 


    return render(request, 'blog.html', { 'blog': page_object , 'blogs': page_objects, 'profile': profile} )


