import pandas as pd

class ImputationMoyenne:
    """
    Classe pour imputer les valeurs manquantes avec la moyenne.
    """
    
    @staticmethod
    def imputation_moyenne(df: pd.DataFrame, column: str):
        """ 
            Imputer les valeurs manquantes d'une colonne avec la moyenne de cette colonne.

            Args:
                df (pd.DataFrame): Le DataFrame contenant les données.
                column (str): Le nom de la colonne à imputer.

            Returns:
                pd.DataFrame: Le DataFrame avec les valeurs manquantes imputées.
        """
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
        return df