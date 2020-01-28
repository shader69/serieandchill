# Generated by Django 3.0.1 on 2019-12-27 13:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_serie_seasonnumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='rate',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default=None, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('serie', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serie', to='app.Serie')),
            ],
        ),
    ]