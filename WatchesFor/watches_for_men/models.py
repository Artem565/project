from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Maker(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Watches(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.FloatField(verbose_name='Размер(см.)')
    material = models.CharField(max_length=MAX_LENGTH, verbose_name='Материал')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступен к заказу')

    category = models.ManyToManyField(Category, blank=True, null=True, verbose_name='Категория')
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT, verbose_name='Производитель')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Часы'


class Order(models.Model):
    SHOP = 'SH'
    COURIER = 'CR'
    TYPE_DELIVERY = [
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
    ]
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя заказчика')
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия заказчика')
    delivery_address = models.CharField(null=True, blank=True, max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ получения')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    finish = models.BooleanField(default=False, verbose_name='Выполнен?')

    watches = models.ManyToManyField(Watches, through='PosOrder', verbose_name='Часы')

    def __str__(self):
        return f"№{self.pk} - ({self.buyer_name} {self.buyer_firstname}) ({self.create_date})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название ')
    telephone = models.CharField(max_length=16, verbose_name='Номер телефона')
    address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес главного офиса')
    is_exists = models.BooleanField(default=True, verbose_name='Возможность заказа')

    def __str__(self):
        return f'{self.name} ({self.telephone})'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Supply(models.Model):
    date_supply = models.DateTimeField(verbose_name='Дата поставки')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')
    watch = models.ManyToManyField(Watches, through='PosSupply', verbose_name='Часы')

    def __str__(self):
        return f'#{self.pk} - {self.date_supply} {self.supplier.name}'

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class PosOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    watch = models.ForeignKey(Watches, on_delete=models.PROTECT, verbose_name='Часы')

    count = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')

    def __str__(self):
        return f'#{self.order.pk} - {self.watch.name} ({self.watch.price} руб.) ({self.order.buyer_name} {self.order.buyer_firstname})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'


class PosSupply(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, verbose_name='Поставка')
    watch = models.ForeignKey(Watches, on_delete=models.PROTECT, verbose_name='Часы')

    count = models.PositiveIntegerField(default=1, verbose_name='Количество товара')

    def __str__(self):
        return f'{self.watch.name} - #{self.supply.pk} ({self.supply.date_supply})'

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставки'