# Implementation of Neuralangelo for the custom dataset

## Step 1: Setup
### Clone the repository: 
```git clone https://github.com/AbdulRehman555/neuralangelo-for-custom-data.git ```

### Environment setup:
#### Pull Images:
```
* docker pull docker.io/chenhsuanlin/colmap:3.8
* docker pull docker.io/chenhsuanlin/neuralangelo:23.04-py3
```
#### Run containers in the separate terminal windows:
```
* sudo docker run --gpus all --shm-size=4G -it -v {source folder path}:{destination folder path} chenhsuanlin/colmap:3.8
* sudo docker run --gpus all --shm-size=32G -it -v {source folder path}:{destination folder path} chenhsuanlin/neuralangelo:23.04-py3
```

* Here {source folder path} is the path of the folder you want to mount with the container. Note that the same folder must be mounted with both containers. While {destination folder path} is the destination path inside the container.
* In the colmap’s container, install an additional library for the conversion of heif format images into jpg formats.
```
* pip install heif-convert
``` 
## Step 2: Data Preparation
* Place your custom data (assets) in the ‘custom_assets/assets’ folder.
```
* mkdir -p custom_assets/assets
```
* Prepare data (In the colmap container):
```
* bash process_all_assets.sh preparation
```
* Note that this bash script will traverse the ‘custom_assets/assets’ directory, goes through the each asset folder and perform data preparation step.
* You can specify the format of custom data images by setting the IMAGE_FORMAT variable inside the process_all_assets.sh.
## Step 3: Training
* Train custom data (In the neuralangelo container):
```
* bash process_all_assets.sh training
```
* Training settings can be changed from the following configs:
* imaginaire/config_base.yaml
* projects/neuralangelo/configsbase.yaml
## Step 4: Mesh Extraction
* Extract meshes for all the trained assets (In the neuralangelo container):
```
* bash process_all_assets.sh extraction
```


## Official Implementation

### [Project page](https://research.nvidia.com/labs/dir/neuralangelo/) | [Paper](https://arxiv.org/abs/2306.03092/) | [Colab notebook](https://colab.research.google.com/drive/13u8DX9BNzQwiyPPCB7_4DbSxiQ5-_nGF)

<img src="assets/teaser.gif">
