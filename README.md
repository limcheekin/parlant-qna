<div align="center">
<img alt="Parlant Logo" src="https://github.com/emcie-co/parlant-qna/blob/0aba0fae493fb97593d1553392c86476d1cc45e4/banner.png" />
  <h2>Parlant Q&A: A Questions/Answers Tool Service for Parlant</h2>
  <p>
    <a href="https://www.parlant.io/" target="_blank">Website</a> |
    <a href="https://www.parlant.io/docs/quickstart/introduction" target="_blank">Introduction</a> |
    <a href="https://www.parlant.io/docs/quickstart/installation" target="_blank">Installation</a> |
    <a href="https://www.parlant.io/docs/tutorial/getting_started/overview" target="_blank">Tutorial</a> |
    <a href="https://www.parlant.io/docs/about" target="_blank">About</a>
  </p>
  <p>
    <a href="https://pypi.org/project/parlant-qna/" alt="Parlant Q&A on PyPi"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/parlant-qna"></a>
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/parlant-qna">
    <a href="https://opensource.org/licenses/Apache-2.0"><img alt="Apache 2 License" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" /></a>
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/emcie-co/parlant-qna">
    <a href="https://discord.gg/duxWqxKk6J"><img alt="Discord" src="https://img.shields.io/discord/1312378700993663007?style=flat&logo=discord&logoColor=white&label=discord">
</a>
  </p>
</div>

A dynamic question-answering tool service that helps your Parlant agents provide accurate, traceable responses based on your FAQ data.

### Changes Made
Install additional dependencies:
```
pip install --no-cache-dir litellm datasets transformers
pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
```

Setup environment variables:
```
export OPENAI_API_KEY=your_openai_api_key

export LITELLM_PROVIDER_BASE_URL="http://192.168.1.111:8880/v1"
export LITELLM_PROVIDER_MODEL_NAME="openai/ibm-granite_granite-4.0-h-tiny"
export LITELLM_PROVIDER_API_KEY="sk-1"
```

### What is this?

This tool service enables your Parlant agents to answer questions based on a managed set of questions and answers that you provide.

### ✨ Key Features ✨

The service carefully evaluates each question against your FAQ, providing:

- 📝 **Detailed explanation** of how the question was interpreted in light of the FAQ
- 📚 **References to specific source material** used (question IDs and relevant quotes)
- 🔍 **Complete traceability** for each response through session events in Parlant sessions (via tool events)
- 🛡️ **Protection against hallucination** - if the information isn't in your knowledge base, the agent won't make up an answer

### 🚀 Getting Started

Install `parlant-qna`:

```bash
$ pip install parlant-qna
```

You can run the service in two ways:

```bash
# As a standalone server
parlant-qna serve

# Or as a hosted module within your Parlant server
parlant-server --module parlant_qna.module
```

### 📚 Adding FAQs

Add question/answer pairs dynamically through the CLI:

```bash
$ parlant-qna add \
    -q "What are your business hours?" \
    -a "We're open Monday through Friday, 9 AM to 5 PM Eastern Time."
```

### ⚡⚙️ How It Works

When your agent needs to answer a question, it calls the `find_answer` tool through the `qna` service. The service then:

1. Evaluates the question for proper context and intent
2. Searches your FAQs for relevant information
3. Constructs an answer using only verified information
4. Records the entire process as a tool event in the session
5. Returns both the answer and detailed metadata about sources used

Example response:

```json
{
  "answer": "We're open Monday through Friday, 9 AM to 5 PM Eastern Time.",
  "evaluation": "Question seeks information about operational hours, which is provided in the background information",
  "references": [
    {
      "question_id": "dja8-108fj",
      "quotes": ["Monday through Friday, 9 AM to 5 PM Eastern Time"]
    }
  ]
}
```

### 💡 Use Cases

Perfect for:

- Building customer service agents that need accurate, verifiable answers
- Creating internal support bots that can explain their reasoning
- Developing agents that need to provide source references for their responses
- Ensuring compliance by preventing agents from making up information

### 🤝🛠️ Contributing

We're actively developing this tool service. If you'd like to contribute, please:

1. Check our issue tracker for current needs
2. Join our [Discord community](https://discord.gg/duxWqxKk6J) for discussion
3. Submit pull requests with improvements
