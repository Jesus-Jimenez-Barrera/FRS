import os
from django.conf import settings

class File_Control:
    def __init__(self):
        self.location_script = settings.BASE_DIR

    def dir_database(self):
        try:
            name_dir = 'Facial_Pattern'
            location_database = os.path.join(self.location_script, "media", "Database")
            output_file_dir = os.path.join(location_database, name_dir)
            
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)
                print(f'Directorio creado')
            
            return os.path.abspath(output_file_dir)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
