import os

import torch

from torch import nn
from torchvision import models
from torchvision import transforms

from PIL import Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Connected device with", device)

imageTransformer = transforms.Compose(
    [
        transforms.Resize((256, 256)),
        transforms.CenterCrop((150, 150)),
        transforms.ToTensor(),
        transforms.Normalize([0.5] * 3, [0.5] * 3),
        transforms.Resize((256, 256))
    ]
)

class Model():
    def __init__(self, model, weights):
        self.model = model
        self.weights = BASE_DIR + "/Data"  + "/" + weights

        self.load = False
    
    def __call__(self, image):
        return self.predict(image)

    def ready(self):
        if(not self.load):
            try:
                self.model.load_state_dict(torch.load(self.weights, map_location=device))
                self.model.eval()
                print("Successfully load weights.")
            except Exception as e:
                print(e)
            finally:
                self.load = True
    
    def predict(self, image):
        self.ready()
        x = imageTransformer(Image.open(image).convert('RGB')).reshape(1, 3, 256, 256)
        y = self.model(torch.FloatTensor(x).to(device))
        return y.argmax(dim=1,keepdim=True)


model = {
    "resnet18": Model(models.resnet18(pretrained=False).to(device), "resnet18.pt"),
    "resnet50": Model(models.resnet50(pretrained=False).to(device), "resnet50.pt"),
    "efficientnet_b0": Model(models.efficientnet_b0(pretrained=False).to(device), "efficientnetb0.pt")
}

model["resnet18"].model.fc = nn.Linear(512, 2).to(device)
model["resnet50"].model.fc = nn.Linear(2048, 2).to(device)
model["efficientnet_b0"].model.classifier[1] = nn.Linear(1280, 2).to(device)