from django.contrib import admin
from .models import Item, Article, Category, Order
# Register your models here.

class ItemsInstanceInline(admin.TabularInline):
    model = Item


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'items',)
    list_display = ('title', 'text', 'get_items')

    def get_items(self, obj):
        return " ; ".join([i.title for i in obj.items.all()])


class ItemAdmin(admin.ModelAdmin):
    fields = (('title', 'cathegory'), 'text', 'photo',)
    list_display = ('title', 'text', 'get_article', 'get_reviews_count', 'cathegory')

    def get_article(self, obj):
        return " ; ".join([i.title for i in obj.articles.all()])

    def get_reviews_count(self, obj):
        return obj.reviews.count()

    get_reviews_count.short_description = 'Колличество отзывов'
    get_article.short_description = 'Статья'


class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', ('is_main', 'main_category'))
    list_display = ('title', 'is_main', 'main_category', 'get_items')
    inlines = [ItemsInstanceInline]

    def get_items(self, obj):
        return ' ; '.join([i.title for i in obj.items.all()])

    get_items.short_description = 'Товары'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'get_items_count', 'get_items')

    def get_items_count(self, obj):
        return obj.items.count()

    def get_items(self, obj):
        return ' ; '.join([i.title for i in obj.items.all()])

    get_items.short_description = 'Товары'
    get_items_count.short_description = 'Колличество товаров'


admin.site.register(Item, ItemAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)