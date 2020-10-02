from django.core import serializers

# from models import User
from django.apps import apps 

from apps.a1crud import models

from ultil.u1core import GenSourceCore 
core_gen = GenSourceCore()

class GenCICD:
    def __init__(self):
        self.root_link = 'output/'
        self.templates_link = 'templates/'
    
    def gen_docker_angular(self, idproject):
        project_name = models.Project.objects.filter(id = idproject)[0].name

        # copy docker compose file to project
        source_path_template = 'docker-compose.yml'
        dest_path_template = project_name + '/docker-compose.yml'
        core_gen.render_replace(source_path_template, dest_path_template, [project_name])

        return project_name
