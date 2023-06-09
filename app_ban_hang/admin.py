from django.contrib import admin
from .models import *
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

class SanPhamAdmin(admin.ModelAdmin):
    list_display = ['LoaiSP', 'TenSP', 'GiaSP', 'LuotMua', 'TonKho', 'DanhGia']
    list_filter = ['TonKho']
    search_fields = ['TenSP']
    inlines = [CommentInline]

admin.site.register(Base)
admin.site.register(SanPham)
admin.site.register(Blog)
admin.site.register(LoaiSP)
admin.site.register(DonHang)
admin.site.register(OrderItem)
admin.site.register(ThongTinNguoiMua)
admin.site.register(LienHe)
admin.site.register(TuVanNoiThat)

admin.site.register(Carousel_Home)
admin.site.register(Home)



###################################################################################################