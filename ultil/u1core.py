import shutil
import os
from os import path

class GenSourceCore: 

    def __init__(self):
        self.root_link = 'output/'
        self.templates_link = 'templates/'
    
    def read_file(self, path_file):
        with open(self.templates_link + path_file, 'r', encoding='utf8') as f:
            return f.readlines()  

    def create_file(self, file_name, content=''):
        print('file_name', file_name)
        with open(self.root_link + file_name,'w',encoding='utf8') as f:
            f.write(content)

    def create_folder(self, folder_path):
        from pathlib import Path
        Path(self.root_link + folder_path).mkdir(parents=True, exist_ok=True) 

    def copy_folder(self, source_folder, dest_folder):
        try:
            # remove old folder first 
            if os.path.exists(self.root_link + dest_folder):
                shutil.rmtree(self.root_link + dest_folder)

            # copy folder
            shutil.copytree(self.templates_link + source_folder, self.root_link + dest_folder)

        # Directories are the same
        except shutil.Error as e:
            print('Directory not copied. Error: %s' % e)
        # Any error saying that the directory doesn't exist
        except OSError as e:
            print('Directory not copied. Error: %s' % e)


    def render_replace(self, input_path_file, ouput_path_file, params):
        number_param = len(params)

        # read all data in file
        datas = self.read_file(input_path_file)
        output = ''
        
        ans = 0
        
        for data in datas:  
            if data.find('phuong' + str(ans)) >= 0 and ans < number_param:
                output = output + data.replace('phuong' + str(ans), params[ans])
                ans = ans + 1
            else:
                output = output + data
        
        # save file after replace
        self.create_file(ouput_path_file, output)

    def zipdir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    def zip_project(self, project_name):
        import shutil
        from datetime import datetime
        now = datetime.now()  # current date and time
        date_time = now.strftime("%m%d%Y%H%M%S")

        output_filename = 'output/'+ project_name + date_time
        input_dir_name = 'output/'+ project_name
        shutil.make_archive(output_filename , 'zip', input_dir_name)

        return 'http://34.126.84.178/output/'+ project_name + date_time +'.zip'

