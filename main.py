import os
from export import export_frame
from post import post_images

def select_export() -> None:
    filename = input("Enter filename: ")
    outdir = input("Enter output directory path: ")

    if not filename or filename.isspace():
        print("Please input the filename of the video!")
        return

    if not outdir or outdir.isspace():
        print("Please input the output directory!")
        return

    export_frame(filename, outdir)

def select_post() -> None:
    foldername = input("Enter directory folder: ")

    if not foldername or foldername.isspace():
        print("Please enter foldername!")
        return

    post_images(foldername)

def main() -> None:
    while True:
        choice = input("Select 'export', 'post', or 'exit': ")

        if choice.lower() == "export":
            select_export()
        elif choice.lower() == "post":
            select_post()
        elif choice.lower() == "exit":
            break
        else:
            print("Input not found in the list.")

if __name__ == "__main__":
    main()