# Generated by Django 3.2.4 on 2021-11-30 09:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=20)),
                ('numero', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('eglise_frequente', models.CharField(max_length=200)),
                ('classe', models.CharField(max_length=50)),
                ('residence', models.CharField(max_length=150)),
                ('probleme_particulier', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('projets', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('etablissement', models.CharField(max_length=100)),
                ('dirigeant', models.CharField(max_length=200)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]