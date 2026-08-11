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


RASTER_BLOCK_EDGE_ENV = "THREEDGS_SLAM_RASTER_BLOCK_EDGE"


def raster_block_edge_compile_args():
    """Select an explicitly requested native tile edge without changing defaults."""
    value = os.environ.get(RASTER_BLOCK_EDGE_ENV)
    if value is None:
        return []
    try:
        edge = int(value)
    except ValueError as error:
        raise RuntimeError(f"{RASTER_BLOCK_EDGE_ENV} must be a positive integer") from error
    if edge <= 0:
        raise RuntimeError(f"{RASTER_BLOCK_EDGE_ENV} must be a positive integer")
    return [f"-D{RASTER_BLOCK_EDGE_ENV}={edge}"]


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

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
            extra_compile_args={
                "nvcc": ["-I" + os.path.join(PROJECT_ROOT, "third_party/glm/")]
                + raster_block_edge_compile_args()
            })
        ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
