from PIL import Image
import numpy as np
from torch import Tensor
from torchvision import transforms

transformer = transforms.Compose([
    transforms.RandomHorizontalFlip(),  # Horizontal flip for augmentation
    transforms.RandomRotation(10),  # Random rotation (between -10 to 10 degrees)
    transforms.RandomAffine(translate=(0.1, 0.1), degrees=30),  # Random translation and rotation (up to 30 degrees)
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),  # Random color jitter
    transforms.RandomResizedCrop(48, scale=(0.8, 1.0)),  # Random crop and resize to 48x48
    transforms.ToTensor(),  # Convert the image to a tensor
    transforms.Normalize(mean=[0.5], std=[0.5]),  # Normalize to [-1, 1]
])


def _make_grayscale(image: Image) -> Image:
    image_array = np.array(image)
    gray_image_array = np.mean(image_array, axis=2).astype(np.uint8)
    return Image.fromarray(gray_image_array)


def transform(image: Image) -> (Image, Tensor):
    if len(np.array(image).shape) > 2 and np.array(image).shape[2] > 1:
        image = _make_grayscale(image)

    return image, transformer(image)
