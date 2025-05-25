FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

# Evita problemas con locales
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8

# # Instala dependencias para OpenGL, Python y PIL
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    ffmpeg \
    # libgl1 \
    # libglx0 \
    # libglx-mesa0 \
    # libgl1-mesa-glx \
    # libglapi-mesa \
    # libx11-6 \
    # libxext6 \
    # libglu1-mesa \
    # libnvidia-gl-550 \
    # libglfw3 \
    # libglfw3-dev \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

RUN /bin/sh -c pip install --upgrade pip
RUN /bin/sh -c pip install PyOpenGL PyOpenGL_accelerate glfw pip pillow freetype-py pygame PyOpenGL PyOpenGL_accelerate numpy
# RUN /bin/sh -c pip install jupyterlab
# RUN /bin/sh -c pip install --no-cache-dir notebook

# # Instala bibliotecas de Python
# RUN pip install --upgrade pip && pip install \
#     PyOpenGL \
#     PyOpenGL_accelerate \
#     glfw \
#     Pillow \
#     numpy


# Establece el directorio de trabajo
WORKDIR /home/openglnvidia

# Expone el puerto para Jupyter Notebook
# EXPOSE 8888


# Comando para ejecutar Jupyter Notebook
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

#docker run -p 8872:8888 -v /mnt/SSD2T/2-DiplomadoIA/DeepLearning/dockersdata/openGL:/home/openglnvidia -it --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix --gpus all -it -e NVIDIA_VISIBLE_DEVICES=all -e NVIDIA_DRIVER_CAPABILITIES=all --ipc=host --name openglnvidiacontainer openglnvidiaimage 

#nohup jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
