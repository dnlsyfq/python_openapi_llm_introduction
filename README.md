# Python OpenAI API & LLM Introduction

> A beginner-friendly introduction to using Large Language Models (LLMs) with Python and the OpenAI API.

## 📖 Overview

Large Language Models (LLMs) are AI systems trained on massive amounts of text data to understand and generate human-like language. Using the OpenAI API, developers can quickly integrate AI-powered capabilities into applications.

Common use cases include:

- 🤖 Chatbots and virtual assistants
- ✍️ Content generation
- 📝 Text summarization
- 💻 Code generation and review
- ❓ Question answering
- 📊 Data extraction and classification
- ⚙️ Workflow automation

This repository demonstrates how to connect to the OpenAI API using Python and build simple LLM-powered applications.

---

## 🚀 Prerequisites

Before starting, ensure you have:

- Python 3.8 or later
- An OpenAI API key
- Basic knowledge of Python

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/python-openai-llm-introduction.git
cd python-openai-llm-introduction
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install openai python-dotenv
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Load your credentials securely:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```

> ⚠️ Never commit API keys to GitHub.

---

## 🧠 What is a Large Language Model?

A Large Language Model (LLM) is a neural network trained to understand and generate natural language.

Modern LLMs can:

- Write content
- Summarize documents
- Generate code
- Translate languages
- Answer questions
- Extract structured information
- Perform reasoning tasks

LLMs generate responses by predicting the most likely next tokens based on the provided context.

---

## 💻 Your First OpenAI API Call

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1",
    input="Explain Large Language Models in simple terms."
)

print(response.output_text)
```

---

## 💬 Chat Example

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "system",
            "content": "You are a helpful AI tutor."
        },
        {
            "role": "user",
            "content": "What is machine learning?"
        }
    ]
)

print(response.output_text)
```

---

## 🎯 Common LLM Use Cases

### Content Generation

```python
prompt = "Write a blog introduction about artificial intelligence."
```

### Text Summarization

```python
prompt = "Summarize this article in three bullet points."
```

### Code Generation

```python
prompt = "Write a Python function that calculates factorial."
```

### Information Extraction

```python
prompt = """
Extract the following information:
- Name
- Email
- Phone Number
"""
```

### Sentiment Analysis

```python
prompt = """
Determine whether this review is positive,
negative, or neutral.
"""
```

---

## 📂 Project Structure

```text
python-openai-llm-introduction/
│
├── README.md
├── requirements.txt
├── .env
│
├── examples/
│   ├── basic_completion.py
│   ├── chatbot.py
│   ├── summarizer.py
│   └── sentiment_analysis.py
│
└── src/
    └── main.py
```

---

## ⚡ Best Practices

### 1. Write Clear Prompts

✅ Good:

```text
Summarize this article in three bullet points.
```

❌ Poor:

```text
Summarize.
```

### 2. Handle Exceptions

```python
try:
    response = client.responses.create(
        model="gpt-4.1",
        input="Hello!"
    )

    print(response.output_text)

except Exception as e:
    print(f"Error: {e}")
```

### 3. Store Secrets Securely

- Use environment variables
- Never hardcode API keys
- Avoid exposing keys in client-side applications

### 4. Monitor Usage

Track:

- Request volume
- Model usage
- API costs
- Rate limits

---

## 🔒 Security Considerations

When building AI applications:

- Never expose API keys publicly
- Validate user input
- Avoid sending sensitive data
- Implement rate limiting
- Log requests responsibly
- Follow your organization's security policies

---

## 📚 Learning Resources

- OpenAI Platform Documentation
- OpenAI API Reference
- Python Official Documentation
- Prompt Engineering Guides

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## ⭐ Support

If you found this project useful:

- Star the repository ⭐
- Share it with others 📢
- Contribute improvements 🚀

---

## 🙏 Acknowledgments

Special thanks to:

- OpenAI
- The Python community
- Open-source contributors worldwide

Happy coding! 🎉
