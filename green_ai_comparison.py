# green_ai_comparison.py

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
    emissions_data = getattr(tracker, "final_emissions", None) or getattr(tracker, "_final_emissions_data", None)

    generated_text = generated[0]['generated_text']

    with open(f"outputs/{model_name}_output.txt", "w", encoding="utf-8") as f:
        f.write(generated_text)

    if emissions_data is not None:
        # If emissions_data is a float, treat it as emissions_kg and set energy_kwh to 0.0
        if isinstance(emissions_data, dict):
            energy_kwh = round(emissions_data.get("energy_consumed", 0.0), 6)
            emissions_kg = round(emissions_data.get("emissions", 0.0), 6)
        else:
            energy_kwh = 0.0
            emissions_kg = round(float(emissions_data), 6)
    else:
        energy_kwh = 0.0
        emissions_kg = 0.0

    inference_time = round(end_time - start_time, 3)
    output_quality = len(generated_text)

    results[model_name] = {
        "Energy consumption (kWh)": energy_kwh,
        "CO₂ emissions (kg)": emissions_kg,
        "Inference time (s)": inference_time,
        "Output quality (chars)": output_quality
    }

# Save metrics
with open("metrics/performance_metrics.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print("\n All generations completed. Check 'outputs/' and 'metrics/' folders.")

