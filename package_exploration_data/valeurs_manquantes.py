import pandas as pd

class ValeursManquantes:
    """
    Classe pour gérer les valeurs manquantes dans un DataFrame pandas.
    """

    @staticmethod
    def calculer_valeurs_manquantes(df: pd.DataFrame):
        """
        Calcule le nombre de valeurs manquantes dans chaque colonne du DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à analyser.

        Returns:
            res: Nombre de valeurs manquantes dans le DataFrame.
        """
        
        if not isinstance(df, pd.DataFrame):
            raise ValueError("L'argument doit être un DataFrame pandas.")   
        if df.empty:
            return "Le DataFrame est vide."
        if df.isnull().sum().sum() == 0:
            return "Il n'y a pas de valeurs manquantes dans le DataFrame."
        res = df.isnull().sum()
        return res        