<div align="center">

<h1>Causallm14b大模型量化版本，基于DPO算法优化</h1>

<h2>无内容审查，无思想钢印</h2>


<br><br>


</div>

------


### Quick Install with Conda

```bash
conda create -n venv python=3.10
conda activate venv
```
### Install Manually
#### Make sure you have python3 installed

```bash
sudo apt-get install python3.10
```

#### Pip Packages

```bash
pip install -r requirements.txt
```

```bash

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 
```


## CUDA Toolkit:

Download and install CUDA Toolkit 12.2 from NVIDIA’s official website.

https://developer.nvidia.com/cuda-12-2-0-download-archive?target_os=Windows

Verify the installation with nvcc --version and nvidia-smi.


#### GPU Version Install

```bash
pip uninstall -y llama-cpp-python
set CMAKE_ARGS=-DLLAMA_CUBLAS=on
set FORCE_CMAKE=1
pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
```

## download model

https://huggingface.co/tastypear/CausalLM-14B-DPO-alpha-GGUF

put it in ./mymodel

## change model

edit config.py and change model_path


## how to use

```
python3 app.py
```

![](./test_14b.png)



In the use of the model, attention should be paid to conforming to the local laws and regulations.

Of course, in use, gentlemen can give full play to their imagination, but to pay attention to the issue of legal compliance, they must conform to the core socialist values and carry forward the positive energy.

It is emphasized here that prosperity, democracy, civilization, harmony, freedom, equality, justice, the rule of law, patriotism, dedication, integrity and friendliness are the basic contents of socialist core values.




