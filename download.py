import requests
import zipfile
import os
from tqdm import tqdm

url = "https://huggingface.co/datasets/nuwandaa/ffhq128/resolve/main/thumbnails128x128.zip"
zip_filename = "thumbnails128x128.zip"
extract_folder = "images"

print(f"Connecting to Hugging Face...")

response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open(zip_filename, 'wb') as file, tqdm(
    desc="Downloading",
    total=total_size,
    unit='iB',
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for data in response.iter_content(chunk_size=1024):
        size = file.write(data)
        bar.update(size)

print(f"\nDownload complete! Saved as {zip_filename}.")
print(f"Extracting images to ./{extract_folder}/ ...")
os.makedirs(extract_folder, exist_ok=True)

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("All done! Your dataset is ready.")