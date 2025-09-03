import pandas as pd

class ChangeType:
    """
    Classe pour changer le type de données des colonnes dans un DataFrame pandas.
    """

    @staticmethod
    def changer_type_colonne(df: pd.DataFrame, column: str, new_type: str):
        """
        Change le type de données d'une colonne spécifique dans un DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à modifier.
            column (str): La colonne dont le type doit être changé.
            new_type (str): Le nouveau type de données (e.g., 'int', 'float', 'str').

        Returns:
            pd.DataFrame: Le DataFrame avec le type de la colonne modifié.
        """
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' n'existe pas dans le DataFrame.")
        try:
            df[column] = df[column].astype(new_type)
        except ValueError as e:
            raise ValueError(f"Erreur lors du changement de type: {e}")
        return df