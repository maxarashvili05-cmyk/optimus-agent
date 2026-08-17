OptiMindAgent + OptimusCore
🤖 OptiMindAgent ingests content from the Blogger API and stores it in OptimusCore, a persistent memory layer powered by CockroachDB and AWS.
Built for the CockroachDB × AWS Hackathon, this project demonstrates how agentic memory can be production‑grade, resilient, and globally distributed.

✨ Features
CockroachDB Persistent Memory  
Stores conversation history, blog posts, embeddings, and task state in a resilient cluster.

Distributed Vector Indexing  
Semantic search directly on embeddings inside CockroachDB.

AWS S3 Backup  
All artifacts (conversations, blog posts) are backed up to S3.

AWS Lambda Trigger  
Serverless execution of OptimusCore functions.

ccloud CLI Integration  
Cluster status, audit logs, and provisioning directly from the CLI.

📂 Project Structure
Code
/project-root
  ├── optimus_core.py      # CockroachDB + AWS memory layer
  ├── optimind_agent.py    # Blogger ingestion + analysis
  ├── cli.py               # Command-line interface
  ├── requirements.txt     # Dependencies
  ├── README.md            # Documentation
⚙️ Setup
Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/optimind-agent.git
cd optimind-agent
Install dependencies

bash
pip install -r requirements.txt
Set environment variables

bash
export BLOG_ID="YOUR_BLOG_ID"
export BLOGGER_API_KEY="YOUR_BLOGGER_API_KEY"
export AWS_S3_BUCKET="YOUR_BUCKET_NAME"
export OPENAI_API_KEY="YOUR_OPENAI_KEY"
Run CLI

bash
python cli.py --status
python cli.py --analyze POST_ID
python cli.py --search "agentic memory systems"
🛠️ Requirements
Python 3.9+

CockroachDB cluster (Cloud MCP Server)

AWS account (S3 + Lambda)

OpenAI API key (for embeddings)

Blogger API key (for ingestion)

📊 Architecture Diagram (ASCII)
Code
        +-------------------+
        |   Blogger API     |
        +-------------------+
                 |
                 v
        +-------------------+
        |  OptiMindAgent    |
        |  (ingestion)      |
        +-------------------+
                 |
                 v
        +-------------------+
        |   OptimusCore     |
        | CockroachDB + AWS |
        +-------------------+
          |           |
          v           v
   CockroachDB   AWS Services
 (Persistent DB)   (S3, Lambda)
🧩 CockroachDB Tools Used
MCP Server → Direct connection to CockroachDB cluster.

Distributed Vector Indexing → Embeddings stored and queried at scale.

ccloud CLI → Cluster status and audit logs.

🧩 AWS Services Used
AWS S3 → Artifact/document storage.

AWS Lambda → Serverless agent execution.

🎥 Demo
Live demo available here: Optimus Demo

🧪 How to Run the Demo (Step‑by‑Step)
Check system status

bash
python cli.py --status
Output shows OptimusCore online and Blogger API verified.

Analyze a blog post

bash
python cli.py --analyze POST_ID
Fetches post from Blogger API.

Generates embeddings.

Saves to CockroachDB + S3.

Logs analysis completion.

Perform semantic search

bash
python cli.py --search "agentic memory systems"
Generates embedding for query.

Runs distributed vector search in CockroachDB.

Returns top‑k relevant posts or conversations.

Trigger AWS Lambda (optional)
Inside optimus_core.py:

python
core = OptimusCore()
response = core.trigger_lambda("YourLambdaFunction", {"task":"diagnose"})
print(response)
📖 Use Case Explanation
We chose a blog ingestion workflow to demonstrate agentic memory. OptiMindAgent fetches posts from Blogger, analyzes them, and stores them in CockroachDB with embeddings. This is just one example — the same architecture can be applied to:

Chatbots that persist conversation history.

Recommendation systems with semantic search.

Incident diagnosis agents that store logs and run serverless analysis.

The blog use case makes the demo concrete, but the design is generalizable to any agentic system.

🏆 Judging Criteria Mapping
Agentic Memory Design

CockroachDB is the system of record for agent memory.

Stores embeddings, blog content, and task state with distributed vector indexing.

Technical Implementation

Uses MCP Server for direct agent‑to‑CockroachDB connection.

ccloud CLI integration for cluster management and audit logs.

Semantic search implemented with CockroachDB’s vector indexing.

Real‑World Impact

Demonstrates how agents can persist memory across failures and regions.

Use case: AI blog architect that continuously ingests, analyzes, and retrieves content.

Production Readiness

Secure connection with TLS (sslmode=verify-full).

AWS S3 backup ensures redundancy.

Lambda integration for scalable serverless execution.

Creativity & Originality

Combines Blogger API ingestion with CockroachDB agentic memory.

Shows how content workflows can be automated with persistent, semantic memory.

📜 License
MIT License — free to use, modify, and distribute.