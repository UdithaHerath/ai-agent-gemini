# Step 3 – Testing and Deployment Report

## Course
Applied System Software (ASD)

## Student
Herath Mudiyanselage Udesha Uditha Kumara Herath  
221AMB073

---

# Project Title

AI Agent Gemini – Modular AI Assistant with Dynamic Tool Execution

---

# Testing Process

The testing process was performed alongside the implementation phase to ensure system correctness, reliability, and robustness.

A structured testing approach was applied, including:

- unit testing of individual tools,
- integration testing of tool interactions,
- validation of error handling,
- functional testing of core workflows.

Testing was implemented using Python’s built-in `unittest` framework.

---

# Test Structure

A dedicated `tests/` folder was created containing separate test files for different components:

- `test_calculator.py`
- `test_file_reader.py`
- `test_registry.py`

This structure ensures modular and maintainable test development.

---

# Test Scenarios

The following key scenarios were tested:

## Calculator Tool
- addition, subtraction, multiplication, division
- division by zero handling

## File Reader Tool
- reading an existing file
- handling non-existent files

## Tool Registry
- registering tools
- retrieving tools
- handling invalid tool requests

---

# Error Handling Testing

The system was tested against common failure scenarios:

- invalid mathematical expressions
- division by zero
- missing file inputs
- non-existent files
- unknown tool requests

The system was updated to gracefully handle errors by returning descriptive error messages instead of crashing.

---

# Test Results

All implemented tests were executed successfully:

- total tests: 10
- passed: 10
- failed: 0

The results confirm that the system behaves correctly under both normal and edge-case conditions.

---

# Deployment Preparation

The system is prepared for controlled deployment with the following components:

- `requirements.txt` for dependency management
- clear project structure
- modular design for easy extension
- command-line execution interface

To run the system:

```bash
pip install -r requirements.txt
python main.py
```

---

# Data Conversion and Handling

The system processes structured input data in the form of dictionaries passed between components.

Examples include:

- tool parameters (e.g., expression, filename)
- tool outputs returned as strings

Data is validated and handled within each tool to ensure consistency and correctness across the system.

---

# Conclusion

The system has been successfully tested and prepared for deployment. The testing process ensured correctness, reliability, and robustness of all major components.

The modular architecture and tool-based design support future scalability and extension of the system.