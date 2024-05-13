import glob
import os
import argparse

def create_txt_from_filename(path):

    print(f"Creating .txt files from filenames in {path}")
    for idx, f in enumerate(glob.iglob(f"{path}/**", recursive=True)):
        print(f"Creating {f}.txt")
        if not os.path.isfile(f) or not os.path.splitext(f)[1] in ['.jpg', '.png', '.jpeg', '.webp', '.bmp']:
            continue

        path_without_filename = os.path.dirname(f)
        base_name = os.path.splitext(os.path.basename(f))[0]
        #caption = os.path.splitext(base_name)[0].split("_")[0]
        caption = os.path.basename(os.path.normpath(path_without_filename))
        target = f"{path_without_filename}/{base_name}.txt"
        print (f"Creating file: {target} from {f}")
        with open(target, "w") as text_file:
            text_file.write(caption)

if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--path", type=str, help="path to folder")
    #parser.add_argument(r"C:\Users\Frank\EveryDream2trainer\250_1")
    #args = parser.parse_args()
    #create_txt_from_filename(args.path)
    create_txt_from_filename(r"C:\Users\Frank\stable-diffusion-webui-modified\EveryDream2trainer\ingredients")