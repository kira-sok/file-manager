# File Organizer

A Python script that automatically sorts files in the "Downloads" directory by type into subfolders.

## What it does

Scans a folder and moves files into categorized subfolders:

| Folder    | Extensions                                      |
|-----------|-------------------------------------------------|
| Images    | .jpg, .jpeg, .png, .gif, .bmp, .webp            |
| Documents | .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt |
| Archives  | .zip, .rar, .7z, .tar, .gz                      |
| Music     | .mp3, .wav, .flac                               |
| Video     | .mp4, .mov, .avi                                |
| Code      | .py, .js, .html                                 |
| Other     | everything else                                 |

## Usage

By default, the script organizes your `~/Downloads` folder.

```python
# To organize Downloads:
organize(path)

# To revert everything back:
unorganize(path)

# To organize a custom folder:
organize("/path/to/folder")
```

## Technologies

- Python 3.10+
- `os` - working with the file system
- `shutil` - moving files
