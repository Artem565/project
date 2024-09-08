import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=255, verbose_name='Имя заказчика')),
                ('buyer_firstname', models.CharField(max_length=255, verbose_name='Фамилия заказчика')),
                ('delivery_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес доставки')),
                ('delivery_type', models.CharField(choices=[('SH', 'Самовывоз'), ('CR', 'Курьер')], default='SH', max_length=2, verbose_name='Способ получения')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('finish', models.BooleanField(default=False, verbose_name='Выполнен?')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название ')),
                ('telephone', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес главного офиса')),
                ('is_exists', models.BooleanField(default=True, verbose_name='Возможность заказа')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_supply', models.DateTimeField(verbose_name='Дата поставки')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watches_for_men.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставка',
                'verbose_name_plural': 'Поставки',
            },
        ),
        migrations.CreateModel(
            name='PosSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watches_for_men.supply', verbose_name='Поставка')),
            ],
            options={
                'verbose_name': 'Позиция поставки',
                'verbose_name_plural': 'Позиции поставки',
            },
        ),
        migrations.CreateModel(
            name='Watches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('size', models.FloatField(verbose_name='Размер(см.)')),
                ('material', models.CharField(max_length=255, verbose_name='Материал')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')),
                ('is_exists', models.BooleanField(default=True, verbose_name='Доступен к заказу')),
                ('category', models.ManyToManyField(blank=True, null=True, to='watches_for_men.category', verbose_name='Категория')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watches_for_men.maker', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Часы',
            },
        ),
        migrations.AddField(
            model_name='supply',
            name='watch',
            field=models.ManyToManyField(through='watches_for_men.PosSupply', to='watches_for_men.watches', verbose_name='Часы'),
        ),
        migrations.AddField(
            model_name='possupply',
            name='watch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watches_for_men.watches', verbose_name='Часы'),
        ),
        migrations.CreateModel(
            name='PosOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Скидка')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watches_for_men.order', verbose_name='Заказ')),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watches_for_men.watches', verbose_name='Часы')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиции заказа',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='watches',
            field=models.ManyToManyField(through='watches_for_men.PosOrder', to='watches_for_men.watches', verbose_name='Часы'),
        ),
    ]