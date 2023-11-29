from django.apps import AppConfig


def create_group(sender, **kwargs):
    from django.contrib.auth.models import Group

    group_names = ['TataUsaha_SET','TataUsaha_ALPALHAN','TataUsaha_BMN','TataUsaha_POSKON','TataUsaha_PUSKOD',
                   'DATIN','PROGLAP','MALUR',
                ]

    # Check if the group already exists to avoid duplicates
    for group_name in group_names:
        if not Group.objects.filter(name=group_name).exists():
            Group.objects.create(name=group_name)


class EarsipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'earsip_app'

    def ready(self):
         # Connect the post_migrate signal to the create_groups function
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_group, sender=self)
