# AsterNova — Enterprise HR Policy & Employee Support Copilot

An Agentic RAG application that helps employees find accurate answers from internal HR documents using **LangGraph, FastAPI, OpenAI, Pinecone, and Tavily**.

The application retrieves internal knowledge, evaluates evidence, rewrites queries when necessary, uses external search as a controlled fallback, and generates source-grounded answers.

## Features

- **Agentic RAG:** Stateful workflows with LangGraph and conditional routing.
- **Semantic Search:** Retrieve relevant HR documents using Pinecone.
- **Evidence Grading:** Evaluate retrieved context before generating answers.
- **Query Rewriting:** Improve weak queries and retry retrieval with bounded attempts.
- **Web Search Fallback:** Use Tavily when internal evidence is insufficient and external search is appropriate.
- **Grounded Responses:** Provide answers with relevant source references.
- **Document Ingestion:** Upload and index HR knowledge documents.
- **REST API:** Expose functionality through FastAPI.
- **Interactive UI:** Employee-facing chat interface built with HTML, CSS, and JavaScript.
- **Audit Logging:** Track workflow decisions and application events.
- **Containerization:** Support reproducible deployment using Docker.

## Agentic RAG Workflow

```text
Employee Question
       |
       v
  Query Router
       |
       v
Retrieve Internal HR Knowledge
       |
       v
    Grade Evidence
       |
   +---+---+
   |       |
Sufficient Weak
   |       |
   v       v
Generate   Rewrite Query
Answer        |
          Retry Retrieval
              |
              v
        Grade Evidence
              |
        +-----+-----+
        |           |
    Sufficient   Insufficient
        |           |
        v           v
    Generate    Check External
    Answer      Search Eligibility
                    |
                    v
               Tavily Search
                    |
                    v
              Grade Web Results
                    |
               +----+----+
               |         |
           Sufficient   Weak
               |         |
               v         v
         Cited Answer  Abstain or
                       Refer to HR
```

**Key principle:** Internal HR policies remain the source of truth for company-specific rules. External information is clearly distinguished from internal guidance, and unsupported answers are not fabricated.

## Technology Stack

| Component | Technology |
|---|---|
| Agent orchestration | LangGraph |
| LLM | OpenAI |
| Embeddings | OpenAI `text-embedding-3-small` |
| Vector database | Pinecone |
| Web search | Tavily |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Metadata and audit | SQLite for local development; PostgreSQL for production |
| Testing | Pytest |
| Deployment | Docker |

## Project Structure

```text
asternova-hr-copilot/
├── app/
│   ├── api/
│   │   ├── routes.py
│   │   └── dependencies.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── security.py
│   ├── rag/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   ├── retrieval.py
│   │   ├── grading.py
│   │   └── workflow.py
│   ├── services/
│   │   ├── ingestion.py
│   │   ├── search.py
│   │   └── audit.py
│   └── main.py
├── data/
│   └── sample_kb/
│       ├── employee_handbook.md
│       ├── leave_policy.md
│       └── remote_work_policy.md
├── static/
│   ├── css/style.css
│   └── js/app.js
├── templates/
│   └── index.html
├── tests/
├── scripts/
│   └── ingest_sample_kb.py
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd asternova-hr-copilot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` and configure your API keys.

```env
APP_ENV=development
APP_PORT=8080

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small

PINECONE_API_KEY=
PINECONE_INDEX_NAME=asternova-hr-kb
PINECONE_NAMESPACE=company-hr-kb

TAVILY_API_KEY=

DATABASE_URL=sqlite:///./hr_copilot.db

MAX_RETRIEVAL_RETRIES=2
RETRIEVAL_TOP_K=5
ENABLE_EXTERNAL_SEARCH=true
```

Configure the Pinecone index dimension to match the selected embedding model. Keep all credentials out of source control.

### 5. Ingest sample documents

```bash
python scripts/ingest_sample_kb.py
```

### 6. Run the application

```bash
python run.py
```

Open the application:

- **Web interface:** `http://127.0.0.1:8080`
- **API documentation:** `http://127.0.0.1:8080/docs`

These commands assume the repository implements the listed scripts and configuration.

## Demo Scenarios

| Scenario | Expected Behavior |
|---|---|
| Internal HR question | Answer from relevant internal documents |
| Remote-work policy | Retrieve and cite the applicable policy |
| Weak retrieval results | Rewrite the query and retry within configured limits |
| Current public information | Search external sources when appropriate and label the evidence |
| Insufficient evidence | Explain the limitation instead of hallucinating |
| Unauthorized document access | Reject access to restricted information |

## Security Considerations

- Protect API keys and sensitive documents.
- Enforce authentication and role-based authorization for protected endpoints.
- Apply document-level access controls during retrieval.
- Validate uploaded documents and restrict file sizes.
- Treat retrieved documents and web content as untrusted input.
- Apply timeouts, rate limits, and bounded retries.
- Keep audit logs free of unnecessary personal information.
- Require human review for consequential HR decisions.

**Note:** Production deployment requires implementation and testing of these security controls. Sample HR documents are illustrative and must be replaced with approved organizational policies before real-world use.

## License

Add an appropriate open-source license before publishing the repository.