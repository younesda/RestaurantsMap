import pandas as pd

class Doublon:
    """
    Classe pour gérer les doublons dans un DataFrame pandas.
    """

    @staticmethod
    def calcul_doublons(df: pd.DataFrame):
        """
        Calcule le nombre de doublons dans le DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à analyser.

        Returns:
            res: Nombre de doublons dans le DataFrame.
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("L'argument doit être un DataFrame pandas.")
        if df.duplicated().sum() == 0:
            return "Il n'y a pas de doublons dans le DataFrame."
        res = df.duplicated().sum()
        return res