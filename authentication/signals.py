from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """Crea los grupos por defecto al ejecutar migraciones."""
    groups = ["admin", "user"]
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)
    print("✅ Grupos creados exitosamente.")

@receiver(post_save, sender=CustomUser)
def add_superuser_to_admin_group(sender, instance, created, **kwargs):
    """Agrega automáticamente el superusuario al grupo 'admin'."""
    if created and instance.is_superuser:
        admin_group, _ = Group.objects.get_or_create(name="admin")
        instance.groups.add(admin_group)
        print(f"✅ Usuario {instance.username} agregado al grupo 'admin'.")
