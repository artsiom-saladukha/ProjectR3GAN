# ProjectR3GAN
This repository contains the implementation of the R3-GAN pipeline from the paper "The GAN is dead; long live the GAN! A Modern Baseline GAN".
As well as the results of various experiments related to it.

Link to the source article: https://arxiv.org/abs/2501.05441
Link to the source code: https://github.com/brownvc/R3GAN

## Getting Started
These instructions will give you a hint on how to install and run our R3GAN replica, as well as additional information on this repo insights.

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
