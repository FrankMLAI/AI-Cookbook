## AI Cookbook
### Short Abstract
The cookbook takes in a recipe input (food name, instructions, and ingredients list) and generates depictions using multiple fine-tuned Stable Diffusion models.
Tuning is handled by Everydream2 and the CLIP score evaluation is handled by Pytorch. End-user functionality is enabled through the TKGUI.py file.

### Instructions
Install Automatic1111's Stable Diffusion 1.5 (https://github.com/AUTOMATIC1111/stable-diffusion-webui/) and install victorchall's Everydream2trainer (https://github.com/victorchall/EveryDream2trainer)
Copy the files from our various folders into where they are instructed to be kept. Such instructions and detailed usage guidelines will be included inside individual readme's inside of each folder.
Separate your image datasets into testing and training sets along with their corresponding prompts. 

### Tuning
Divide your training set into quantities that will not overload your VRAM (250 seems to be the limit for VRAMS of 12GB).
Perform tuning in iterations until the entire training set has been ingested.
Move the outputted "last" checkpoints into your "stable-diffusion-webui\models\Stable-diffusion" folder.
Alternatively, our tuned models can be found at https://huggingface.co/FrankML/AI-Cookbook-Tuned-Models
You will need to tune for both foodnames and ingredients for full utility.

### Image generation & CLIP
Start up Stable Diffusion using webui.bat. This should open up a standard SD GUI.
You can utilize the "prompts_from_txtfile.py" script to generate a batch of images. This is important for CLIP testing.
Input both the generated images as well as the prompts utilized to generate them into the "Clip.py" script. 
This is a computationally intensive task that might require you to split up your images into batches of 100 (with a VRAM of 12GB).

### TKGUI
Start up Stable Diffusion using webui-user.bat. This will start up SD in API mode.
Run TKGUI in a separate terminal.
The buttons & functions are self explanatory but some clicking will be required to iterate through all of the ingredient/instructions iterations.

Complete and proper setup will result in a folder size of approximately 81GB (after tuning).

For more detailed information and instructions, please see the individual readme's in each folder within the source code zip.
