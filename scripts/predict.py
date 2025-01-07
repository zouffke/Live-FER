from FER_CNN import FERCNN
import torch
import torch.nn.functional as F

from emotions import emotions

model_path = 'model/model.tar'


def _convert_softmax(output, dim=1):
    probabilities = F.softmax(output, dim=dim)
    percentages = probabilities.squeeze().cpu().numpy() * 100
    # Print the percentages
    outputs = {}
    for emotion, percentage in zip(emotions, percentages):
        outputs[emotion] = percentage

    return outputs

def predict(image):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    model = FERCNN().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))

    model.eval()
    with torch.no_grad():
        output = model(image.to(device))
        _, predicted = torch.max(output, 1)

    predicted_emotion = emotions[predicted.item()]

    return predicted_emotion, _convert_softmax(output)
