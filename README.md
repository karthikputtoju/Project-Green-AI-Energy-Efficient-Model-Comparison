# green-ai-model-comparison
Compare GPT2 vs DistilGPT2 for text generation with energy usage, carbon emissions, and performance metrics to promote Green AI awareness.
## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/karthikputtoju/green-ai-model-comparison.git
    cd green-ai-model-comparison
    ```

2. **Create and activate a Python virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
   
    ```bash
    If you encounter issues with `requirements.txt`, you can manually install the main dependencies:
    pip install torch transformers codecarbon 
    ```

## Results Explanation

After execution, results are saved to `results/` as CSV and visualizations. Key metrics include:

- **Energy Usage:** Power consumed during inference for each model.
- **Carbon Emissions:** Estimated CO₂ output based on energy usage and location.
- **Performance:** Text quality metrics (e.g., perplexity, BLEU), generation speed.
- **Comparison:** Summarized in tables and plots for easy interpretation.

Use these insights to evaluate the environmental impact and efficiency of different AI models, supporting Green AI initiatives.

## License

This project is licensed under the MIT License.
