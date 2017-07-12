**PASO 1. INSTALACIÓN DE DEPENDENCIAS.**

**Actualizar y mejorar cualquier paquete existente:**

$ sudo apt-get update

$ sudo apt-get upgrad

**Instalar CMake, para configurar el proceso de construcción de OpenCV:**

$ sudo apt-get install build-essential cmake pkg-config

**Instalar paquetes de E / S de imagen para cargar formatos de archivo de imagen desde el disco:**

$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

**Instalar paquetes de E / S de vídeo. Para leer formatos de archivo de vídeo desde el disco, así como trabajar directamente con secuencias de vídeo:**

$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

$ sudo apt-get install libxvidcore-dev libx264-dev

**Instalar la biblioteca de desarrollo de GTK, para compilar el módulo *** highgui *** que se utiliza para mostrar imágenes a nuestra pantalla y construir GUIs básicas:**

$ sudo apt-get install libgtk2.0-dev

**Instalar dependencias adicionales para optimizar operaciones matriciales:**

$ sudo apt-get install libatlas-base-dev gfortran

**Instalar los archivos iniciales de Python 2.7 y Python 3 para compilar OpenCV con enlaces de Python:**

$ sudo apt-get install python2.7-dev python3-dev



**PASO 2. DESCARGAR CÓDIGO FUENTE OPENCV**

**Tomar el   archivo**** 3.1.0 **** de OpenCV desde el repositorio oficial de  ** [**OpenCV**](https://github.com/Itseez/opencv) **:**

$ cd ~

$ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip

$ unzip opencv.zip

**Obtener la instalación completa de OpenCV:**

$ wget -O opencv\_contrib.zip https://github.com/Itseez/opencv\_contrib/archive/3.1.0.zip

$ unzip opencv\_contrib.zip

**PASO 3. INSTALAR PYTHON 2.7 Y PYTHON 3**

**Instalar **** pip ****, como gestor de paquetes Python:**

$ wget https://bootstrap.pypa.io/get-pip.py

$ sudo python get-pip.py

**Instalar virtualenv y virtualenvwrapper para utilizar entornos virtuales independientes:**

$ sudo pip install virtualenv virtualenvwrapper

$ sudo rm -rf ~/.cache/pip

**Actualizar el archivo ~ /. profile para incluir las siguientes líneas en la   **_** parte inferior **_**  del archivo:**

#virtualenv and virtualenvwrapper

export WORKON\_HOME=$HOME/.virtualenvs

source /usr/local/bin/virtualenvwrapper.sh

**Actualizar el archivo para reflejar los cambios:**

$ echo -e &quot;\n# virtualenv and virtualenvwrapper&quot; &gt;&gt; ~/.profile

$ echo &quot;export WORKON\_HOME=$HOME/.virtualenvs&quot; &gt;&gt; ~/.profile

$ echo &quot;source /usr/local/bin/virtualenvwrapper.sh&quot; &gt;&gt; ~/.profile

**Implementar el código:**

$source~/.profile

**Utilizar el entorno virtual de Python para el desarrollo de la visión por computadora, después de introducir el código creará un entorno virtual cv usando Python 2.7:**

$mkvirtualenv cv-ppython2

**Si deseas usar Python 3, escribir el siguiente código:**

$mkvirtualenv cv-ppython3

**Para comprobar si estas en el entorno virtual CV, para ello es importante escribir el primer código y después el segundo con la herramienta workon, no salir del cv, debe permanecer en CV para el resto de la instalación, no cerrar la terminal:**

$ source ~/.profile

$ workon cv

**Instalar Numpi:**

$pip install nump

**De nueva cuenta es importante permanecer en cv, si la terminal no se encuentra dentro de la CV, reescribir el código:**

$workon cv

**Configurar la compilación utilizando CMAKE:**

$ cd ~/opencv-3.1.0/

$ mkdir build

$ cd build

$ cmake -D CMAKE\_BUILD\_TYPE=RELEASE \

    -D CMAKE\_INSTALL\_PREFIX=/usr/local \

    -D INSTALL\_PYTHON\_EXAMPLES=ON \

    -D OPENCV\_EXTRA\_MODULES\_PATH=~/opencv\_contrib-3.1.0/modules \

    -D BUILD\_EXAMPLES=ON ..

**Compilar OpenCV:**
$ make -j4

**La función del comando **** - ****j4****  controla el número de núcleos para aprovechar al compilar OpenCV 3. El Raspberry Pi 3 tiene  **_** cuatro núcleos **_** , por lo tanto, se suministra un valor de  ****4****    para permitir que OpenCV compile más rápido. Sin embargo, debido a las condiciones de carrera, hay ocasiones en las que se **** producen **** errores al utilizar múltiples núcleos. Si esto le sucede a usted, sugiero iniciar la compilación de nuevo y usar sólo   **_** un **_**  núcleo:**

$ make clean

$ make

**Instalar OpenCV3 en la raspberry:**

$ sudo make install

$ sudo ldconfig

**PASO 4. FINALIZACIÓN DE LA INSTALACIÓN**

**Si la OpenCV se instaló correctamente, verificar carpeta:**

$ ls -l /usr/local/lib/python2.7/site-packages/

total 1852

-rw-r--r-- 1 root staff 1895772 Mar 20 20:00 cv2.so

**Simular****  los enlaces OpenCV en nuestro   entorno virtual  ****cv**  **para Python 2.7:**

$ cd ~/.virtualenvs/cv/lib/python2.7/site-packages/

$ ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

**Verificar los enlaces**  **de OpenCV + Python:**

$ ls -l /usr/local/lib/python3.4/site-packages/

total 1852

-rw-r--r-- 1 root staff 1895932 Mar 20 21:51 cv2.cpython-34m.so

**Cambiar el nombre del archivo:**

$ cd /usr/local/lib/python3.4/site-packages/

$ sudo mv cv2.cpython-34m.so cv2.so

**Simular vínculos OpenCV en el   entorno **** cv **** virtual para Python 3.4:**

$ cd ~/.virtualenvs/cv/lib/python3.4/site-packages/

$ ln -s /usr/local/lib/python3.4/site-packages/cv2.so cv2.s

**PASO 5. PRUEBA DE INSTALACIÓN DEL OPENCV 3**

**Abra un nuevo terminal, ejecute los   comandos, para importar los enlaces Python + OpenCV**

$ source ~/.profile

$ workon cv

$ python

&gt;&gt;&gt; import cv2

&gt;&gt;&gt; cv2.\_\_version\_\_

&#39;3.1.0&#39;

&gt;&gt;&gt;

**Finalmente escribir código para liberar espacio en memoria:**

$rm-rf opencv-3.1.0opencv\_contrib-3.1.0
