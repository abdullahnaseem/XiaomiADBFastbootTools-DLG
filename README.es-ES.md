

# Creador de Lista Debloat (DLG)
Genera una lista compatible con **XiaomiADBFastbootTools** de las aplicaciones y el bloatware de tu dispositivo. 
## Enlace al proyecto original [XiaomiADBFastbootTools](https://github.com/Szaki/XiaomiADBFastbootTools "XiaomiADBFastbootTools") 


### Características
* Te permite gestionar todas tus aplicaciones con **XiaomiADBFastbootTools**.
* Gestiona aplicaciones que no están disponibles por defecto en **XiaomiADBFastbootTools**.
* Comprueba las aplicaciones de bloatware instaladas que es seguro eliminar.


### Por hacer
* Obtener la última *lista de bloatware* desde **GitHub**
* Extraer automáticamente la *lista de aplicaciones* del dispositivo. 
* Soportar más plataformas.


### Uso
* Descarga la última versión.
* Asegúrate de tener la *lista de bloatware* y la *lista de aplicaciones* en el mismo directorio. (**Lee más abajo para obtener más información**)
* Ejecuta el archivo ejecutable desde el directorio.
* Importa las *listas generadas* en el gestor de aplicaciones de **XiaomiADBFastbootTools**.
* ¡Gestiona tus aplicaciones con facilidad!


### Listas
Los nombres de los archivos y el formato pueden cambiar en futuras versiones. Para evitar errores, utiliza los nombres exactos con distinción de mayúsculas y minúsculas para los archivos.

**apps.txt** - Lista de todas las aplicaciones instaladas en tu dispositivo. Se puede extraer del dispositivo mediante comandos simples de adb
```bash
  adb shell
  pm list packages -f > /sdcard/apps.txt
  adb pull /sdcard/apps.txt 
```

**debloat.txt** - Lista de los paquetes de bloatware conocidos y seguros de eliminar. Se incluye con el ejecutable.

**package-list.txt** - Lista generada de todas las aplicaciones instaladas en tu dispositivo, compatible con **XiaomiADBFastbootTools**.

**debloat-list.txt** - Lista generada del bloatware instalado en tu dispositivo que es seguro eliminar, compatible con **XiaomiADBFastbootTools**.

  


# AVISO
Aunque la *lista de bloatware* contiene aplicaciones que han sido verificadas y probadas por usuarios, eliminar ciertas aplicaciones aún puede causar problemas o errores en algunos sistemas.
