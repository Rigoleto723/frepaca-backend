# Generated by Django 4.2.20 on 2025-04-07 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialLiquidacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_liquidado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_liquidacion', models.DateTimeField(auto_now_add=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo')),
            ],
        ),
    ]
