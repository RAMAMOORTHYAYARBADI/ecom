from django.shortcuts import HttpResponse
import json, codecs


def Response(data,http_code, error=True, json_format=True):
    if error:
        status = True
        response = {
            "data": data,
            "status": status,
            "http_code": http_code
        }
        # http_code=200
    else:
        status = False
        # http_code=404
        response = {
            "data": data,
            "status": status,
            "http_code":http_code
        }
    if json_format:
        response = json.dumps(response)

    return HttpResponse(response, content_type='Application/json', status=int(http_code))

def product_pagination(offset,limit,page):
    if page == 1:
        offset = offset
        limit = limit
    if page !=1:
        offset = (int(page) -1) * int(limit)
        limit = (int(limit) * int(page))
    
    return offset,limit

def manage_sorting(query_set=None,sort_type=None,sort_value=None):
    sort_value = '-' + sort_value if sort_type == "desc" else sort_value
    query_set = query_set.order_by(sort_value)
    return query_set