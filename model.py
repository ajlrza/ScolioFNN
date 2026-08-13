# Feedforward Neural Network Class
class Net(nn.Module):
    
    def __init__(self, x, y) -> None:
        super().__init__()
        self.input_x = torch.tensor(x)
        self.target_y = torch.tensor(y)

    # Forward pass function in every iteration
    def forward(self, learn_x: torch.tensor, target_y: torch.tensor) -> None:
        self.learn_x = learn_x
        self.target_y = target_y
        
        self.weight_initialize = nn.init.kaiming_normal_(self.learn_x.weight, mode="fan_in", nonlinearity='relu')
        self.initial_weight = nn.ParameterList([self.weight_initialize])
        
        return self.initial_weight

    # Feed X into Input Layer
    def pass_features(self, learn_x: torch.tensor):
        self.x_features = []
        
        if (type(learn_x) != torch.tensor):
            print("Incompatible data types, use torch.tensor")
            
        if (torch.is_tensor(learn_x)):
            for column in learn_x:
                self.x_features.append(column)

            for param in learn_x:
                self.x_rows = nn.ParameterList([nn.Parameter(param)])


    # Backpropagation Algorithm
    def backprop_compute(self, learn_x: torch.tensor, target_y: torch.tensor):
        self.learn_x = learn_x
        self.target_y = target_y
        
        backprop = torch.autograd.grad(self.target_y, self.target_x)
        return backprop
    
    # Updating weights in every iteration
    def update_weights(self, new_x: torch.tensor):
        # Weights corresponding to each tensor
        self.weights = self.initial_weight

        self.new_x = new_x
        self.old_x = input_x
 
        self.get_loss = nn.BCELoss(weight=self.weights)
        self.loss = self.get_loss(new_x, self.target_y)
        return self.loss    
        
    # View parameters
    def print_params(self):
        print(self.params)
        
    # Train the model method
    def train_model(self, epoch_num):
        
        # Initialize the training epochs
        self.epochs = epoch_num
        
        # Initialize prediction output value
        self.output = None

        # Create the neurons of the model
        self.neuron_list = []

        # Algorithm for determining in and output features in nn.Linear
        self.in_features = self.neurons[]

        self.linear_neuron = nn.Linear(20, 30, bias=True)

        if (len(self.input_x) != neuronLinear.size()):
            raise Exception(f"Size of input x must be same as {neuronLinear.size()}")

        # Apply linear transformations
        for i in range(self.neurons):
            self.apply_linear = self.neuron_linear(self.input_x)
            self.neuron_list.append(self.apply_linear)

        # Apply non-linear functions and train
        for i in range(self.epochs):
            
            self.output = f.relu(torch.tensor(self.neuron_list))
            self.neuron_list.append(self.output)

            self.compute = backprop_compute(self.output)
            self.loss = update_weights(self.compute)
            
            print(f"Training loss: {self.loss}")
            print(self.compute)

    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 
