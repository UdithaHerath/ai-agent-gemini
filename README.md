# AI Agent Gemini

A modular AI-powered command-line assistant developed in Python using the Google Gemini API.  
The system implements an agent-based architecture with dynamic tool execution, memory handling, and ReAct-style reasoning workflows.

This project was developed as part of the **Applied System Software (ASD)** course at Riga Technical University.

---

# Project Overview

The project demonstrates the implementation of an AI- and agent-based software system capable of:

- Understanding user requests
- Selecting appropriate tools dynamically
- Executing external functions
- Managing conversation context
- Producing intelligent responses using an LLM

The system follows modern AI-agent software engineering principles including modular architecture, separation of concerns, extensibility, and tool orchestration.

---

# Features

- Google Gemini API integration
- ReAct-style reasoning loop
- Dynamic tool registry architecture
- Modular tool implementation
- Memory management
- File reading capability
- Mathematical calculations
- Time retrieval tool
- Translation functionality
- Error handling for invalid tool calls
- Extensible architecture for adding future tools

---

# System Architecture

The project uses a modular architecture consisting of the following components:

## Agent
Responsible for:
- interacting with the Gemini model,
- processing prompts,
- managing reasoning flow,
- selecting and executing tools.

## Tool Registry
Maintains and manages all available tools in the system.

## BaseTool
Defines the common interface used by all tools.

## Memory Manager
Stores conversation history and context during execution.

## Tools
Specialized modules responsible for performing specific tasks.

---

# ReAct Workflow

The system implements a simplified ReAct (Reason → Act → Observe) workflow:

1. User submits a request
2. Agent analyzes the request
3. Agent determines whether a tool is required
4. Appropriate tool is selected
5. Tool executes the action
6. Result is returned to the agent
7. Agent generates the final response

---

# Project Structure

```text
ai-agent-gemini/
│
├── agent.py
├── base_tool.py
├── memory.py
├── tool_registry.py
├── main.py
├── requirements.txt
├── README.md
│
├── docs/
│
└── tools/
    ├── calculator_tool.py
    ├── file_reader_tool.py
    ├── time_tool.py
    └── translator_tool.py
```

---

# Technologies Used

- Python 3
- Google Gemini API
- Object-Oriented Programming (OOP)
- Modular Software Architecture
- ReAct Agent Workflow
- Tool Registry Pattern

---

# Installation

## Clone Repository

```bash
git clone https://github.com/UdithaHerath/ai-agent-gemini.git
```

## Navigate to Project Folder

```bash
cd ai-agent-gemini
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Before running the system, insert your Gemini API key inside `main.py`.

Run the application:

```bash
python main.py
```

---

# Example Commands

- "Calculate 25 * 12"
- "Read the sample file"
- "What time is it?"
- "Translate hello to Spanish"

---

# Software Engineering Concepts Applied

This project demonstrates concepts from the Applied System Software course:

- Modular system architecture
- AI-agent workflows
- Tool orchestration
- Separation of concerns
- ReAct reasoning
- Object-oriented design
- Extensible system design
- Integration of AI APIs
- Error handling
- Command-line interaction

---

# Future Improvements

Possible future enhancements include:

- Environment variable support
- Advanced memory persistence
- Multi-agent collaboration
- Web interface
- Additional tools and APIs
- Logging system
- Automated testing suite
- Deployment automation

---

# Author

Herath Mudiyanselage Udesha Uditha Kumara Herath  
221AMB073

Applied System Software  
Riga Technical University