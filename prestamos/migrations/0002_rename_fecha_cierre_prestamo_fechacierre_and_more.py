# Generated by Django 4.2.20 on 2025-04-08 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='fecha_cierre',
            new_name='fechaCierre',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='fecha_inicio',
            new_name='fechaInicio',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='interes_mensual_generado',
            new_name='interesMensualGenerado',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='monto_inicial',
            new_name='montoInicial',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='saldo_actual',
            new_name='saldoActual',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='tasa_interes_mensual',
            new_name='tasaInteresMensual',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='activo',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='estado',
            field=models.CharField(default='Activo', max_length=10),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='fechaActualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
