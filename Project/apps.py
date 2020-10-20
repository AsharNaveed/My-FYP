from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'Project'

    def ready(self):
        import Project.signals
