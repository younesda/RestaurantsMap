import pandas as pd

class ImputationMediane:
    """
    Classe pour imputer les valeurs manquantes avec la médiane.
    """

    @staticmethod
    def imputation_mediane(df: pd.DataFrame, column: str):
        """ 
            Imputer les valeurs manquantes d'une colonne avec la médiane de cette colonne.

            Args:
                df (pd.DataFrame): Le DataFrame contenant les données.
                column (str): Le nom de la colonne à imputer.

            Returns:
                pd.DataFrame: Le DataFrame avec les valeurs manquantes imputées.
        """
        median = df[column].median()
        df[column].fillna(median, inplace=True)
        return df