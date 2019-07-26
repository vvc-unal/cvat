# Generated by Django 2.1.9 on 2019-07-26 10:17

import cvat.apps.annotation.models
import cvat.apps.engine.models
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('format', cvat.apps.engine.models.SafeCharField(max_length=16)),
                ('file_extension', cvat.apps.engine.models.SafeCharField(max_length=16)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('handler_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=settings.BASE_DIR), upload_to=cvat.apps.annotation.models.upload_file_handler)),
                ('version', cvat.apps.engine.models.SafeCharField(max_length=16)),
                ('dump_specification', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('parse_specification', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
