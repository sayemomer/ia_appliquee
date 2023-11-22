import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(128 * 6 * 6, 256)
        self.fc2 = nn.Linear(256, 10)  # Assuming we have 10 classes

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 6 * 6)  # Flatten the tensor
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    

from torchviz import make_dot

# Create a dummy input tensor appropriate for the input dimensions
dummy_input = torch.randn(1, 3, 48, 48, requires_grad=True)

# Create an instance of the model
model = SimpleCNN()

# Perform a forward pass to get the output
output = model(dummy_input)

# Visualize the graph
vis_graph = make_dot(output, params=dict(list(model.named_parameters()) + [('input', dummy_input)]))
vis_graph.view()  # This will render the graph and open it in a viewer

