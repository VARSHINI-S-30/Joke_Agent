# 😂 AI Joke Agent

An AI-powered Joke Agent built using **Python**, **OpenRouter LLM**, **JokeAPI**, and **Streamlit**. The agent understands natural language requests, uses tool calling to fetch jokes from an external API, and responds conversationally through an interactive chat interface.

---

# 📌 Project Overview

The AI Joke Agent is an intelligent chatbot that generates jokes based on user requests. Instead of generating jokes itself, the agent uses an external API (JokeAPI) as a tool. The Large Language Model (LLM) decides when to invoke the tool, retrieves the joke, and presents it naturally to the user.

The project demonstrates the core concepts of **Agentic AI**, including:

- Tool Calling
- External API Integration
- Conversational Memory
- LLM Reasoning
- Interactive Streamlit UI

---

# 🚀 Features

- 🤖 AI-powered conversational interface
- 😂 Fetches jokes using JokeAPI
- 💻 Programming jokes
- 👻 Spooky jokes
- 🌑 Dark jokes
- 🎉 Random jokes
- 📜 Chat history
- 💬 Natural language interaction
- 🧠 Conversation memory
- ⚡ Real-time API responses
- 🖥️ Streamlit web interface
- 🔄 Tool Calling using OpenRouter

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| OpenRouter | LLM API |
| JokeAPI | External Joke API |
| Streamlit | Frontend UI |
| Requests | API Calls |
| JSON | Conversation Memory |
| dotenv | Environment Variables |

---

# 📂 Project Structure

```
AI_Joke_Agent/
│
├── app.py
├── main.py
├── prompts.py
├── tools.py
├── memory.py
├── memory.json
├── .env
├── requirements.txt
└── README.md
```

---

# 🤖 AI Agent Workflow

```
User Question
      │
      ▼
OpenRouter LLM
      │
      ▼
Determines whether tool is needed
      │
      ▼
Calls Joke Tool
      │
      ▼
JokeAPI
      │
      ▼
Returns Joke
      │
      ▼
LLM formats response
      │
      ▼
Displayed in Streamlit
```

---

# 🧰 Tool Used

## get_joke()

Purpose:

Fetches jokes from JokeAPI.

Input

- Category

Output

- Joke

Example

```
Input

Programming

Output

Why do programmers prefer dark mode?

Because light attracts bugs.
```

---

# 📡 API Used

## JokeAPI

Endpoint

```
https://v2.jokeapi.dev/joke/Any
```

Example

```
https://v2.jokeapi.dev/joke/Programming
```

No API key required.

---

# 🖥️ Streamlit Interface

The UI contains

- ChatGPT-style chat interface
- Sidebar
- Clear Chat button
- Example prompts
- Chat history
- Loading animation
- Responsive design

---

# 🧠 Memory

Conversation history is stored inside

```
memory.json
```

This enables the agent to remember previous interactions during the session.

---

# 📊 Agent Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
                  ▼
              main.py
                  │
                  ▼
          OpenRouter LLM
                  │
          Tool Calling
                  │
                  ▼
             tools.py
                  │
                  ▼
              JokeAPI
                  │
                  ▼
             Joke Result
                  │
                  ▼
           OpenRouter LLM
                  │
                  ▼
          Streamlit Response
```

---

# 📁 File Description

## app.py

Contains the Streamlit user interface.

---

## main.py

Controls

- Agent Loop
- Tool Calling
- LLM Communication
- Memory Integration

---

## tools.py

Contains

```
get_joke()
```

Responsible for communicating with JokeAPI.

---

## prompts.py

Contains the system prompt that instructs the LLM to use the joke tool whenever appropriate.

---

## memory.py

Loads and saves conversation history.

---

## memory.json

Stores chat history.

---

# 🌟 Advantages

- Beginner friendly
- Easy to extend
- Demonstrates Agentic AI
- Uses real external APIs
- Interactive interface
- Modular code structure
- Real-time responses
- Reusable architecture

---

# 🔮 Future Enhancements

- Voice input
- Text-to-Speech jokes
- Joke rating system
- Favorite jokes
- Joke categories dropdown
- Multi-language jokes
- User authentication
- Cloud deployment
- Database integration
- Joke history dashboard
- Emoji reactions
- Daily joke notification

---

# 🎯 Learning Outcomes

This project demonstrates

- Agentic AI
- Tool Calling
- Function Calling
- API Integration
- LLM Communication
- Prompt Engineering
- Streamlit Development
- Memory Management
- JSON Handling
- Python Programming

---

# 📸 Sample Conversation

**User**

```
Tell me a programming joke
```

**Agent**

```
Why do programmers prefer dark mode?

Because light attracts bugs.
```

---

# 📄 License

This project is intended for educational and learning purposes.

---

# 👨‍💻 Author

Developed as a hands-on Agentic AI project using Python and OpenRouter.
