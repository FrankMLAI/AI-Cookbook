import torch
from torchmetrics.functional.multimodal import clip_score
from functools import partial
from PIL import Image
import numpy as np
import os

my_file = open(r"C:\Users\Frank\stable-diffusion-webui-modified\CLIP\Ingset\ing1000.txt", encoding="utf-8")
prompts = my_file.read().splitlines()

mypath=r"C:\Users\Frank\stable-diffusion-webui-modified\CLIP\Ingset\Ing1000"
def load_dataset( ) :
    data =[]
    for fname in os.listdir(mypath):
        pathname = os.path.join(mypath, fname)
        img = Image.open(pathname)
        a = np.asarray(img)
        data.append(a)
    return data
data= load_dataset()
images = np.stack(data, axis=0)

clip_score_fn = partial(clip_score, model_name_or_path="openai/clip-vit-base-patch16")

def calculate_clip_score(images, prompts):
    images_int = (images * 255).astype("uint8")
    clip_score = clip_score_fn(torch.from_numpy(images_int).permute(0, 3, 1, 2), prompts).detach()
    return round(float(clip_score), 4)

sd_clip_score = calculate_clip_score(images, prompts)
print(f"CLIP score: {sd_clip_score}")

# from torchmetrics.multimodal.clip_score import CLIPScore
# metric = CLIPScore(model_name_or_path="openai/clip-vit-base-patch16")
# values = [ ]
# for x, y in zip(images, prompts):
#     values.append(metric(x, y))
# fig_, ax_ = metric.plot(values)