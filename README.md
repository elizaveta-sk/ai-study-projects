# AI Study Projects

Projects I built while learning to work with LLMs, AI agents and coding assistants. They start with my biggest project, followed by the labs from two DeepLearning.AI courses in the order I did them.

## Main project: AI Ticket Management System

**[Repository](https://github.com/elizaveta-sk/ai_ticket_management_system) · Live demo: [Contact form](https://aiticketmanagement.netlify.app/contact) · [Login](https://aiticketmanagement.netlify.app/login)**
*might take a minute to load, because it's a free server tier. if you get any type of error logging in, retry in a minute.

sample user for the login page = 
lucy_agent@example.com password123

A support desk for an online course provider. An AI agent answers the questions it can from a knowledge base and passes everything else to a human support team on a ticket management platform.

**Stack:** React, TypeScript, Bun, Express, PostgreSQL, Prisma, Better Auth, the Vercel AI SDK with OpenAI, SendGrid, Sentry, Vitest and Playwright. Deployed on Netlify, Render and Neon.

### What I learned

- **Building with AI coding agents:** scoping, planning, building, testing, reviewing and improving a full-stack app in phases, while maintaining project context. I also created specialised review and testing agents, and used AI to diagnose issues and refactor toward clean, reusable components.
- **Full-stack development:** React, Express, TypeScript and PostgreSQL with Prisma, including authentication, role-based access, validation, email-to-ticket workflows and admin CRUD features.
- **Testing and security:** component and end-to-end tests, input validation, XSS sanitisation, rate limiting, environment-based secrets, and authentication and authorisation reviews.
- **AI product features:** ticket classification, knowledge-base-assisted resolution, reply polishing and conversation summaries, supported by job queues and state-based ticket handling.

## Claude Code: A Highly Agentic Coding Assistant

### 1. [Expense Tracker](https://github.com/elizaveta-sk/expense-tracker-starter)

A small React app for tracking income and expenses. The starter deliberately shipped with bugs, a poor UI and messy code, so I used it to practise fixing all three with Claude Code.

- **Bugs:** fixed totals that were joining amounts as text instead of adding them, and a seed transaction with the wrong type.
- **UI:** redesigned the app to look more modern and added a spending chart with Recharts.
- **Code:** split the single large `App.jsx` into separate components.
- **Features and form behaviour:** added transaction deletion, separate income and expense categories, and validation that rejects blank descriptions.

### 2. [RAG Chatbot](https://github.com/elizaveta-sk/starting-ragchatbot-codebase/tree/feature/source-links-and-new-chat)

A web app that answers questions about course materials. The course provided the UI and the base of the app, and I extended it by working on the LLM integration and adding new features.

**How it works**

- Course scripts are split into chunks, embedded and stored in ChromaDB when the server starts.
- Claude decides for each question whether to answer directly or call a tool to look up the course materials.
- Searches can be narrowed to a course or lesson, and partial course names are matched to the right course.
- Each session remembers recent messages, so follow-up questions work.
- The sidebar shows the available courses and suggested questions.

**What I added**

- **Course outline tool:** a new tool Claude can call to return a course's title, link and full lesson list.
- **Clickable sources:** answers link to the lesson video they came from, or to the course if there is no lesson link.
- **New Chat button:** clears the conversation, cancels any request in progress and deletes the old session on the server.
- **Model upgrade:** moved the app to a newer Claude model and updated the API calls to handle its thinking blocks.

**Stack:** Python, FastAPI, ChromaDB, sentence-transformers, the Anthropic SDK, and HTML, CSS and JavaScript.

## Agentic AI

Completed notebook projects for the DeepLearning.AI Agentic AI course. Each project includes a Jupyter notebook and its requirements.

| Order | Project | What it implements | Skills practised |
| --- | --- | --- | --- |
| 1 | [`reflective-ai-agent`](./reflective-ai-agent) | A writing agent that drafts, critiques, and revises an essay. | Prompt design, self-reflection, iterative improvement, OpenAI API use. |
| 2 | [`tool-use-reflective-agents`](./tool-use-reflective-agents) | A research agent that calls arXiv and web-search tools, improves its report, and produces HTML. | Function/tool calling, API integration, tool-result loops, reflection, report publishing. |
| 3 | [`agentic-workflows`](./agentic-workflows) | A multi-agent research workflow with planning, research, writing, editing, and execution stages. | Agent orchestration, role separation, research tools, multi-step workflows. |
| 4 | [`planning-workflows`](./planning-workflows) | A planning-first autonomous research pipeline that turns a plan into an edited report. | Task planning, delegation, sequential workflows, synthesis and editorial review. |

### Running a lab

Open a project folder, install its dependencies with `pip install -r requirements.txt`, create a `.env` file with `OPENAI_API_KEY` (plus `TAVILY_API_KEY` for every lab except `reflective-ai-agent`), then run `jupyter notebook` and open that lab's `.ipynb` file.

The two workflow labs intentionally cover similar roles from different course exercises: `agentic-workflows` is the graded integrated lab, while `planning-workflows` concentrates on the planning pattern.
