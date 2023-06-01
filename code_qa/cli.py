import fire
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from code_qa.logger import logger
from code_qa.utils import load_files, load_openai_token


class CodeQA:
    CODE_QA_FOLDER = "./.code_qa_data"

    def init(self, project_path="./"):
        token = load_openai_token()

        logger.info("Start loading project")
        raw_docs = load_files(project_path)
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(raw_docs)

        logger.info("Start generating embeddings")
        embeddings = OpenAIEmbeddings(openai_api_key=token)
        docsearch = Chroma.from_documents(docs, embeddings, persist_directory=self.CODE_QA_FOLDER)
        logger.info(f"Saving embeddings to {self.CODE_QA_FOLDER}")
        docsearch.persist()
        logger.info("Initialising CodeQA was successful")
        return

    def query(self, *query, model_name='gpt-3.5-turbo'):
        if not query:
            logger.error(
                'No query provided. Please provide a query to process e.g. `code_qa query How can I run this CLI`.')
            return

        token = load_openai_token()
        model = ChatOpenAI(model_name=model_name, temperature=0, openai_api_key=token)  # switch to 'gpt-4'
        embeddings = OpenAIEmbeddings(openai_api_key=token)
        docsearch = Chroma(embedding_function=embeddings, persist_directory=self.CODE_QA_FOLDER)
        qa = ConversationalRetrievalChain.from_llm(model, retriever=docsearch.as_retriever())
        return qa({"question": ' '.join(query), "chat_history": []})


def main():
    return fire.Fire(CodeQA)


if __name__ == '__main__':
    main()
