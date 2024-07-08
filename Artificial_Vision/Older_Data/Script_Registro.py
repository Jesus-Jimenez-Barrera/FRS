# Get Information Script (GIS)
# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera
""" This script is designed with the purpose of obtaining information related to facial patterns,
for this it captures the subject's data and stores it for further processing. """

# Functions for the operation of the algorithm
from File_Control_Script import File_Control
from Get_Information_Script import Extract_mesh

# Instance of the classes to use
obj_mesh = Extract_mesh()
obj_file = File_Control()


def User_data_LOG():

    """ In this method, the information that will be registered is obtained and
    the routes for its storage are generated. """

    # Directory search function to store facial patterns
    try:

        user_name = input("Ingrese el nombre del usuario: ")
        obj_mesh.extract_facial_mesh(user_name)

    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")


def main():
    User_data_LOG()


if __name__ == '__main__':
    main()