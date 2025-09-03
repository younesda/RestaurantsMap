import pandas as pd

class ImputationMode:
    """
    Classe pour imputer les valeurs manquantes avec le mode.
    """

    @staticmethod
    def imputation_mode(df: pd.DataFrame, column: str):
        """ 
            Imputer les valeurs manquantes d'une colonne avec le mode de cette colonne.

            Args:
                df (pd.DataFrame): Le DataFrame contenant les données.
                column (str): Le nom de la colonne à imputer.

            Returns:
                pd.DataFrame: Le DataFrame avec les valeurs manquantes imputées.
        """
        mode = df[column].mode()
        df[column].fillna(mode, inplace=True)
        return df