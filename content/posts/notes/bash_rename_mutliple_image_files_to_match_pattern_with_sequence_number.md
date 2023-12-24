---
Category: note
Date: '2023-06-27'
Modified: '2023-07-12'
Slug: bash-rename-mutliple-image-files-to-match-pattern-with-sequence-number
Status: published
Tags: bash, python, bash-script, python-script, alias, image-rename, utility script
Title: Bash - Rename Multiple Image Files to Match Pattern With Sequence Number
---

The use case for the provided script is to rename multiple image files in a directory while maintaining their original file extensions. This script can be handy in situations where you have a collection of image files with different formats or extensions, and you want to standardize their names for better organization or consistency.

By executing the script, all image files with extensions such as `.jpg`, `.jpeg`, `.png`, `.gif`, `.tiff`, `.heic`, and `.heif` in the current directory will be renamed. The new names will follow the pattern "img_xxx.ext", where "xxx" represents a sequence number starting from 000, and "ext" represents the original file extension.

For example, if you have the following image files in the directory:

```
photo1.jpg
picture.png
image2.jpeg
snapshot.tiff
capture.heic
```

Running the script will rename them as:

```
img_000.jpg
img_001.png
img_002.jpeg
img_003.tiff
img_004.heic
```

This allows for consistent naming and easier identification of the image files in the directory.

Here's the Bash script that supports multiple image formats and preserves the original file extension while renaming the files:

```bash
#!/bin/bash

counter=0

for file in *.{jpg,jpeg,png,gif,tiff,heic,heif}; do
    if [[ -f "$file" ]]; then
        extension="${file##*.}"
        newname=$(printf "img_%03d.%s" "$counter" "$extension")
        mv "$file" "$newname"
        ((counter++))
    fi
done
```

In this script:

1. The `for` loop uses brace expansion `{}` to iterate over multiple file extensions: `jpg`, `jpeg`, `png`, `gif`, `tiff`, `heic`, and `heif`.
2. Inside the loop, the script checks if the current file is a regular file using the `-f` test.
3. If it's a regular file, it extracts the original file extension using the `${file##*.}` syntax.
4. The `newname` variable is generated using `printf` with the current value of the `counter` variable and the extracted extension.
5. Finally, the file is renamed using the `mv` command, preserving the original extension.

To use this script, follow these steps:

1. Open a text editor and paste the script into a new file.
2. Save the file with a `.sh` extension, for example, `rename_images.sh`.
3. Open a terminal and navigate to the directory where the image files are located.
4. Make the script executable by running the following command: `chmod +x rename_images.sh`.
5. Run the script using the command `./rename_images.sh`.

After running the script, all the image files in the directory should be renamed according to the pattern you specified.

## Oneliner

Here's a one-liner Bash command that renames all image files in the current directory to match the pattern "img_xxx.jpg" where "xxx" is a sequence number starting from 000:

```bash
counter=0; for file in *.jpg; do if [[ -f "$file" ]]; then newname=$(printf "img_%03d.jpg" "$counter"); mv "$file" "$newname"; ((counter++)); fi; done
```

This command combines the same logic as the previous script into a single line. The `counter` variable is set to 0, and then the `for` loop iterates over the `.jpg` files in the directory. The rest of the logic remains the same.

To use this one-liner, open a terminal, navigate to the directory containing the image files, and run the command. The image files will be renamed accordingly.

To create a Bash alias for the one-liner version of the last script, you can add the following line to your `~/.bashrc` or `~/.bash_aliases` (`.zshrc` or `~/.zsh_aliases` if using zsh) file:

```bash
alias rename_images='counter=0; for file in *.{jpg,jpeg,png,gif,tiff,heic,heif}; do if [[ -f "$file" ]]; then extension="${file##*.}"; newname=$(printf "img_%03d.%s" "$counter" "$extension"); mv "$file" "$newname"; ((counter++)); fi; done'
```

Save the file and then run `source ~/.bashrc` or `source ~/.bash_aliases` to apply the changes.

Afterward, you can use the `rename_images` command in your terminal to execute the one-liner script and rename the image files in the current directory accordingly.

## Python version

Here's a Python script that achieves the same functionality as the Bash script, renaming image files while preserving their original extensions:

```python
import os

counter = 0
extensions = [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".heic", ".heif"]

for filename in os.listdir("."):
    if filename.lower().endswith(tuple(extensions)) and os.path.isfile(filename):
        file_parts = os.path.splitext(filename)
        newname = f"img_{counter:03d}{file_parts[1]}"
        os.rename(filename, newname)
        counter += 1
```

In this Python script:

1. The `counter` variable keeps track of the sequence number for renaming the files.
2. The `extensions` list contains the supported image extensions.
3. The script iterates over each file in the current directory using `os.listdir(".")`.
4. For each file, it checks if the filename has a matching extension and if it is a regular file.
5. If both conditions are satisfied, it extracts the file's extension and uses `os.rename()` to perform the renaming operation.
6. The new name is constructed using the desired pattern "img_xxx.ext", where "xxx" represents the sequence number and "ext" represents the original file extension.
7. Finally, the `counter` is incremented for the next file.

You can save this Python script to a file with a `.py` extension, for example, `rename_images.py`, and then run it using a Python interpreter. The image files in the directory will be renamed accordingly, following the specified pattern while preserving their original extensions.
