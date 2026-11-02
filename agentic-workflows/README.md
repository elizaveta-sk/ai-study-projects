# Agentic Workflows

This is a graded lab project for DeepLearning.AI's Agentic AI course. It implements a multi-agent research workflow with a planning agent, tool-using research agent, writer agent, editor agent, and executor agent.

## Setup

1. Create and activate a Python virtual environment.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Add `OPENAI_API_KEY` and `TAVILY_API_KEY` to `.env`.

## Run in Jupyter Notebook

Run `jupyter notebook` from this folder, then open `agentic_workflows_lab.ipynb` and select **Run All Cells**.

The notebook imports `research_tools.py`, which contains the arXiv, Tavily, and Wikipedia tools made available to the research agent. The supplied defaults follow the graded-lab specification; if `openai:o4-mini` is unavailable for your account, pass another available model when calling the individual agents.
