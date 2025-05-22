# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Instala dependencias necesarias
# RUN apt update && apt install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*
# RUN apt update && apt install ffmpeg libsm6 libxext6  -y

# Instala Jupyter Notebook
RUN pip install --upgrade pip
RUN pip install --no-cache-dir notebook
# RUN pip install tensorflow[and-cuda]
# RUN pip install matplotlib
# RUN pip install manim
# RUN pip install pandas
# RUN pip install ydata_profiling ipywidgets
# RUN pip install torch torchvision torchaudio torchsummary
# RUN pip install -U scikit-learn
# RUN pip install pydot graphviz
#Para cv2
# RUN pip install opencv-python
# RUN pip install opencv-contrib-python
# RUN pip install ipython
# ADD . /media/markos/SSD2T/2-DiplomadoIA
#RUN pip install --no-cache-dir numpy pandas matplotlib

# Establece el directorio de trabajo
WORKDIR /home/carretero

# Expone el puerto para Jupyter Notebook
EXPOSE 8888

# Comando para ejecutar Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]




##---------Comandos para despues de levantar la imagen

#Crear la imagen. Se debe estar parado donde se encuentra el dockefile
##docker build -t carreterodockerimage .

#Levantar el contenedor #Con -v ${PWD} monta la carpeta donde estas parado a /home/jupyter del contenedor
## Con "-it --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix " da permisos para el display de la compu
#docker run -p 8870:8888 -v /mnt/SSD2T/2-DiplomadoIA/DeepLearning/dockersdata/carreterocontainer:/home/carretero --gpus all --ipc=host --name carreterocontainer carreterodockerimage 
#docker run -p 8871:8888 -v /mnt/SSD2T/2-DiplomadoIA/DeepLearning/dockersdata/openGL:/home/carretero -it --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix --gpus all --ipc=host --name openglcontainer carreterodockerimage 


#Crear jupiter server cambiar contraseña (Despues de crear el contenedor)
#https://jupyter-server.readthedocs.io/en/latest/operators/public-server.html
#jupyter server --generate-config 
#jupyter server password 





#Para detectar la GPU y evitar el error "docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].""
#docker context use default
