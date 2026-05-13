# ScolioFNN

## Overview
ScolioFNN is a custom Artificial Neural Network implementation built using PyTorch. It is designed to handle custom feedforward logic, manual feature extraction, and iterative weight updates. The project overrides standard PyTorch `nn.Module` behaviors to provide granular control over backpropagation, weight initialization, and the training loop directly within the model class.

## Requirements
To run this model, ensure you have the following installed:
* Python 3.7+
* PyTorch (`torch`, `torchvision`)

## Architecture & Methods

The core of ScolioFNN is built inside the `Model` class, inheriting from `torch.nn.Module`. 

### Key Methods:
* `__init__(self, x, y)`: Initializes the model with input tensors (`x`) and target tensors (`y`).
* `forward(self, learn_x, target_y)`: Defines the forward pass of the network. Initializes weights using Kaiming Normal initialization (`fan_in`, `relu`).
* `passFeatures(self, learn_x)`: Validates input data types and iterates through tensors to append features and initialize standard PyTorch `ParameterList`s.
* `backpropCompute(self, learn_x, target_y)`: A custom implementation of backpropagation utilizing `torch.autograd.grad` to manually compute gradients based on inputs and targets.
* `updateWeights(self, new_x)`: Calculates the Binary Cross Entropy Loss (`BCELoss`) between the newly generated inputs and the target variables.
* `trainModel(self, epoch_num)`: The main training loop. It initializes the linear transformations (`nn.Linear`), applies non-linear activation functions (`ReLU`), and loops through the specified number of epochs to continuously update weights and calculate loss.

## Usage

```python
import torch
from your_module import Model

# Prepare your data
params = [1.0]
x = torch.tensor(params)
y = torch.tensor([0.0]) # Target tensor

# Initialize the model
tst = Model(x, y)

# Train the model (Example: 5 epochs)
tst.trainModel(epoch_num=5)
