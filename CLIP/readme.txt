You can move the CLIP folder directly into "C:\Users\Frank\stable-diffusion-webui-modified"
Set up your input images folder and input prompts as depicted in the "CLIP folder setup.PNG" and the CLIP txt examples folders.
The txt files examples in the folder have had their CLIP scores appended to their filenames after completion, but such is not necessary for the intial setup.
Disclaimer: CLIP scoring, as implemented by Pytorch, only accepts images of the same size.
This is not an issue for CLIP scoring the generated images, but it does present issues for many training sets.
Luckily our Kaggle dataset had image size consistency.