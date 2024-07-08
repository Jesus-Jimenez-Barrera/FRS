# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera
""" Script designed to manage the files system """

# Program library
import os

# Beginning of the file control class
class File_Control:

    def __init__(self):
        self.location_script = os.path.dirname(os.path.abspath(__file__))

    # Function to log data
    def dir_database(self):

        # Start error checking
        try:

            # Name of the file where information will be sent
            name_dir = 'Facial_Pattern'

            # File control operations (used to specify the output directory)
            location_database = os.path.join(self.location_script, "..", "Database")
            output_file_dir = os.path.join(location_database, name_dir)

            # If the file does not output, this function will create a new one
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)
                print(f'Directorio creado')
                output_file_dir = os.path.abspath(output_file_dir)
                print(f'La direccion es: {output_file_dir}')
                return output_file_dir

            # If the file does not output, this function will create a new one
            else:
                output_file_dir = os.path.abspath(output_file_dir)
                print(f'La direccion encontrada es lla siguiente: {output_file_dir}')
                return output_file_dir

        except Exception as e:
            print(f'Ha ocurrido un error: {e}')