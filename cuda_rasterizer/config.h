/*
 * Copyright (C) 2023, Inria
 * GRAPHDECO research group, https://team.inria.fr/graphdeco
 * All rights reserved.
 *
 * This software is free for non-commercial, research and evaluation use 
 * under the terms of the LICENSE.md file.
 *
 * For inquiries contact  george.drettakis@inria.fr
 */

#ifndef CUDA_RASTERIZER_CONFIG_H_INCLUDED
#define CUDA_RASTERIZER_CONFIG_H_INCLUDED

#define NUM_CHANNELS 3 // Default 3, RGB
#define DEFAULT_RASTER_BLOCK_EDGE 16

#ifdef THREEDGS_SLAM_RASTER_BLOCK_EDGE
#define BLOCK_X THREEDGS_SLAM_RASTER_BLOCK_EDGE
#define BLOCK_Y THREEDGS_SLAM_RASTER_BLOCK_EDGE
#else
#define BLOCK_X DEFAULT_RASTER_BLOCK_EDGE
#define BLOCK_Y DEFAULT_RASTER_BLOCK_EDGE
#endif

#endif
