# Generated by Django 4.0.4 on 2022-04-25 21:41

from django.db import migrations
import django_grapesjs.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blogs_background_delete_choice_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='html',
            field=django_grapesjs.models.fields.GrapesJsHtmlField(),
        ),

    ]
