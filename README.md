# AI_agent
### File Structure
```
ai-agent/
├── src/                              # Main source package (src-layout)
│   └── research_agent/
│       ├── __init__.py
│       ├── agents/                   # Agent implementations
│       │   ├── __init__.py
│       │   ├── base.py               # Abstract base agent (framework-agnostic)
│       │   ├── deep_research.py      # Deep Research agent
│       │   └── prompts/
│       │       ├── __init__.py
│       │       └── deep_research.md
│       ├── tools/                    # Tool layer
│       │   ├── __init__.py
│       │   ├── base.py               # Tool protocol/ABC
│       │   ├── web_search.py         # Web search (e.g., DuckDuckGo, Tavily)
│       │   ├── web_scraper.py        # Web scraper (e.g., httpx + BeautifulSoup)
│       │   └── registry.py           # Tool registry
│       ├── llm/                      # LLM abstraction (swap frameworks here)
│       │   ├── __init__.py
│       │   ├── client.py
│       │   └── config.py
│       ├── models/                   # Pydantic models (as you wanted)
│       │   ├── __init__.py
│       │   ├── config.py             # pydantic-settings (env config)
│       │   ├── common.py             # Shared types
│       │   ├── messages.py           # Message/tool-call schemas
│       │   └── research.py           # Research-specific models
│       ├── memory/                   # Conversation state management
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── history.py
│       └── utils/
│           ├── __init__.py
│           ├── logging.py            # Structured logging
│           └── retry.py              # Retry/backoff utilities
├── api/                              # FastAPI backend (decoupled from agent)
│   ├── __init__.py
│   ├── main.py                       # FastAPI app factory
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── research.py           # Research endpoints
│   │   │   └── health.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py                # API request/response schemas
│   ├── db/
│   │   ├── __init__.py
│   │   ├── engine.py                 # SQLAlchemy async engine
│   │   └── models.py                 # ORM models
│   └── deps.py                       # FastAPI dependencies
├── frontend/                         # All frontends
│   ├── chainlit/                     # Chainlit chat UI
│   │   ├── app.py
│   │   ├── .chainlit/
│   │   │   └── config.toml
│   │   └── public/
│   │       └── chainlit.md
│   └── cli/                          # CLI interface
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py                   # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── agents/
│   │   ├── tools/
│   │   └── models/
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_research_flow.py
│   └── e2e/
│       └── __init__.py
├── scripts/                          # Dev/ops scripts
│   └── clean_git_history.sh          # Script to purge .env from git
├── .env.example                      # Template (NO secrets)
├── .gitignore                        # Updated
├── .python-version                   # Keep 3.12
├── pyproject.toml                    # Clean deps
├── README.md
└── uv.lock