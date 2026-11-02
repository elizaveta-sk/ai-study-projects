# Planning Workflows for Autonomous Agents

This DeepLearning.AI Agentic AI lab implements a planning-driven research workflow. A planner builds the work plan, a tool-using researcher gathers evidence, a writer drafts the report, and an editor critiques and improves it.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Add `OPENAI_API_KEY` and `TAVILY_API_KEY` to `.env`.

## Run in Jupyter Notebook

Run `jupyter notebook` in this folder and open `planning_workflows_lab.ipynb`. Run the cells in order, then run the final cell to execute the full workflow.

The notebook uses `research_tools.py` for arXiv, Tavily, and Wikipedia search. Its `openai:o4-mini` planner default follows the lab brief; pass another available model to `planner_agent` if that model is unavailable on your account.
