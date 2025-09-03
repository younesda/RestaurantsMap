import pandas as pd

class DetecteurZScore:
    """
    Classe pour détecter les anomalies dans un DataFrame pandas en utilisant la méthode du Z-Score.
    """

    @staticmethod
    def detecter_anomalies_z_score(df: pd.DataFrame, threshold: float = 3.0):
        """
        Détecte les anomalies dans un DataFrame en utilisant la méthode du Z-Score.

        Args:
            df (pd.DataFrame): Le DataFrame à analyser.
            threshold (float): Le seuil de Z-Score pour considérer une valeur comme une anomalie.

        Returns:
            pd.DataFrame: Un DataFrame contenant les lignes considérées comme des anomalies.
        """   
        z_scores = (df - df.mean()) / df.std()
        anomalies = df[(z_scores.abs() > threshold).any(axis=1)]
        if anomalies.empty:
            return "Aucune anomalie détectée."
        return anomalies