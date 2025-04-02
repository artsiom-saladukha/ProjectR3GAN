# ProjectR3GAN
This repository contains the implementation of the R3-GAN pipeline from the paper "The GAN is dead; long live the GAN! A Modern Baseline GAN".
As well as the results of various experiments related to it.

Link to the source article: https://arxiv.org/abs/2501.05441
Link to the source code: https://github.com/brownvc/R3GAN

## Getting Started
These instructions will give you a hint on how to install and run our R3GAN replica, as well as additional information on this repo insights.

### Negative Results and Future Work (original article)
* Researchers tried to apply GELU, Swish, and SMU to G and D and found that doing
so worsened FID considerably. In the context of GANs, GELU and Swish have the same problem as ReLU: that they
have little gradient in the negative interval. Since G is updated from the gradient of D,
having these activation functions in D could sparsify the gradient of D and as a result
G will not receive as much useful information from D compared to using leaky ReLU. 
This does not explain the strange case of SMU: SMU is a smooth approximation of
leaky ReLU and does not have the sparse gradient problem. It is unclear why it also underperformed.

* Researchers tried adding group normalization to G and D and it did not improve FID or training
stability. However in EDM2 (the strongest diffusion UNet) the normalization is applied to the trainable weights
and this improves performance considerably. It is expected that applying the normalization
techniques in EDM2 would improve this model’s performance.

* Reseachers tried scaling up the model size. They found that allocating more model capacity to
lower resolution stages generally did not improve FID, but contributed to more rapid
overfitting. Increasing model capacity at higher resolution stages improved FID in experiments.
Capacity distribution for each resolution stage of the model is an important topic to be explored further.

* Researchers experimented with Adam β2 = 0.999 and found that doing so led to stability issues on ImageNet models.
They expect that introducing proper normalization to the model will resolve this problem.

* Researchers tried lazy regularizatio in early experiments where R1 and R2 were applied
once every 8 minibatches. This led to slightly worse FID performance on real world datasets
like FFHQ and CIFAR-10. However, it resulted in complete convergence failure on Stacked
MNIST and several two dimensional toy datasets (line, circle, 25 Gaussians, etc.), indicating
potential concerns regarding the mathematical legitimacy of this trick.

* Researchers tried mixed precision training with IEEE FP16 (was used in StyleGAN2-ADA, StyleGAN3, and EDM2). 
This worsened the model training (switching to BFloat16 (less precise) fixed the problem).
It is expected that introducing proper normalization to the model will allow to use IEEE FP16.

* Researchers didn't conduct any experiment with a transformer architecture/attention mechanism in general.
We are interested to see whether adding attention blocks to a convolutional network (BigGAN, diffusion UNet) or
using a pure transformer architecture (DiT) will result in stronger performance, given the impressive results of EDM2 (UNet).

* Researchers tried removing the activation function after the 3×3 grouped convolution in each residual
block as modern architectures typically do not apply non-linearity after depthwise convolution. This worsened FID performance

* Researchers tried Pixel-Shuffle/Unshuffle for changing the resolution of the activation maps and found that without low-pass filtering,
this led to high frequency artifacts similar to checkerboard artifacts even though Pixel-Shuffle does not have the uneven overlap problem
that transposed convolution does. Note that bilinear resampling is equivalent to applying channel duplication/averaging
with Pixel-Shuffle/Unshuffle in conjunction with a low-pass kernel. 
It might be interesting in future studies to explore inplace resampling filters that apply a low-pass filtered Pixel-Shuffle/Unshuffle operation 
on top of a learned function that changes the number of channels.


### Short summary on what this research covers:
* Replicate the results described in the article;
* Experiment with different image output sizes and check how quality of it changes with increase;
* Experiment with different ad-hoc techniques used in classic GAN modifications to determine how well do they fit this architecture;
* Experiment with style-injection;
* Experiment with conditional generation, explore the latent space of generator.

### Installing the packages
Download and install the package using package installer for Python (in the official R3-GAN repo it is mentioned that they ran all pipelines with StyleGAN3-needed packages only):

	$ conda env create -f environment.yml
	$ conda activate env_r3gan

### Running the training pipeline
NOT IMPLEMENTED YET

The training process can be initiated with the following line (after you successfully installed the package):
	
 	(env_r3gan) $ python training.py

### Generating a sample
NOT IMPLEMENTED YET

To receive the generated image sample write the following line: 

	(env_r3gan) $ python generate.py


## Authors
  - **Artsiom Saladukha** - [artsiom-saladukha](https://github.com/artsiom-saladukha)
  - **Daniil Domnin** - [DaniilDomnin](https://https://github.com/DaniilDomnin)
