from django.core import serializers

# from models import User
from django.apps import apps 

from apps.a1crud import models

from ultil.u1core import GenSourceCore 
core_gen = GenSourceCore()

class GenSourceDatabase: 
    def __init__(self):
        self.root_link = 'output/'
        self.templates_link = 'templates/'
    
    def gen_database_mysql(self, idproject):
        params = ['Le Hong Phuong']
        # test gen  
        tables = models.Class.objects.filter(idproject = idproject)
        if len(tables) > 0: 
            content = ''
            roles = 'a:3'
            ans = 1

            print(serializers.serialize("json",  tables)) 
            for table in tables:  
                classname = table.classname
                properties = table.properties.split(',')
                attributes = table.attributes.split(',')
                lengths = table.lengths.split(',')
                print(classname)
                print(properties) #id,name,address
                print(attributes) #INT,VARCHAR,VARCHAR
                print(lengths)    #0,255,0

                classname = 'p' + classname

                content = content + '-- \n' 
                content = content + '-- Table structure for table `'+ classname +'` \n'
                content = content + '--                      \n'
                content = content + 'CREATE TABLE `'+ classname +'` (                                          \n'
                
                for i in range(len(properties)):
                    if properties[i] == 'id':
                        content = content + '  `id` int(11) NOT NULL,\n'
                        continue

                    if attributes[i] == 'INT':
                        content = content + '  `'+ properties[i] +'` int(11) DEFAULT NULL,\n'
                    
                    if attributes[i] == 'VARCHAR':
                        content = content + '  `'+ properties[i] +'` varchar('+ lengths[i] +') COLLATE utf8_unicode_ci DEFAULT NULL,\n'
                    
                    if attributes[i] == 'TEXT':
                        content = content + '  `'+ properties[i] +'` text COLLATE utf8_unicode_ci DEFAULT NULL,\n'

                    if attributes[i] == 'DATE':
                        content = content + '  `'+ properties[i] +'` date NOT NULL,\n'

                    if attributes[i] == 'DATETIME':
                        content = content + '  `'+ properties[i] +'` datetime NOT NULL DEFAULT current_timestamp(),\n'

                    if attributes[i] == 'FLOAT':
                        content = content + '  `'+ properties[i] +'` float DEFAULT NULL,\n'

                    if attributes[i] == 'BOOLEAN':
                        content = content + '  `'+ properties[i] +'` tinyint(1) DEFAULT NULL,\n'

                    if attributes[i] == 'VARBINARY':
                        content = content + '  `'+ properties[i] +'` varbinary('+ lengths[i] +') DEFAULT NULL,\n'
                
                # delete string ',' end of string
                content = content[:-2] + '\n'

                content = content + ') ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;  \n'
                content = content + '                                                               \n'
                content = content + '--                                                             \n'
                content = content + '-- Indexes for table `'+ classname +'`                                    \n'
                content = content + '--                                                             \n'
                content = content + 'ALTER TABLE `'+ classname +'` ADD PRIMARY KEY (`id`);                     \n'
                content = content + '                                                               \n'
                content = content + '--                                                             \n'
                content = content + '-- AUTO_INCREMENT for table `'+ classname +'`                             \n'
                content = content + '--                                                             \n'
                content = content + 'ALTER TABLE `'+ classname +'` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;\n' 
                content = content + '                                                               \n'

                # update permission
                roles = roles + ',' + chr(97 + ans) + ':3'
                ans = ans + 1

            params.append(roles)
            params.append(content)

            # gen project folder
            project_name = models.Project.objects.filter(id = idproject)[0].name
            core_gen.create_folder(project_name + '/database')
            core_gen.render_replace('database/input_mysql.sql', project_name + '/database/output.sql', params)

        else:
            print('project havent class')
    
