import h5py
import numpy as np
import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm
import tarfile


def unzip_tar(tar_path, extract_dir):
    os.makedirs(extract_dir, exist_ok=True)
    print("正在解压tar文件...")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_dir)


def process_h5_folder(input_folder, output_root, frames_per_file=10):
    """
    处理整个文件夹的h5文件并保存指定帧的MRI图像

    Params：
    input_folder: 输入的h5文件目录
    output_root: 输出图片的根目录
    frames_per_file: 每个文件提取的帧数
    """
    output_path = Path(output_root)
    output_path.mkdir(parents=True, exist_ok=True)
    h5_files = [f for f in os.listdir(input_folder) if f.endswith('.h5')]

    for file_name in tqdm(h5_files):
        file_path = Path(input_folder) / file_name
        case_id = file_name.split('.')[0]
        case_output = output_path / case_id
        case_output.mkdir(exist_ok=True)

        with h5py.File(file_path, 'r') as f:
            kspace = f['kspace'][()]

            total_slices = kspace.shape[0]
            selected_indices = np.linspace(0, total_slices - 1, frames_per_file, dtype=int)

            for i, slice_idx in enumerate(selected_indices):

                kspace_slice = kspace[slice_idx]

                k_shift = np.fft.ifftshift(kspace_slice, axes=(-2, -1))
                image = np.fft.ifft2(k_shift)
                image_shift = np.fft.fftshift(image)

                img_abs = np.abs(image_shift)
                img_norm = (img_abs / np.percentile(img_abs, 99) * 255).clip(0, 255).astype(np.uint8)

                save_path = case_output / f"{case_id}_slice{slice_idx:04d}.png"
                Image.fromarray(img_norm).save(save_path)


if __name__ == "__main__":
    # An example
    unzip_tar(
        tar_path="/root/knee_singlecoil_val.tar.xz",
        extract_dir="/root/"
    )
    process_h5_folder(
        input_folder="/root/singlecoil_val/",
        output_root="/root/fastmri_test_images/",
        frames_per_file=20
    )
