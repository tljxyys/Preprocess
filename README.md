# MRI 数据预处理与图像重建代码说明 / MRI Data Preprocessing and Image Reconstruction Code Documentation

## 概述 / Overview
本代码实现了对fastMRI数据集中的单线圈膝关节MRI数据进行解压、预处理和图像重建的功能。主要包含tar文件解压缩和HDF5数据处理两大模块，能够从k-space数据重建MRI图像，并以指定帧数保存为PNG格式。  
This code implements functionalities for decompressing, preprocessing, and reconstructing single-coil knee MRI data from the fastMRI dataset. It consists of two main modules: tar file extraction and HDF5 data processing, which reconstruct MRI images from k-space data and save specified frames in PNG format.

## 主要功能 / Key Features
### 1. 数据解压模块 / Data Extraction Module
- 自动解压.tar.xz格式的原始数据文件  
  Automatically extracts .tar.xz format raw data files
- 创建标准化的目录结构  
  Creates standardized directory structures

### 2. 数据处理模块 / Data Processing Module
- 读取HDF5格式的k-space数据  
  Reads k-space data in HDF5 format
- 执行快速傅里叶逆变换(IFFT)重建图像  
  Performs image reconstruction using Inverse Fast Fourier Transform (IFFT)
- 自动标准化图像强度值(0-255范围)  
  Automatically normalizes image intensity values (0-255 range)
- 按病例ID创建分层目录结构  
  Creates hierarchical directory structure by case ID
- 支持自定义每例样本的保存帧数  
  Supports customizable number of saved frames per case

## 数据来源 / Data Source
本代码使用的原始数据来自NYU Langone Health的fastMRI项目:  
The raw data used by this code comes from the fastMRI project by NYU Langone Health:  
[https://fastmri.med.nyu.edu](https://fastmri.med.nyu.edu)

**重要提示 / Important Notice**  
使用者应严格遵守fastMRI数据使用协议:  
Users must strictly adhere to the fastMRI data usage agreement:
1. 仅可用于非商业研究用途  
   For non-commercial research use only
2. 必须引用官方论文(Zbontar et al., 2018)  
   Mandatory citation of the original paper (Zbontar et al., 2018)
3. 禁止患者身份识别  
   Prohibition of patient identification
4. 遵守CC-BY-NC 4.0许可条款  
   Compliance with CC-BY-NC 4.0 license terms

## 使用说明 / Usage Instructions
### 环境要求 / Requirements
- Python 3.7+
- 依赖库: h5py, numpy, Pillow, tqdm  
  Dependencies: h5py, numpy, Pillow, tqdm

### 参数配置 / Parameter Configuration
```python
unzip_tar(
    tar_path="/path/to/input.tar.xz",  # 输入tar文件路径 / Input tar file path
    extract_dir="/output/directory/"   # 解压输出目录 / Extraction directory
)

process_h5_folder(
    input_folder="/input/h5/folder/",  # HDF5文件目录 / HDF5 files directory 
    output_root="/output/image/root/", # 图像输出根目录 / Image output root
    frames_per_file=20                # 每例保存帧数 / Frames per case
)
