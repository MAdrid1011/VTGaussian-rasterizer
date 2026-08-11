#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os
os.path.dirname(os.path.abspath(__file__))

nvcc_args = ["-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")]
block_edge = os.environ.get("THREEDGS_SLAM_RASTER_BLOCK_EDGE")
if block_edge is not None:
    try:
        block_edge = int(block_edge)
    except ValueError as error:
        raise RuntimeError("THREEDGS_SLAM_RASTER_BLOCK_EDGE must be an integer") from error
    if block_edge <= 0:
        raise RuntimeError("THREEDGS_SLAM_RASTER_BLOCK_EDGE must be positive")
    nvcc_args.extend([f"-DBLOCK_X={block_edge}", f"-DBLOCK_Y={block_edge}"])

setup(
    name="diff_gaussian_rasterization",
    packages=['diff_gaussian_rasterization'],
    ext_modules=[
        CUDAExtension(
            name="diff_gaussian_rasterization._C",
            sources=[
            "cuda_rasterizer/rasterizer_impl.cu",
            "cuda_rasterizer/forward.cu",
            "cuda_rasterizer/backward.cu",
            "rasterize_points.cu",
            "ext.cpp"],
            extra_compile_args={"nvcc": nvcc_args})
        ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
