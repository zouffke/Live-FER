import torch.nn as nn
import torch.nn.functional as F

class FERCNN(nn.Module):
    def __init__(self, num_classes=7):
        super(FERCNN, self).__init__()

        # Convolutional layers to extract features from the input image
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1) # Input: 1 channel (grayscale), Output: 32 channels, 3x3 kernel
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1) # Input: 32 channels, Output: 64 channels, 3x3 kernel
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1) # Input: 64 channels, Output: 128 channels, 3x3 kernel

        # Max pooling layers to downsample the feature maps and reduce computational cost
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0) # Reduces spatial dimensions by half

        # Fully connected layers to perform classification based on the extracted features
        self.fc1 = nn.Linear(in_features=128 * 6 * 6, out_features=256) # Input: flattened feature map, Output: 256 neurons
        self.fc2 = nn.Linear(in_features=256, out_features=num_classes) # Input: 256 neurons, Output: num_classes (e.g., 7 emotions)

        # Dropout layer to prevent overfitting by randomly setting some neurons to zero during training
        self.dropout = nn.Dropout(0.5) # Dropout probability of 0.5

    def forward(self, x):
        # Convolutional and pooling layers with ReLU activation functions
        x = self.pool(F.relu(self.conv1(x))) # Convolution, ReLU activation, then Max Pooling
        x = self.pool(F.relu(self.conv2(x))) # Convolution, ReLU activation, then Max Pooling
        x = self.pool(F.relu(self.conv3(x))) # Convolution, ReLU activation, then Max Pooling

        # Flatten the feature map to feed it into the fully connected layers
        x = x.view(-1, 128 * 6 * 6) # Reshape the tensor: (batch_size, 128 * 6 * 6)

        # Fully connected layers with ReLU activation and dropout
        x = F.relu(self.fc1(x)) # Fully connected layer, ReLU activation
        x = self.dropout(x) # Dropout regularization
        x = self.fc2(x) # Final fully connected layer for classification

        return x