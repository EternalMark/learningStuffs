FROM node:24

# Instalar dependencias del sistema
RUN apt update && apt install -y \
    git \
    wget \
    curl \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libgbm-dev \
    libxshmfence-dev \
    xvfb \
    && apt clean

# Crear usuario sin privilegios (opcional)
# RUN useradd -ms /bin/bash pinokio
# USER pinokio
WORKDIR /home/pinokio

# Clonar Pinokio
# RUN git clone https://github.com/pinokiocomputer/pinokio.git
# WORKDIR /home/pinokio/Pinokio

# Instalar dependencias y construir
# RUN npm install
# RUN npm run build

# Comando de inicio
# CMD ["npm", "start"]


#docker build -t pinokioimagenode .
##docker run -p 7000-7010:7000-7010 -v /mnt/SSD2T/2-DiplomadoIA/DeepLearning/dockersdata/pinokio:/home/pinokio -it --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix --gpus all --ipc=host --name pinokiocontainer pinokioimagenode 
##docker run -p 8871:8888 -v /mnt/SSD2T/2-DiplomadoIA/DeepLearning/dockersdata/openGL:/home/carretero -it --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix --gpus all --ipc=host --name openglcontainer carreterodockerimage  
#
#pinokio --no-sandbox