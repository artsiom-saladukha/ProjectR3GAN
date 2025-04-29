import os
import re
from typing import List, Optional, Union

import click
import dnnlib
import numpy as np
import PIL.Image
import torch

import legacy


def interpolate_model(G,
                      label,
                      z1,
                      z2,
                      num_steps=10):
    with dnnlib.util.open_url(network_pkl) as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device)
    os.makedirs(outdir, exist_ok=True)
    
    label = torch.zeros([1, G.c_dim], device=device)
    if G.c_dim != 0:
        if class_idx is None:
            raise click.ClickException('Must specify class label with --class when using a conditional network')
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print ('warn: --class=lbl ignored when running on an unconditional network')
    
    z1 = torch.from_numpy(np.random.RandomState(1).randn(1, G.z_dim)).to(device)
    z2 = torch.from_numpy(np.random.RandomState(2).randn(1, G.z_dim)).to(device)
    interpolated_images = interpolate_latent_space(G, label, z1, z2, num_steps=10)
    return interpolated_images
