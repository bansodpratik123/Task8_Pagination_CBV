from django.shortcuts import render
from django.views.generic import ListView

from .models import Laptops
# Create your views here.


def homepage(request):
    return render(request,'Homepage.html',{})

class ShowLaptops(ListView):
    queryset = Laptops.objects.all()
    template_name = 'Laptops_list.html'
    paginate_by = 3




























# from django.shortcuts import render
# from .models import Laptops
#
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
# # Create your views here.
# def homepage(request):
#     return render(request,'Homepage.html',{})
#
# def showlaptops(request):
#     records=Laptops.objects.all()
#     paginate=Paginator(records,3)
#     page_show=request.GET.get('page')
#
#     try:
#         rec = paginate.page(page_show)
#     except PageNotAnInteger:
#         rec = paginate.page(1)
#     except EmptyPage:
#         rec = paginate.page(paginate.num_pages)
#
#     # return render(request, 'studentpages/show.html', {'posts': posts})
#     return render(request,'Laptops_list.html',{'rec':rec})


