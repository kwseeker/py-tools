# NVIDIA CUDA 更新

CUDA（Compute Unified Device Architecture）是由NVIDIA推出的一种并行计算平台和编程模型，旨在利用NVIDIA GPU的并行计算能力。

```shell
# 查看显卡即 CUDA 信息
nvidia-smi

# 当前安装的显卡驱动支持的 CUDA 版本最高为 12.1
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.41.03              Driver Version: 530.41.03    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA P104-100                 Off| 00000000:01:00.0 Off |                  N/A |
| 37%   43C    P8                6W / 180W|      4MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      1349      G   /usr/lib/xorg/Xorg                            4MiB |
+---------------------------------------------------------------------------------------+

# 安装 CUDA 12.1, https://developer.nvidia.com/cuda-toolkit-archive
# 本机 Linux Mint 21.1 基于 Ubuntu 22.04
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-ubuntu2204-12-1-local_12.1.1-530.30.02-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-1-local_12.1.1-530.30.02-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

faster-whisper 模型在 GPU 上运行需要安装下面的库：

- [cuBLAS for CUDA 12](https://developer.nvidia.com/cublas)
- [cuDNN 9 for CUDA 12](https://developer.nvidia.com/cudnn)

其中 cuBLAS 在安装 CUDA 时就一起安装了，只需要额外安装 cuDNN：

```
wget https://developer.download.nvidia.com/compute/cudnn/9.10.2/local_installers/cudnn-local-repo-ubuntu2204-9.10.2_1.0-1_amd64.deb
sudo dpkg -i cudnn-local-repo-ubuntu2204-9.10.2_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-ubuntu2204-9.10.2/cudnn-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudnn-cuda-12
```

测试语音识别处理中是否使用 GPU: 

```
# nvidia-smi 结果中可以看到语音识别进程
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A    486447      C   ...rk/python/py-tools/.venv/bin/python     3250MiB |
+---------------------------------------------------------------------------------------+
```