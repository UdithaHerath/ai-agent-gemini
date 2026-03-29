# No-Code AI Agent (CLI) with Gemini API

## Overview
This project implements a command-line AI agent using Python and the Gemini API.  
The agent follows the ReAct (Reason → Act → Observe) pattern and can dynamically use tools.

## Features
- CLI-based AI agent
- Gemini API integration (`google-genai`)
- Real tool execution (not simulated)
- ReAct reasoning loop
- Modular architecture

## Tools Implemented
- Calculator Tool
- Time Tool
- Translator Tool (custom)
- File Reader Tool

## Architecture
- Agent → handles reasoning and API calls  
- ToolRegistry → manages tools  
- BaseTool → abstract interface  
- MemoryManager → stores conversation history  

## Requirements
```bash
pip install -r requirements.txt