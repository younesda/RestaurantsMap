import pandas as pd

class RenameColumns:
    """
    Classe pour renommer les colonnes dans un DataFrame pandas.
    """

    @staticmethod
    def renommer_colonnes(df: pd.DataFrame, nouvelles_colonnes: list):
        """
        Renomme les colonnes d'un DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à modifier.
            nouvelles_colonnes (list): La liste des nouveaux noms de colonnes.

        Returns:
            pd.DataFrame: Le DataFrame avec les colonnes renommées.
        """
        if len(nouvelles_colonnes) != len(df.columns):
            raise ValueError("Le nombre de nouveaux noms de colonnes doit correspondre au nombre de colonnes existantes.")
        df.columns = nouvelles_colonnes
        return df