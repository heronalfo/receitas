from django.core.paginator import Paginator
import math

def make_pagination_range(page_range, current_page, segment_size=4):

    total_pages = len(page_range)
    middle_page = current_page
    segment_start = max(1, middle_page - segment_size // 2)
    
    segment_end = min(total_pages + 1, segment_start + segment_size)
    
    pagination = page_range[segment_start - 1:segment_end - 1]

    return {
    
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': total_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'segment_start': segment_start,
        'segment_end': segment_end,
        'first_page_out_of_range': segment_start > 1,
        'last_page_out_of_range': segment_end < total_pages + 1,
        
    }
    
def make_pagination(request, query_set, perpage, qty_pages):
    
    try:
    
        current_page = int(request.GET.get('page', 1))
    
    except ValueError:
        
        current_page = 1
    
    paginator = Paginator(query_set, perpage)
    page_obj = paginator.get_page(current_page)
    
    pages = make_pagination_range(
        page_range=paginator.page_range,
        segment_size = 4,
        current_page=current_page
            
    )
    
    return page_obj, pages