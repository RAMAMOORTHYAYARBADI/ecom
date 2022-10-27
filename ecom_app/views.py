from rest_framework import generics,permissions,status,viewsets, parsers
from .serializers import *
from .models import *
from django.db.models.query_utils import Q
from  ecom_app.helpers.utils import Response, product_pagination, manage_sorting

class ManageProduct(viewsets.ViewSet):

    """
    Get all product  list API 
    """
    def get_all_product(self, request):
        try:
            query_set = ProductMstr.objects.filter(is_deleted = False).order_by('-created_on') 
            page =request.GET['page'] if 'page' in request.GET else 1 
            limit =request.GET['limit'] if 'limit' in request.GET else 12
            search_text =request.GET['search_text'] if 'search_text' in request.GET else ""
            product_category =request.GET['product_category'] if 'product_category' in request.GET else ""
            min_price =request.GET['min_price'] if 'min_price' in request.GET else ""
            max_price =request.GET['max_price'] if 'max_price' in request.GET else ""
            sort_type =request.GET['sort_type'] if 'sort_type' in request.GET else ""
            sort_value =request.GET['sort_value'] if 'sort_value' in request.GET else ""
            if search_text != None:
                query_set=query_set.filter(Q(product_name__icontains = search_text) | 
                                            Q(product_code__icontains = search_text) |
                                                Q(product_category__icontains = search_text))
            if product_category != "":
                product_category = product_category.split(",")
                query_set=query_set.filter(product_category__in = product_category)
            if  min_price != "" and max_price != "":
                query_set=query_set.filter(product_price__range=[min_price, max_price])
            if sort_type != "" and sort_value !="":
                query_set = manage_sorting(query_set,sort_type,sort_value) 
            #pagination calculation
            total_count=len(query_set)
            count_1 = total_count % 12
            count_2 = total_count // 12
            if  count_1 != 0:
                count_2 +=1

            #pagination
            offset = 0
            limit = int(limit)
            page_ = product_pagination(offset,limit,page)
            result = query_set[page_[0]:page_[1]]
            serializer = ProductMstrSerializer(result, many=True).data
            return Response(serializer, 200, True)
        except:
            return Response("Internal Server Error", 400, False)

