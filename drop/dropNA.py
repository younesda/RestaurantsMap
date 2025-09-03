import pandas as pd

class DropNA:   
    @staticmethod
    def drop_na(df: pd.DataFrame):
        """
        Supprime les valeurs NA dans le DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à traiter.

        Returns:
            pd.DataFrame: Un nouveau DataFrame sans valeurs NA.
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("L'argument doit être un DataFrame pandas.")
        df_sans_na = df.dropna()
        print(f"Nombre de lignes avant suppression des NA : {len(df)}")
        print(f"Nombre de lignes après suppression des NA : {len(df_sans_na)}")
        return df_sans_na