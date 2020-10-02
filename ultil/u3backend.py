from django.core import serializers

# from models import User
from django.apps import apps 

from apps.a1crud import models

from ultil.u1core import GenSourceCore 
core_gen = GenSourceCore()

class GenSourceBackend: 
    def __init__(self):
        self.root_link = 'output/'
        self.templates_link = 'templates/'
        
    
    def gen_backend_php(self, idproject):
        project_name = models.Project.objects.filter(id = idproject)[0].name

        # copy sample to output
        core_gen.copy_folder('backend/php', project_name + '/backend')

        tables = models.Class.objects.filter(idproject = idproject)
        params = []
        
        if len(tables) > 0: 
            content = ''
            import_services = ''
            ans = 100
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

                content = content + '<?php                                                                                      \n'
                content = content + '    switch ($data->what) {                                                                 \n'
                content = content + '        //******************'+ classname +'************************             \n'
                content = content + '        // '+ classname +'('+ ','.join(properties) +')\n'

                properties = properties[1:]

                content = content + '        // Get all data from '+ classname +'\n'
                content = content + '        case '+ str(ans) +': {                                                                        \n'
                content = content + '            $sql = "SELECT * FROM '+ classname +'";\n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '                                                                                           \n'
                content = content + '        // Insert data to '+ classname +'\n'
                content = content + '        case '+ str(ans + 1) +': {                                                                        \n'
                content = content + '            $sql = "INSERT INTO '+ classname +'('+ ','.join(properties) +')\n'
                
                # create insert value => VALUES('$data->name','$data->address')
                insert_value = ','.join(list(map(lambda x: '\'$data->'+ x +'\'', properties)))
                
                content = content + '                    VALUES('+ insert_value +')";                               \n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '                                                                                           \n'
                content = content + '        // Update data '+ classname +'\n'
                content = content + '        case '+ str(ans + 2) +': {\n'

                # create update value => name='$data->name', address='$data->address'
                update_value = ','.join(list(map(lambda x: x + '=\'$data->' + x+'\'', properties)))

                content = content + '            $sql = "UPDATE '+ classname +' SET '+ update_value +'\n'
                content = content + '                    WHERE id=\'$data->id\'";                                                 \n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '                                                                                           \n'
                content = content + '        // Delete data of '+ classname +'\n'
                content = content + '        case '+ str(ans + 3) +': {                                                                        \n'
                content = content + '            $sql = "DELETE FROM '+ classname +'\n'
                content = content + '                    WHERE id IN($data->listid)";                                           \n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '                                                                                           \n'
                content = content + '        // Find data with id '+ classname +'\n'
                content = content + '        case '+ str(ans + 4) +': {                                                                        \n'
                content = content + '            $sql = "SELECT * FROM '+ classname +'\n'
                content = content + '                    WHERE id=\'$data->id\'";                                                 \n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '                                                                                           \n'
                content = content + '        // Select with pagination(offset, number-item-in-page) '+ classname +'\n'
                content = content + '        case '+ str(ans + 5) +': {                                                                        \n'
                content = content + '            $sql = "SELECT * FROM '+ classname +'\n'
                content = content + '                    LIMIT $data->offset, $data->limit";                                    \n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '                                                                                           \n'
                content = content + '        // Count number item of '+ classname +'\n'
                content = content + '        case '+ str(ans + 6) +': {                                                                        \n'
                content = content + '            $sql = "SELECT COUNT(1) FROM '+ classname +' ";\n'
                content = content + '            break;                                                                         \n'
                content = content + '        }                                                                                  \n'
                content = content + '    }                                                                                      \n'
                content = content + '?>                                                                                         \n'
                
                # create service file include "../Service/100lop.php";
                import_services = import_services + '	include "../Service/'+ str(ans) + classname +'.php";\n'
                core_gen.create_file(project_name + '/backend/Service/' + str(ans) + classname + '.php', content)
                content = ''
                
                ans = ans + 100 

            params.append(import_services)    

            # gen project folder  
            source_path_template = 'backend/php/Controller/SelectAllByWhat.php'
            dest_path_template = project_name + '/backend/Controller/SelectAllByWhat.php'
            core_gen.render_replace(source_path_template, dest_path_template, params)

        else:
            print('project havent class')
    
