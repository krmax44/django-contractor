# Generated by Django 2.2.4 on 2020-04-15 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('token', models.UUIDField(default=uuid.uuid4)),
                ('version', models.IntegerField(default=0)),
                ('source_url', models.URLField()),
                ('files', models.TextField(blank=True)),
                ('webhook_log', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contract',
                'verbose_name_plural': 'contracts',
            },
        ),
        migrations.CreateModel(
            name='ContractWorkPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='contractor_contractworkplugin', serialize=False, to='cms.CMSPlugin')),
                ('javascript', models.TextField(blank=True)),
                ('styles', models.TextField(blank=True)),
                ('version', models.IntegerField(default=0)),
                ('xpath', models.CharField(blank=True, max_length=255)),
                ('html', models.TextField(blank=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractor.Contract')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]