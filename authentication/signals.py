from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """Crea los grupos por defecto al ejecutar migraciones."""
    groups = ["admin", "user"]
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)
    print("✅ Grupos creados exitosamente.")
