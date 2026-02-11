# src/dataset.py

import os

def load_image_paths(path):

    # Caso 1: es un archivo
    if os.path.isfile(path):
        return [path]

    # Caso 2: es una carpeta
    elif os.path.isdir(path):
        image_paths = []

        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith((".jpg", ".jpeg", ".png")):
                    image_paths.append(os.path.join(root, file))

        return image_paths

    else:
        raise ValueError(f"Invalid path: {path}")

