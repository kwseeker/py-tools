from huggingface_hub import hf_hub_download

# 访问 huggingface_hub 需要翻墙，推荐从 modelscope 下载
file_path = hf_hub_download(repo_id="Systran/faster-whisper-base", filename="model.bin",
                            local_dir="faster-whisper-base")
print(f"Model file downloaded to: {file_path}")
