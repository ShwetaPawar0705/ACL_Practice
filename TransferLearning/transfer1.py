import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms
import kagglehub

num_classes = 20
batch_size = 32
num_epochs = 3
learning_rate = 0.001

# Data transformations
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# Load Datasets
data_dir = kagglehub.dataset_download("crawford/20-newsgroups")
