from src.dataset import load_image_paths
from src.pipeline import NavigationPipeline
from tqdm import tqdm
import json

#DATA_PATH = "data/bdd100k_images_10k/10k/test/b6579e76-e88b8169.jpg"
DATA_PATH = "data/bdd100k_images_10k/10k/test/bc88fd46-c20fe7dd.jpg"

pipeline = NavigationPipeline()
image_paths = load_image_paths(DATA_PATH)

#results = []

output = pipeline.run_on_image(DATA_PATH)

#for img_path in tqdm(image_paths[:50]):  # limit for testing
#    output = pipeline.run_on_image(img_path)
#    output["image"] = img_path
#    results.append(output)

with open("results/logs.json", "w") as f:
    json.dump(output, f, indent=4)
