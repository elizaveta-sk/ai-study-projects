# Reflective AI Agent

This is a Week 2 lab project for DeepLearning.AI's Agentic AI course. It builds a three-step reflective writing agent: draft an essay, critique it, then revise it using the critique.

The completed lab is available as a Jupyter Notebook with sections and comments: `reflective_writing_agent_lab.ipynb`.

## Setup

1. Create and activate a Python virtual environment.
2. Install the dependencies: `pip install -r requirements.txt`.
3. Open the included `.env` file and paste your key after `OPENAI_API_KEY=`. For the supplied default models, use an OpenAI API key.

## Run it in Jupyter Notebook

Yes, the completed lab can be run in Jupyter Notebook. From this folder, start Jupyter with:

```sh
jupyter notebook
```

Then open `reflective_writing_agent_lab.ipynb` and select **Run All Cells**. The last cell prints the draft, reflection, and revised essay.

The notebook includes the `generate_draft`, `reflect_on_draft`, and `revise_draft` functions. Each returns the model's generated text. The reflection stage uses `gpt-4o-mini` because the lab's original `o4-mini` default is deprecated.
