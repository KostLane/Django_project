from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    items = models.ManyToManyField('Item', related_name='articles', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['id']


class Item(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='shop/photos')
    cathegory = models.ForeignKey('Category', related_name='items', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']


class Review(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    star = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')


class Category(models.Model):
    title = models.CharField(max_length=150)
    is_main = models.BooleanField()
    main_category = models.ForeignKey('Category', related_name='sub_categories', on_delete=models.CASCADE, blank=True,
                                      null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ['id']


class Basket(models.Model):
    sid = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    items = models.ManyToManyField(Item, through='ItemInBasket', related_name='basket')


class ItemInBasket(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    count = models.IntegerField()


class Order(models.Model):
    items = models.ManyToManyField(Item, through='ItemInOrder')
    owner = models.CharField(max_length=150, default='no owner')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['id']


class ItemInOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()