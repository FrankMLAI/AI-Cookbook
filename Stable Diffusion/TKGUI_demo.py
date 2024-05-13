import requests
import base64
import re
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import spacy
import os
import glob
from tkinter import messagebox
import shutil

url = "http://127.0.0.1:7861"
#change to whatever placeholder img you want
foodbot = r"C:\Users\Frank\stable-diffusion-webui-modified\TK\foodbot.png"
nlp = spacy.load('en_core_web_lg')
globalcounter=int(0)
num_ins=int(0)
globalcounter2=int(0)
num_ing=int(0)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Recipe Image Generator')
        self.geometry('1500x1500') 
        
        self.label_text = tk.StringVar()
        self.label_text.set("Let it cook")

        self.ins_button_text = tk.StringVar()
        self.ins_button_text.set("Instructions button")

        self.ing_button_text = tk.StringVar()
        self.ing_button_text.set("Ingredients button")

        firstlabel = tk.Label(self, textvariable=self.label_text)
        firstlabel.pack()
        
        self.python_image = tk.PhotoImage(file=foodbot)
        displayimg = ttk.Label(self, image=self.python_image)
        displayimg.pack()

        recipename = tk.Entry(self, width = 100)
        recipename.insert(0,"Grilled Cheese Sandwich")
        recipename.pack()       

        def nameImgGen():
            pattern=re.compile("[^\w']|_")
            if recipename.get():
                recipe_input = recipename.get()
            
            option_payload = {
                "sd_model_checkpoint": "last-food1000-ep10-gs02490",
            }
            response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

            payload = {
                "prompt": pattern.sub('', recipe_input)+"photorealistic, clear images, highly detailed",
                "negative_prompt": "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature",

            }
            namefolder= r"C:\Users\Frank\stable-diffusion-webui-modified\TK\names"
            foodfname = namefolder + "\\" + recipe_input + ".png"

            # Send said payload to said URL through the API.
            response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
            r = response.json()

            # Decode and save the image.
            with open(foodfname, 'wb') as f:
                f.write(base64.b64decode(r['images'][0]))
            self.python_image = tk.PhotoImage(file=foodfname)
            ttk.Label(self, image=self.python_image).pack()

        nameButton = tk.Button(self, 
                        text = "Recipe Name",  
                        command = nameImgGen)
        nameButton.pack()

        def sentenceSplit(instructions):
            doc = nlp (instructions)
            sentencesplits = [sent.text.strip() for sent in doc.sents]
            return sentencesplits

        recipeinstructions = tk.Entry(self, width = 100) 
        recipeinstructions.insert(0,"Butter the bread on one side and place the bread butter-side down on a hot skillet. Top with cheese, then place another slice of bread on top (butter-side up). Cook until the bottom slice is lightly browned, then flip. Continue cooking until the cheese is melted.")
        recipeinstructions.pack()

        def insImgGen():
            namefolder= r"C:\Users\Frank\stable-diffusion-webui-modified\TK\instructions"
            if recipeinstructions.get():
                ins_input = recipeinstructions.get()
            sentList=sentenceSplit(ins_input)
            sentCounter=0
            pattern=re.compile("[^\w']|_")
            option_payload = {
                "sd_model_checkpoint": "last-food1000-ep10-gs02490",
            }
            response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

            for sent in sentList:
                sentCounter+=1
                payload = {
                    "prompt": pattern.sub('',sent),
                    "negative_prompt": "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature",
                }
                foodfname = namefolder + "\\" + str (sentCounter) + ".png"       

                # Send said payload to said URL through the API.
                response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
                r = response.json()

                # Decode and save the image.
                with open(foodfname, 'wb') as f:
                    f.write(base64.b64decode(r['images'][0]))
                self.python_image = tk.PhotoImage(file=foodfname)
                ttk.Label(self, image=self.python_image).pack()
                
            # for images in os.listdir(namefolder):
            #     imgs.append(ImageTk.PhotoImage(Image.open(r"C:\Users\Frank\stable-diffusion-webui-modified\TK\instructions"+"\\"+images)))
            #     self.python_image = imgs[-1]
            #     ttk.Label(self, image=self.python_image).pack()
            global num_ins 
            num_ins = len([entry for entry in os.listdir(namefolder) if os.path.isfile(os.path.join(namefolder, entry))])
            
            global globalcounter
            globalcounter = 1

            self.label_text.set("image "+str(globalcounter)+" of  "+str(num_ins))
            self.ins_button_text.set("Next instruction")
            insButton.configure(command=next_ins)

            first_ins = r"C:\Users\Frank\stable-diffusion-webui-modified\TK\instructions\1.png"
            self.python_image = tk.PhotoImage(file=first_ins)
            ttk.Label(self, image=self.python_image).pack()
      
        insButton = tk.Button(self, 
                        textvariable = self.ins_button_text,  
                        command = insImgGen) 
        insButton.pack() 

        recipeingredients = tk.Entry(self, width = 100) 
        recipeingredients.insert(0,"Bread. Sliced Cheddar cheese. Butter.")
        recipeingredients.pack()

        def ingImgGen():
            namefolder= r"C:\Users\Frank\stable-diffusion-webui-modified\TK\ingredients" 
            if recipeingredients.get():
                ing_input = recipeingredients.get()
            sentList=sentenceSplit(ing_input)
            sentCounter=0
            pattern=re.compile("[^\w']|_")
            
            option_payload = {
                "sd_model_checkpoint": "last-ingredients4-ep10-gs06340",
            }
            response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

            for sent in sentList:
                sentCounter+=1
                payload = {
                    "prompt": pattern.sub('',sent),
                    "negative_prompt": "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature",
                }
                foodfname = namefolder + "\\" + str (sentCounter) + ".png"       

                # Send said payload to said URL through the API.
                response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
                r = response.json()

                # Decode and save the image.
                with open(foodfname, 'wb') as f:
                    f.write(base64.b64decode(r['images'][0]))
                #self.python_image = tk.PhotoImage(file=foodfname)
                #ttk.Label(self, image=self.python_image).pack()
            
            global num_ing 
            num_ing = len([entry for entry in os.listdir(namefolder) if os.path.isfile(os.path.join(namefolder, entry))])
            
            global globalcounter2
            globalcounter2 = 1

            self.label_text.set("image "+str(globalcounter2)+" of  "+str(num_ing))
            self.ing_button_text.set("Next ingredient")
            ingButton.configure(command=next_ing)

            first_ing = r"C:\Users\Frank\stable-diffusion-webui-modified\TK\ingredients\1.png"
            self.python_image = tk.PhotoImage(file=first_ing)
            ttk.Label(self, image=self.python_image).pack()

        def next_ins():
            global num_ins
            global globalcounter
            if globalcounter==num_ins:
                globalcounter=0

            globalcounter=globalcounter+1
            namefolder= r"C:\Users\Frank\stable-diffusion-webui-modified\TK\instructions"
            foodfname = namefolder + "\\" + str (globalcounter) + ".png"  
            self.python_image = tk.PhotoImage(file=foodfname)
            ttk.Label(self, image=self.python_image).pack()
            self.label_text.set("image "+str(globalcounter)+" of  "+str(num_ins))

        def next_ing():
            global num_ing
            global globalcounter2
            if globalcounter2==num_ing:
                globalcounter2=0

            globalcounter2=globalcounter2+1
            namefolder= r"C:\Users\Frank\stable-diffusion-webui-modified\TK\ingredients"
            foodfname = namefolder + "\\" + str (globalcounter2) + ".png"  
            self.python_image = tk.PhotoImage(file=foodfname)
            ttk.Label(self, image=self.python_image).pack()
            self.label_text.set("image "+str(globalcounter2)+" of  "+str(num_ing))
            
        ingButton = tk.Button(self, 
                        textvariable = self.ing_button_text,  
                        command = ingImgGen) 
        ingButton.pack()  
        
if __name__ == "__main__": 
    app = App()

    def on_closing():
        path1=r"C:\Users\Frank\stable-diffusion-webui-modified\TK\names"
        path2=r"C:\Users\Frank\stable-diffusion-webui-modified\TK\instructions"
        path3=r"C:\Users\Frank\stable-diffusion-webui-modified\TK\ingredients"
        shutil.rmtree(path1)   
        shutil.rmtree(path2)   
        shutil.rmtree(path3)
        os.makedirs(path1)
        os.makedirs(path2)
        os.makedirs(path3)      
        app.destroy()
        
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()