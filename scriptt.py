import os

folders = [
    "data/raw",
    "data/processed",
    "data/embeddings",
    "models",
    "api",
    "dashboard/components",
    "scripts",
    "utils",
    "configs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("✅ Folder structure created successfully!")
