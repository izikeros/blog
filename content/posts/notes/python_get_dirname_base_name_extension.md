---
category: note
date: '2022-02-15'
slug: python-get-file-and-path-parts-dirname-base-name-extension
status: published
tags: base name, dirname, file extension, path, python
title: Python - get file and path parts (dirname, base name, extension)
---
To split the full file name (e.g. `/root/dir/sub/file.ext`) with a path into various parts you can use python built-in functions from the `os` module.
You can retrieve:
- base name - just file name with extension (in our example: `file.ext`)
- file path (in our example: `/root/dir/sub/`)
- core name from the file name (in our example: `file`)
- extension from the file name (in our example: `.ext`)

See the code below:
```python
    import os
    full_file = '/root/dir/sub/file.ext'
    
    # file name with extension 
    basename = os.path.basename(full_file)
    print(f'basename: {basename}')

    # full path to file
    dirname = os.path.dirname(full_file)
    print(f'dirname: {dirname}')

    # extract core name and extension from the filename
    core_name, ext = os.path.splitext(basename)
    print(f'core_name: {core_name}', f'ext: {ext}')
```

Example results:
```python
>>> import os
>>> base=os.path.basename('/root/dir/sub/file.ext')
>>> base
'file.ext'
>>> os.path.splitext(base)
('file', '.ext')
>>> os.path.splitext(base)[0]
'file'
```

**Reference:**
- Stackoverflow - [How to get the filename without the extension from a path in Python?](https://stackoverflow.com/questions/678236)

