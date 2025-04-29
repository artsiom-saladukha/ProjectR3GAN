# ProjectR3GAN
This repository contains the implementation of the R3-GAN pipeline from the paper "The GAN is dead; long live the GAN! A Modern Baseline GAN".
As well as the results of various experiments related to it.

There is a widely-spread claim that GANs are difficult to train, and GAN architectures in the literature are littered with empirical tricks.
The R3GAN research provide evidence against this claim and build a modern GAN baseline in a more principled manner.
First, researchers derive a well-behaved regularized relativistic GAN loss that addresses issues of mode dropping and non-convergence that were previously tackled via a bag of ad-hoc tricks.
The loss is analyzed mathematically and it is proven that it admits local convergence guarantees, unlike most existing relativistic losses. 
Second, new loss allows to discard all ad-hoc tricks and replace outdated backbones used in common GANs with modern architectures.
Using StyleGAN2 as an example, the roadmap of simplification and modernization presented that results in a new minimalist baseline -- R3GAN.
Despite being simple, it surpasses StyleGAN2 on FFHQ, ImageNet, CIFAR, and Stacked MNIST datasets, and compares favorably against SOTA GANs and even diffusion models.

"The relativistic discriminator: a key element missing from standard GAN" is the article in which principles used in R3GAN pipeline are described.
Primarily the new approach to objective function.

Link to the source article (can also be found within the repo (r3gan_article.pdf)):

https://arxiv.org/abs/2501.05441

Link to the relativistic GAN loss article (can also be found within the repo (rel_discr_article.pdf)):

https://arxiv.org/abs/1807.00734 

Link to the source code:

https://github.com/brownvc/R3GAN

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

Short summary on what this research covers:
* Replicate the results described in the article;
* Experiment with different ad-hoc techniques used in classic GAN modifications to determine how well do they fit this architecture;
* Experiment with conditional generation, explore the latent space of generator.

### Installing the packages
Download and install the packages (in the official R3-GAN repo it is mentioned that they ran all pipelines with StyleGAN3-needed packages only, we encountered a problemm that not all needed packages were listed).
All experiments were completed within the Google Colab and Kaggle environment. All Jupyter-notebooks include complete installation pipeline.

## Contribution
Artsiom Saladukha:
* Latent space interpolation exploration (pre-trained and CIFAR-trained models);
* GAN backbone complexity reduction research;
* Traditional GAN ad-hoc techniques research and adaptation;

Daniil Domnin:
* Article results replication;
* GAN backbone complexity reduction research;
* Latent space interpolation enforcement methods research;

## Authors
  - **Artsiom Saladukha** - [artsiom-saladukha](https://github.com/artsiom-saladukha)
  - **Daniil Domnin** - [DaniilDomnin](https://https://github.com/DaniilDomnin)
