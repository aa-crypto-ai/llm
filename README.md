## Setup nvidia for docker
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# check and list gpus
docker run -it --rm --gpus all ubuntu nvidia-smi
```

## check your CUDA version
`nvcc --version`

then go to https://hub.docker.com/r/nvidia/cuda/tags to choose the appropriate image and modify the `Dockerfile` if needed

## Build and run the docker
```
git clone https://github.com/aa-crypto-ai/llm.git
cd llm
docker build -t llm .
# to keep the container not exiting
docker run -dit llm
docker exec -it <container_id> bash
```
