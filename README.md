## LangChain Environment Setup

This guide will walk you through setting up the Python and Pipenv environment required to run LangChain. Please note that LangChain and OpenAI are under active development and may undergo frequent changes. 

**Important Note:** We will be using Pipenv to manage dependencies and enforce specific versions due to the frequent changes mentioned above.

**Before you begin:**

- Deprecation warnings about Langchain versions 0.1.0 and 0.2.0 can be safely ignored.

**Prerequisites:**

- Python 3.11: [https://www.python.org/downloads/](https://www.python.org/downloads/)

**Setting Up Pipenv:**

1. **Create a project directory:**
   - Create a directory named `pycode` on your development machine.

2. **Install Pipenv (if not already installed):**
   - Open your terminal and run:
     ```bash
     pip install pipenv
     ```
   - For some environments, use:
     ```bash
     pip3 install pipenv
     ```

3. **Create a Pipfile:**
   - Inside your `pycode` directory, create a file named `Pipfile`.

4. **Copy and paste the following code into your Pipfile:**

   ```
   [[source]]
   url = "https://pypi.org/simple"
   verify_ssl = true
   name = "pypi"

   [packages]
   langchain = "==0.0.352"
   openai = "==0.27.8"
   python-dotenv = "==1.0.0"

   [dev-packages]

   [requires]
   python_version = "3.11"
   ```

5. **Install dependencies:**
   - Inside your `pycode` directory, run:
     ```bash
     pipenv install
     ```

6. **Activate Pipenv shell:**
   - Run:
     ```bash
     pipenv shell
     ```
   - This will activate the virtual environment managed by Pipenv.

**Running Python Scripts:**

- Once inside the activated Pipenv shell, you can run Python commands as shown in the lecture videos, for example:

   ```bash
   python main.py
   ```

**Additional Notes:**

- If you make changes to environment variables or keys, you may need to exit and re-enter the shell using `pipenv shell`.
- Anaconda users: Pipenv might conflict with your environment. Deactivate your `conda` environment if you encounter any issues.

**Remember to ignore deprecation warnings about Langchain versions 0.1.0 and 0.2.0!**

