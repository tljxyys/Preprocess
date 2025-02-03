# MRI 数据预处理代码说明 / MRI Data Preprocessing Code Documentation

## 概述 / Overview
FastMRI_H5_to_PNG代码文件实现了对fastMRI数据集中的单线圈膝关节MRI数据进行解压、预处理和图像重建的功能。主要包含tar文件解压缩和HDF5数据处理两大模块，能够从k-space数据重建MRI图像，并以指定帧数保存为PNG格式。  
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
- 执行傅里叶逆变换(IFFT)重建图像  
  Performs image reconstruction using Inverse Fast Fourier Transform (IFFT)
- 标准化图像强度值(0-255范围)  
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
```

## 可用数据集 / Available Datasets
### 预处理的FastMRI数据集膝关节MRI图像 / Preprocessed Knee MRI Images
我们提供了基于fastMRI官方数据knee_singlecoil_val.tar预处理的图像样本集：  
We provide preprocessed image samples based knee_singlecoil_val.tar on the official fastMRI data:

[![Download](https://img.shields.io/badge/Download_FastMRI_PNG_Images-Google_Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1JGFZkP71IPX16ZYX1TWSs5xmvBUnpaAu/view?usp=sharing)

**数据集特性 / Dataset Characteristics**
- 原始来源: fastMRI knee_singlecoil_val 验证集  
  Original Source: fastMRI knee_singlecoil_val validation set
- 处理方式: 每个病例均匀采样20帧  
  Processing: 20 uniformly sampled frames per case
- 格式规格: PNG格式 (368x640 分辨率)  
  Format: PNG (368x640 resolution)
- 命名规范: 
  ```
  {case_id}/
  ├── {case_id}_slice0000.png  # 格式保留原始相位信息
  ├── ...
  └── {case_id}_slice0019.png  # Frame indices preserved
  ```

### IXI T2模态预处理图像 / IXI T2 Preprocessed Images
新增基于IXI数据集的预处理结果（将NIFTI文件转为PNG图像）：  
Newly added high-quality preprocessed data from IXI dataset:

[![Download](https://img.shields.io/badge/Download_IXI_T2_IMG-Google_Drive-important?logo=google-drive&style=flat-square)](https://drive.google.com/file/d/1O53qoZMVbGh0hP1m9nuPoLeSIBU3CU7H/view?usp=sharing)

**核心参数 / Key Specifications**
| 属性                  | 参数值                     | 英文说明                    |
|-----------------------|--------------------------|---------------------------|
| 原始数据集             | IXI-T2                  | Source Dataset: IXI-T2    |
| 病例数量              | 578 cases               | Total Cases: 578          |
| 切片总量              | 11,560 slices           | Total Slices: 11,560       |
| 空间分辨率            | 256×256                 | Spatial Resolution: 256×256|
| 采样策略              | 均匀采样20帧             | Sampling: 20 uniform slices|

**文件结构样例 / File Structure Example**
```bash
IXI-T2-PNG/
├─ IXI01234/
│  ├─ IXI01234_slice_0000.png  # 首帧
│  ├─ IXI01234_slice_0001.png
│  ├──...
│  └─ IXI01234_slice_0019.png  # 末帧
└─ IXI05678/
   ├─ IXI05678_slice_0000.png
   └──...
```
