import torch
import os
import numpy as np
import typing, types
import torch.optim # for optimizers
import torch.nn as nn # for neural network modules
from typing import override
import torch.nn.functional as f # for non-linear function
from torch.utils.data import DataLoader, Dataset # for data handling

    
# Feedforward Neural Network Class
class Net(nn.Module):
    
    def __init__(self, input: int, target: int, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()

        self.x = torch.tensor(input)
        self.y = torch.tensor(target)

        self.input_layer: np.ndarray = np.array(prec)

    # Forward pass to input layer
    def __forward(self, x: torch.Tensor) -> torch.Tensor:
        
        weighted_x = nn.init.kaiming_normal_(self.learn_x, mode="fan_in", nonlinearity='relu')
        
        return weighted_x


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)
    
    def __update_weights(self, weighted_x: torch.Tensor):
 
        return nn.BCELoss(weight=weighted_x)
        
    def params(self):
        print(self.x)

    def train(self, epoch_num):

        self.linear_transform = nn.Linear(self.__forward(self.x), self.y)
        self.epochs = epoch_num
        self.output = None
        self.neuron_list = []
        self.in_features = self.neuron_list

        self.linear_neuron = nn.Linear(20, 30, bias=True)

        if (len(self.input_layer) != self.linear_neuron.size()):
            raise Exception(f"Size of input x must be same as {self.linear_neuron.size()}")

        for i in range(self.neuron_list):
            self.apply_linear = nn.Linear(self.x)
            self.neuron_list.append(self.apply_linear)

        for i in range(self.epochs):
            
            output = f.relu(torch.tensor(self.neuron_list))
            self.neuron_list.append(self.output)

            compute = self.__backprop(output)
            loss = self.__update_weights(compute)
            
            print(f"Training loss: {loss}")
            print(compute)

    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 
