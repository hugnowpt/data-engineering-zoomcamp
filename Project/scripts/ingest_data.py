import kagglehub
import shutil
import os

# download
path = kagglehub.dataset_download("noahtaylson/elite-retail-transaction-dataset-uk")

print("Downloaded to:", path)

# target folder
target_dir = "data"

# create folder if not exists
os.makedirs(target_dir, exist_ok=True)

# copy files to data/
for file_name in os.listdir(path):
    source_file = os.path.join(path, file_name)
    target_file = os.path.join(target_dir, file_name)
    
    shutil.copy(source_file, target_file)

print("Files copied to data/ folder")