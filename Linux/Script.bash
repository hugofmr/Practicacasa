#!/bin/bash

#Creando una ruta para el directorio del usuario
master_dir="Master"

#Creando una funcion en la que si ya existe la carpeta literal de "Master" bajo la ruta "$master_dir" se elimine y a su posterior se cree
#toda la ruta nuevamente 
if [ -d "$master_dir" ]; then
    rm -rf "$master_dir"
    echo "Carpeta Master eliminada"
fi

#creando la carpeta Master
mkdir "$master_dir"
echo "has creado la carpeta Master"
#Creando la carpeta Linux dentro de Master
mkdir $master_dir/Linux
echo "has creado la carpeta Linux"
#Creando el Fichero1 en carpeta Linux
touch $master_dir/Linux/Fichero1.sh
echo "has creado el Fichero1.sh"
#Creando la carpeta Git en Master
mkdir $master_dir/Git
echo "has creado la carpeta Git"
#Creando el Fichero2.sh en Git
touch $master_dir/Git/Fichero2.sh
echo "has creado el Fichero2"
#Creando la carpeta Notebook
mkdir $master_dir/Notebook
echo "has creado la carpeta Notebook"
#Creando la carpeta Jupiter en Notebook
mkdir $master_dir/Notebook/Jupiter
echo "has creado la carpeta Jupiter"
#Creando el Fichero3.txt en Jupiter
touch $master_dir/Notebook/Jupiter/Fichero3.txt
echo "has creado el Fichero3.txt"
#Creando la carpeta Colab en Notebook
mkdir $master_dir/Notebook/Colab
echo "has creado la carpeta Colab"
#Creando el Fichero4.txt en Jupiter
touch $master_dir/Notebook/Colab/Fichero4.txt
echo "has creado el Fichero4.txt"

#Para la revision a posterior utilizar el comando "Tree" dentro de la carpeta "Master"


#Creando el script para la creacion de un script para la creacion de cosa multiples

#!/bin/bash
master_dir="Master"
if [ -d "$master_dir" ]; then
    rm -rf "$master_dir"
    echo "Carpeta Master eliminada"
fi
mkdir "$master_dir"
echo "has creado la carpeta Master"
mkdir $master_dir/Linux
echo "has creado la carpeta Linux"
touch $master_dir/Linux/Fichero1.sh
echo "has creado el Fichero1.sh"
mkdir $master_dir/Git
echo "has creado la carpeta Git"
touch $master_dir/Git/Fichero2.sh
echo "has creado el Fichero2"
mkdir $master_dir/Notebook
echo "has creado la carpeta Notebook"
mkdir $master_dir/Notebook/Jupiter
echo "has creado la carpeta Jupiter"
touch $master_dir/Notebook/Jupiter/Fichero3.txt
echo "has creado el Fichero3.txt"
mkdir $master_dir/Notebook/Colab
echo "has creado la carpeta Colab"
touch $master_dir/Notebook/Colab/Fichero4.txt
echo "has creado el Fichero4.txt"

