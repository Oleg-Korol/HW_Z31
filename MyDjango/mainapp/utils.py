"""""Этот модуль нужен для вспогательных функций"""
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

def get_current_group(request):
    """"
    Returns currently selected group or None
    :param request:Object request
    """
    from .models import Stock

    pk = request.COOKIES.get('current_group')

    if pk:
        try:
            group = Stock.objects.get(pk=int(pk))                #!

        except Stock.DoesNotExist:
            return None

        return group



def paginate(obj:object,
             size:int,
             request:object,
             context:dict,
             var_name = 'object_list'):
    """"Paginate objects provaided by view"""

    paginator = Paginator(obj,size)
    page = request.GET.get('page','1')

    try:
        object_list = paginator.page(page)

    except PageNotAnInteger:
        object_list =  paginator.page(1)
    except EmptyPage:
        object_list =paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context
