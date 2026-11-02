# Tool Use and Reflective Agents

This is a Week 3 lab project for DeepLearning.AI's Agentic AI course. The notebook creates a mini research agent that searches arXiv and the web, reflects on the report, rewrites it, and publishes it as styled HTML. The `research_tools.py` module supplies the arXiv and Tavily tools used by the notebook.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Open `.env` and add both `OPENAI_API_KEY` and `TAVILY_API_KEY`.

## Run in Jupyter Notebook

From this folder, run:

```sh
jupyter notebook
```

Open `tool_use_reflective_agents_lab.ipynb`, then select **Run All Cells**. The final cell displays the generated HTML report.

The notebook follows the manual tool-calling loop demonstrated in the supplied Module 3 examples: it sends tool schemas to the model, executes requested tools locally, adds their JSON results to the conversation, and repeats until the model returns its final report.
