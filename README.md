<h1 align="center" >
    <img src="https://www.edx.org/images/logos/edx-logo-elm.svg" height="10%" width="10%">
</h1>

# MoocWebApp

Introduction to the development of web applications (Universidad Autonoma de Madrid)

## Para iniciar

Aqui obtendras conocimientos básicos sobre `flask` y `python3`, esto esta realizado bajo el entorno del **`SO Windows`**.
Pero pierde cuidado tambien puedes usar otro sistema operativo.

- Primero necesitamos instalar python 3.10
- Luego descargemos Pycharm 
- Por ultimo asegurate de tener pip

Una vez instalado python3 nos ubicamos en la carpeta de instalación, abrimos la consola y verificamos si tenemos lo necesario e instalamos `virtualenv` .

```shell
# Comprobamos instalación de python3 (salir con Control+Z)
c:\Python$>> python
# Comprobamos instalacion de pip3
c:\Python$>> pip3 help
# Instalamos virtualenv
c:\Python$>> pip3 install virtualenv

# Nos ubicamos en la carpteta de nuestro proyecto
c:\Python$>> cd C:\...\moocwebapp
# Creamos el entorno virtual
c:\...moocwebapp$>> virtualenv web
# Activamos el entorno virtual
c:\...moocwebapp$>> web\Scripts\activate
# Una vez adentro ya podemos instalar librerias
(web) c:\...moocwebapp$>> pip install flask
# Para salir del entorno podemos usar
(web) c:\...moocwebapp$>> deactivate
```
