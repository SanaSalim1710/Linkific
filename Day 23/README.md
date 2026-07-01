# AI Research Assistant

A multi-agent research assistant pipeline was built using **LangGraph** and **Groq**. Given a research query, five coordinating agents autonomously search the web, analyse findings, check quality, and produce a polished final report.

<img width="827" height="273" alt="output" src="https://github.com/user-attachments/assets/95872949-e822-4ae8-a36d-7cfc2ec1a0ef" />
## Agents

### Coordinator
**Role:** Orchestrates the entire workflow.

It reads the full shared state after every agent completes their task. It decides which agent should run next based on what has been produced so far and it enforces the revision cap.

### Researcher
**Role:** Gathers raw information from the web that is relevant to the user query.

It calls `TavilySearch` to find relevant sources for the query, then calls `TavilyExtract` to pull the full page text from each URL. It writes  the title, URL, snippet and full text to shared state. It does not summarise or judge quality. Its only purpose is retrieval.

**Tools:** `TavilySearch`, `TavilyExtract`, `web_search(query)`, `web_extract(urls)`

### Analyzer
**Role:** Uses sources from the Research Agent to create a summary.

It takes the raw findings from the Research Agent and uses the LLM to produce a concise, well-structured summary that directly answers the query. If it requires revision, the Critic's feedback is included in the prompt so the Analyzer knows what to improve.

**Tools:** Groq LLM (Llama 3.3-70b), `summariser(findings, query)`

### Critic
**Role:** Quality control.

It compares the Analyzer's summary against the original source text. It checks for factual errors, unsupported claims, contradictions and missing context. It returns a structured JSON verdict (`needs_revision: true/false` and actionable `feedback`). It does not rewrite anything. Its only purpose is to evaluate and provide useful feedback for the Analyser Agent to improve its output.

**Tools:** Groq LLM + `JsonOutputParser`

### Writer
**Role:** Final report formatting.

It takes the approved analysis (after the critic determines revision isn't necessary or after the revision cap is reached) and formats it into a polished report with a title, executive summary, key findings, and conclusion.

**Tools:** Groq LLM (Llama 3.3-70b)

## Shared State

All agents communicate through a single `SharedState` object that flows through the pipeline. Each agent reads what it needs and writes only to its own field.

| Field | Type | Written by | Purpose |
|---|---|---|---|
| `query` | `str` | User | The original research question |
| `research` | `list[dict]` | Researcher | Findings: title, URL, snippet, full text |
| `analysis` | `str` | Analyzer | Research summary |
| `critique` | `dict` | Critic | `{needs_revision, feedback}` |
| `report` | `str` | Writer | Final formatted report |
| `revision_count` | `int` | Coordinator | Tracks how many revision loops have run |
| `max_revisions` | `int` | User (default: 2) | Cap on revision attempts |
| `next_agent` | `str` | Coordinator | Routing target read by the conditional edge |
| `logs` | `list[str]` | All agents | Log of each step of the process |

---
