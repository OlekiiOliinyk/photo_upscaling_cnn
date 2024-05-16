import torch 
import cv2
import srcnn
import numpy as np
import glob as glob
import os

from torchvision.utils import save_image

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = srcnn.SRCNN().to(device)
model.load_state_dict(torch.load('../model_info/model.pth'))

image_paths = glob.glob('../user_photos/*')
for image_path in image_paths:
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    test_image_name = image_path.split(os.path.sep)[-1].split('.')[0]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.reshape(image.shape[0], image.shape[1], 1)
    cv2.imwrite(f"../output/original_photos/test_{test_image_name}.png", image)
    print(f"test_{test_image_name}.png saved to /output/original_photos/")
    image = image / 255.
    
    model.eval()
    with torch.no_grad():
        image = np.transpose(image, (2, 0, 1)).astype(np.float32)
        image = torch.tensor(image, dtype=torch.float).to(device)
        image = image.unsqueeze(0)
        outputs = model(image)
        
    outputs = outputs.cpu()
    save_image(outputs, f"../output/upscaled_photos/output_{test_image_name}.png")
    print(f"output_{test_image_name}.png saved to output/upscaled_photos/")