# Generated by Django 3.1.1 on 2020-09-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['reg_no']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(related_name='products', to='drugs.Ingredient'),
        ),
    ]