
import time
import json
from transformers import pipeline, set_seed
from codecarbon import EmissionsTracker
import os

# Create directories
os.makedirs("outputs", exist_ok=True)
os.makedirs("metrics", exist_ok=True)

PROMPT = "Once upon a time in a forest of AI models, there lived..."
MAX_LENGTH = 100
MODELS = ["distilgpt2", "gpt2"]

results = {}

for model_name in MODELS:
    print(f"\n Generating with {model_name}...")
    set_seed(42)
    generator = pipeline('text-generation', model=model_name)
    tracker = EmissionsTracker(project_name=model_name, output_dir="metrics", output_file=f"{model_name}_emissions.csv")
    tracker.start()

    start_time = time.time()
    generated = generator(PROMPT, max_length=MAX_LENGTH, num_return_sequences=1)
    end_time = time.time()

    tracker.stop()

    generated_text = generated[0]['generated_text']

    with open(f"outputs/{model_name}_output.txt", "w", encoding="utf-8") as f:
        f.write(generated_text)

    results[model_name] = {
        "time_taken_sec": round(end_time - start_time, 3),
        "output_length_tokens": len(generated_text.split()),
        "generated_text": generated_text
    }

# Save metrics
with open("metrics/performance_metrics.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print("\n All generations completed. Check 'outputs/' and 'metrics/' folders.")
