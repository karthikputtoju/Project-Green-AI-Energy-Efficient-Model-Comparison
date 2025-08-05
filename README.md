![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-ML-brightgreen?style=flat&logo=tensorflow)
![Generative AI](https://img.shields.io/badge/Generative%20AI-Green%20AI%20Project-orange?style=flat&logo=openaigym)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

# Green AI – Energy Efficient Model Comparison

This project demonstrates a real-world application of **Green AI** by comparing two popular Hugging Face models:

- **DistilGPT2** – A lightweight, distilled version of GPT2, optimized for speed and energy efficiency.  
- **GPT2** – The original large-scale transformer model by OpenAI.

---

## Objective

To **quantify and compare**:

- **Energy consumed**
- **CO₂ emissions**
- **Generation time**
- **Output length**

…while generating the same prompt using both models.

---

## Why Green AI?

AI workloads consume increasing amounts of **energy** and produce **CO₂ emissions**.  
Green AI focuses on **sustainable AI practices** by:

- Reducing model size
- Optimizing computation
- Tracking environmental impact

This project **proves** that smaller models can often give **similar results** while having a lower **carbon footprint**.

---

## Project Structure

```
green-ai-model-comparison/
├── README.md
├── requirements.txt
├── green_ai_comparison.py # Main script
├── outputs/ # Generated text outputs
│ ├── distilgpt2_output.txt
│ └── gpt2_output.txt
├── metrics/ # Performance & emissions metrics
│ ├── distilgpt2_emissions.csv
│ ├── gpt2_emissions.csv
│ └── performance_metrics.json
│ └── chart.py
```

##  Installation & Setup

1️⃣ **Clone this repo**
```bash
git clone https://github.com/karthikputtoju/green-ai-model-comparison.git
cd green-ai-model-comparison
```

2️⃣ Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3️⃣ Install dependencies
```
pip install -r requirements.txt

```
Note: If any challenges faced, install respective packages manually.

▶️ Run the Comparison
```
python green_ai_comparison.py

```
This will:
- Run DistilGPT2 & GPT2 on the same prompt
- Track energy usage, CO₂ emissions, and inference time with CodeCarbon

Save:
- Generated text → outputs/
- Metrics in JSON & CSV → metrics/
- Color-coded performance chart → metrics/

## Example Results
metrics/performance_metrics.json:
```
{
    "distilgpt2": {
        "Energy consumption (kWh)": 0.0,
        "CO₂ emissions (kg)": 9.9e-05,
        "Inference time (s)": 14.182,
        "Output quality (chars)": 1214
    },
    "gpt2": {
        "Energy consumption (kWh)": 0.0,
        "CO₂ emissions (kg)": 7.1e-05,
        "Inference time (s)": 10.274,
        "Output quality (chars)": 1280
    }
}
```

## Visual Comparison
- 🟢 Good – Best performer for that metric
- 🟧 Better – Mid performer
- 🔴 Bad – Lowest performer
<img width="1886" height="1060" alt="image" src="https://github.com/user-attachments/assets/d57f4d9a-fe68-49b4-b8fb-7ec2afb63a96" />


## Key Learnings
- Smaller models can use less energy, but not always faster on every run.
- Energy use & CO₂ emissions are measurable in real-time.
- Tracking environmental impact is key for Green AI adoption in ML projects.

## License
- This project is licensed under the MIT License – free to use and if anyone want to contribute to reach out to me.

## Acknowledgments
- Hugging Face Transformers
- CodeCarbon
- Inspired by the growing Green AI movement in ML research.

---
