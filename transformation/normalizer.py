import pandas as pd

class Normalizer:
    """
    Classe pour normaliser les données dans un DataFrame pandas. Avec la méthode Min-Max.
    """

    @staticmethod
    def normaliser_donnees(df: pd.DataFrame, column: str):
        """
        Normalise les données d'une colonne spécifique dans un DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à normaliser.
            column (str): La colonne à normaliser.  
        
        Returns:
            pd.Series: Une série pandas contenant les données normalisées.
        """
        col = df[column]
        normalizer =  (col - col.min()) / (col.max() - col.min())
        return normalizer