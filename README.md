# CodeQA

CodeQA is a powerful command-line tool designed to help developers understand and navigate their codebase more efficiently. By asking questions directly about your project, you can gain insights and deepen your understanding of the codebase without the need for extensive manual exploration. CodeQA is built on top of LangChain, leveraging its capabilities to provide accurate and insightful responses.

Besides code, CodeQA is engineered to be universally applicable across various text documents. It enables you to effortlessly navigate through:

- PDF documents
- Markdown files
- And any other form of text-based documents.

## Getting Started

Follow these steps to install and set up CodeQA:

1. **Install CodeQA**: Use pip to install CodeQA. Run the following command in your terminal:

    ```bash
    pip install code-qa
    ```

2. **Set up OpenAI Token**: CodeQA uses OpenAI's API to generate responses. You need to add your OpenAI token to your virtual environment. Replace `YOUR_TOKEN` with your actual OpenAI token:

    ```bash
    export OPENAI_TOKEN=YOUR_TOKEN
    ```

3. **Navigate to your project folder**: Use the `cd` command to navigate to your project's directory:

    ```bash
    cd PATH/TO/MY/PROJECT
    ```

4. **Initialize CodeQA Index**: This will generate a `.code_qa` folder within your project. The folder contains your project embeddings stored as parquet files. Run the following command:

    ```bash
    code_qa init
    ```

## Usage

With CodeQA, you can ask questions directly about your code. For example, if you want to know how to test a particular part of your code, you can ask:

```bash
code_qa query "How can I test this?"
```

## Ignoring Files

If there are certain files or directories that you want CodeQA to ignore, you can specify them in a `.codeqaignore` file. This file follows the same syntax and rules as the `.gitignore` file. Simply create a `.codeqaignore` file in your project's root directory and list the files or directories you want to ignore.


## License

CodeQA is licensed under the Apache License Version 2.0. For more details, see the [LICENSE](LICENSE) file.
