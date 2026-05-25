import zipfile
import os
from pathlib import Path

# Create ZIP file
zip_path = 'Capstone_Project_Submission.zip'
project_dir = Path('c:\\Users\\Pc\\Desktop\\Capstone_Project')

# Files to include
files_to_zip = [
    'dataset1.csv',
    'dataset2.csv',
    'notebook.ipynb',
    'process.txt'
]

# Create zip
with zipfile.ZipFile(project_dir / zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        file_path = project_dir / file
        if file_path.exists():
            zipf.write(file_path, arcname=file)
            print(f'Added: {file}')
        else:
            print(f'Warning: {file} not found')

print(f'\nZIP file created: {zip_path}')
if (project_dir / zip_path).exists():
    file_size = os.path.getsize(project_dir / zip_path) / 1024
    print(f'ZIP file size: {file_size:.2f} KB')
    
    # List contents
    print('\nZIP file contents:')
    with zipfile.ZipFile(project_dir / zip_path, 'r') as zipf:
        for info in zipf.filelist:
            print(f'  - {info.filename} ({info.file_size} bytes)')
