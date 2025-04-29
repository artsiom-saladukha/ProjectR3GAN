import os
import re
from typing import List, Optional, Union

import click
import dnnlib
import numpy as np
import PIL.Image
import torch

import legacy


def interpolate_latent_space(G,
                             label,
                             z1,
                             z2,
                             num_steps=10):
    alphas = torch.linspace(0, 1, num_steps)
    interpolated_images = []

    for alpha in alphas:
        z_interpolated = alpha * z1 + (1 - alpha) * z2
        z_interpolated = z_interpolated.to('cuda')
        with torch.no_grad():
            image = G(z_interpolated, label)
            interpolated_images.append(image)
    return interpolated_images


@click.command()
@click.option('--network', 'network_pkl', help='Network pickle filename', required=True)
@click.option('--outdir', help='Where to save the output images', type=str, required=True, metavar='DIR')
def interpolate_model(network_pkl,
                      outdir,
                      num_steps=10):
    device = 'cuda'
    with dnnlib.util.open_url(network_pkl) as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device)
    os.makedirs(outdir, exist_ok=True)
    
    label = torch.zeros([1, G.c_dim], device=device)
    class_idx = 0
    if G.c_dim != 0:
        if class_idx is None:
            raise click.ClickException('Must specify class label with --class when using a conditional network')
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print ('warn: --class=lbl ignored when running on an unconditional network')
    
    z1 = torch.from_numpy(np.random.RandomState(0).randn(1, G.z_dim)).to(device)
    z2 = torch.from_numpy(np.random.RandomState(42).randn(1, G.z_dim)).to(device)
    
    interpolated_images = interpolate_latent_space(G, label, z1, z2, num_steps=10)
    for idx, image in enumerate(interpolated_images):
        image = (image.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
        PIL.Image.fromarray(image[0].cpu().numpy(), 'RGB').save(f'{outdir}/{idx}.png')
    return interpolated_images


if __name__ == "__main__":
    interpolate_model()
