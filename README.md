
# MCP Basic Project

This repository contains a basic implementation of the MCP (Model Context Protocol). This guide will walk you through the steps to clone the repository, set up a virtual environment, and run the MCP project.

## Steps to Set Up the Project

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/jalaj-pandey/mcp-basic.git
````

### 2. Navigate to the Project Directory

Change into the `mcp-hello` directory:

```bash
cd mcp-hello
```

### 3. Create a Virtual Environment

Create a new virtual environment using `uv`:

```bash
uv venv
```

### 4. Activate the Virtual Environment

Activate the virtual environment:

#### On Windows:

```bash
.venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

Install the necessary dependencies for the project:

```bash
uv add mcp[cli] httpx
```

### 6. Run the Project

Finally, run the main script in development mode:

```bash
mcp dev main.py
```

This will start the project in development mode.

## Additional Information

* **MCP**: The Microservice Control Plane (MCP) is a framework designed to simplify the management of microservices in distributed systems.
* **uv**: A command-line tool to simplify project setup and management in Python.

