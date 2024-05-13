These files should be moved into your Everydream2 folder.
Detailed ED2 installation instructions can be found on https://www.youtube.com/watch?v=OgpJK8SUW3c
Run windows_setup.cmd
Run activate_venv
You will need to move a copy of the default SD checkpoint "v1-5-pruned-emaonly.safetensors" into your checkpoints folder.
Edit the basemodelcmd.txt to your configuration and copy and run it in your venv. This is to set up your initial checkpoint for tuning.
Split up your tuning imagesets into smaller chunks as to avoid computational bottlenecks.
1000select.py is a script for splitting 1000 images into 250 but can easily be altered to suit your computational capacity.
Utilize the filename2txt_number_remove.py to label your image folders in a way that is similar to the tuning_txt_setup.png
Edit the modeltrainingcmd.txt to your configuration and copy and run it for each tuning iteration.
The first run should always be with --resume_ckpt "my_sd15_model".
When it finishes, it should output multiple safetensor files along with their corresponding "log" folder entries. Only the one labeled with "last" is needed as that is final checkpoint generated.
Replace the --resume_ckpt "my_sd15_model" with something that looks like --resume_ckpt "logs\first_iteration\ckpts\last-first_iteration", using the path of the "last" log folder.
Repeat this process until all images have been ingested into the tuned model for both the foodnames and ingredients datasets.
Collect the outputted safetensors and move them into your Stable Diffusion "models/stable-diffusion" folder.
Our outputs are in the Tuned Models folder.