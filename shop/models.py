from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# 1. 메인 배너 & 하단 배너 관리
class MainBanner(models.Model):
    LOCATION_CHOICES = [
        ('TOP', '최상단 메인 배너 (1920x576)'),
        ('BOTTOM', '최하단 배너 (1920x480)'),
        ('NEWHOT', 'NEW & HOT 메인 (572x336)'),
    ]
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='TOP')
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True, help_text="클릭 시 이동할 주소")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.get_location_display()}] {self.title}"

# 2. 카테고리 (Best Pick용)
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

# 3. 상품 (NEW & HOT, Best Pick 공통)
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField()
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    is_best_pick = models.BooleanField(default=False) # Best Pick 노출 여부
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 4. 리뷰 (Best 상품 후기용)
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author_name = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.author_name}"

# 5. 이벤트 페이지
class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/') # 576x400
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# 7. 인스타그램 설정 (관리자 1개 계정)
class InstagramSettings(models.Model):
    username = models.CharField(max_length=50, default='daniel4191', help_text="연동할 인스타그램 아이디")
    profile_url = models.URLField(blank=True, help_text="인스타그램 프로필 링크")

    def __str__(self):
        return f"Instagram: {self.username}"

# 인스타그램 게시글 (파싱한 데이터 저장용)
class InstagramPost(models.Model):
    image_url = models.URLField()
    link_url = models.URLField()
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']