from django.shortcuts import render
from .models import MainBanner, Product, Review, Category, Event, InstagramSettings, InstagramPost
from django.db.models import Count

def main_view(request):
    # 1. 메인 배너
    # top_banner = MainBanner.objects.filter(location='TOP', is_active=True).last()
    top_banners = MainBanner.objects.filter(location="TOP", is_active=True).order_by('-id')
    
    # 3. NEW & HOT
    new_hot_banner = MainBanner.objects.filter(location='NEWHOT', is_active=True).last()
    new_hot_products = Product.objects.filter(is_hot=True).order_by('-created_at')[:4] # 최대 4개
    
    # 4. 베스트 후기 (최신순 3개)
    best_reviews = Review.objects.all().order_by('-created_at')[:3]
    
    # 5. Best Pick (카테고리 & 인기순 상품)
    categories = Category.objects.all()[:6] # 최대 6개
    # 댓글 많은 순으로 정렬하여 최대 5개 가져오기
    best_pick_products = Product.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:5]

    # 5(6). 이벤트 (최대 2개)
    events = Event.objects.filter(is_active=True).order_by('-start_date')[:2]

    # 7. 인스타그램 (계정정보 & 게시글 3개)
    insta_settings = InstagramSettings.objects.first()
    insta_posts = InstagramPost.objects.all()[:3]

    # 8. 하단 배너
    bottom_banner = MainBanner.objects.filter(location='BOTTOM', is_active=True).last()

    context = {
        'top_banners': top_banners,
        'new_hot_banner': new_hot_banner,
        'new_hot_products': new_hot_products,
        'best_reviews': best_reviews,
        'categories': categories,
        'best_pick_products': best_pick_products,
        'events': events,
        'insta_settings': insta_settings,
        'insta_posts': insta_posts,
        'bottom_banner': bottom_banner,
    }
    return render(request, 'shop/main.html', context)