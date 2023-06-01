import os

import pathspec
from langchain.document_loaders import TextLoader


def load_files(root_path):
    # Get all files in current directory
    all_files = []
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            all_files.append(os.path.join(dirpath, filename))

    files_to_load = all_files
    ignore_path = os.path.join(root_path, '.codeqaignore')
    if os.path.exists(ignore_path):
        with open(ignore_path) as f:
            ignore = f.read()

        spec = pathspec.PathSpec.from_lines('gitwildmatch', ignore.splitlines())

        # Filter files based on .gitignore patterns
        files_to_load = [f for f in all_files if not spec.match_file(f)]

    docs = []
    for file in files_to_load:
        try:
            print(file)
            loader = TextLoader(os.path.join(file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass
    return docs


def load_openai_token():
    token = os.environ.get("OPENAI_TOKEN")
    if not token:
        raise EnvironmentError("`OPENAI_TOKEN` is not set")
    return token
