import glob
import pandas as pd
import docx2txt
from langchain.document_loaders import PyPDFLoader


class Loader:
    def __init__(self, path: str) -> None:
        self.path = path
        self.df = None
        self.files = None

    def load_csv(self) -> pd.DataFrame:
        """Load all csv files from a directory and concatenate them into a single dataframe."""
        my_files = glob.glob(f"{self.path}/*.csv")
        self.files = my_files
        df = pd.DataFrame([])
        for i in my_files:
            df_load = pd.read_csv(i)
            df = pd.concat([df, df_load])
        df = df.drop_duplicates(subset=['Title', 'Description', 'Detail URL', 'Location']).reset_index(drop=True)
        df = df.drop_duplicates().reset_index(drop=True)
        self.df = df
        return df

    def load_docx(self) -> pd.DataFrame:
        """Load all docx files from a directory and concatenate them into a single dataframe."""
        my_files = glob.glob(f"{self.path}/*.docx")
        self.files = my_files
        df = pd.DataFrame([])
        for i in my_files:
            text = docx2txt.process(i)
            df = pd.concat([df, pd.DataFrame([text])])
        df = df.rename(columns={0: 'text'}).drop_duplicates().reset_index(drop=True)
        self.df = df
        return df

    def load_pdf(self) -> pd.DataFrame:
        """Load all pdf files from a directory and concatenate them into a single dataframe."""
        my_files = glob.glob(f"{self.path}/*.pdf")
        self.files = my_files
        df = pd.DataFrame([])
        for i in my_files:
            text = ''
            loader = PyPDFLoader(i)
            pages = loader.load()
            for j in pages:
                text += j.page_content
            df = pd.concat([df, pd.DataFrame([text])])
        df = df.rename(columns={0: 'text'}).drop_duplicates().reset_index(drop=True)
        self.df = df
        return df
