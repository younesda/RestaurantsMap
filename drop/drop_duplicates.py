import pandas as pd

class DropDuplicates:
    """
    Classe pour supprimer les doublons dans un DataFrame pandas.
    """

    @staticmethod
    def drop_duplicates(df: pd.DataFrame):
        """
        Supprime les doublons dans le DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à traiter.

        Returns:
            pd.DataFrame: Un nouveau DataFrame sans doublons.
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("L'argument doit être un DataFrame pandas.")
        df_sans_doublons = df.drop_duplicates()
        print(f"Nombre de lignes avant suppression des doublons : {len(df)}")
        print(f"Nombre de lignes après suppression des doublons : {len(df_sans_doublons)}")
        return df_sans_doublons