"""
index-tts 并没有分发到 PyPI 仓库，需要手动安装 index-tts 为软件包
    conda create -n index-tts python=3.10
    conda activate index-tts
    apt-get install ffmpeg
    # or use conda to install ffmpeg
    conda install -c conda-forge ffmpeg
    pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
    # 安装为依赖包，注意仅仅是安装到了当前激活的环境
    pip install -e .
    pip list | grep index
    安装成功后可以看到：
    indextts                 0.1.4       /.../index-tts
"""
