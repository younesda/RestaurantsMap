import pandas as pd

class DetecteurIsolationForest:
    """
    Classe pour détecter les anomalies dans un DataFrame pandas en utilisant la méthode de l'Isolation Forest.
    """

    @staticmethod
    def detecter_anomalies_isolation_forest(df: pd.DataFrame, contamination: float = 0.01):
        """
        Détecte les anomalies dans un DataFrame en utilisant la méthode de l'Isolation Forest.

        Args:
            df (pd.DataFrame): Le DataFrame à analyser.
            contamination (float): La proportion estimée d'anomalies dans les données.

        Returns:
            pd.DataFrame: Un DataFrame contenant les lignes considérées comme des anomalies.
        """
        from sklearn.ensemble import IsolationForest

        model = IsolationForest(contamination=contamination, random_state=42)
        model.fit(df)
        df['anomaly'] = model.predict(df)
        anomalies = df[df['anomaly'] == -1].drop(columns=['anomaly'])
        
        if anomalies.empty:
            return "Aucune anomalie détectée."
        
        return anomalies