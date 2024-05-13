After following the standard Stable Diffusion installation, move the files into the folders.
Move prompts_from_txtfile.py into the scripts folder. 
Move ui.py into the modules folder.
The remaining files can go directly into the root stable diffusion folder, some of them replacing older copies of the same file. 
Running webui.bat opens Stable Diffusion in GUI mode and webui-user.bat opens it in API mode.
A server running in GUI mode is good for utilizing the prompts_from_txtfile.py script to batch generate test prompts.
The prompt_example text files show how the test prompts should be formatted. Some string modification is necessary to reformat our csv into proper prompts. 
A server running in API mode is needed to run our tkinter app, TKGUI.py successfully.
Additionally, the TK folder should also be moved into the Stable Diffusion root for TKGUI.py to work.
