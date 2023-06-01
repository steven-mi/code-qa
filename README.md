# CodeQA

CodeQA is a command-line tool that allows you to ask questions about a project. Gain insights and deepen your
understanding of a repository's codebase effortlessly. It is built on top of LangChain.

## Getting Started

Install Code QA:

```bash
pip install code-qa
```

Add your OpenAI token as virtual environment:

```bash
export OPENAI_TOKEN=YOUR_TOKEN
```

Go to your project folder:

```bash
cd PATH/TO/MY/PROJECT
```

Initialise Code QA Index. This will generate an `code_qa` folder within your project:

```
code_qa init
```

Ask questions about my code:

```
code_qa query How can I test this?
```

## Ignoring Files

If you want to ignore certain files, then create an `.codeqaignore` file and specify them. The file follows the same
standard as `.gitignore`

## License
Apache License Version 2.0, see `LICENSE`