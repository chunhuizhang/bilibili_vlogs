
from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image
prompt = 'a photo of an astronaut riding a horse on mars'

pipeline = StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4',
                                                   use_auth_token=True,
                                                   revision='fp16'
                                                   ).to('cuda')
with autocast('cuda'):
    output = pipeline(prompt)

print(output)
img = output['images'][0]
img.show()
img.save('./output/fp16.png')
