# 🍽️ Restaurants Map

## 📌 Description
Ce projet consiste à créer une **carte des restaurants** en utilisant des données stockées dans **MongoDB**, puis à les **exporter avec PyMongo**, effectuer un **data cleaning** via des packages personnalisés, et enfin préparer les données pour des analyses ou une visualisation.

---

## 🚀 Fonctionnalités
- Extraction des données depuis **MongoDB** avec **PyMongo**
- Nettoyage et normalisation des données avec un **package custom Python**
- Organisation des données en fichiers propres pour analyse
- Visualisation des restaurants sur une carte (HTML)

---

## 🛠️ Technologies utilisées
- **MongoDB** (Base NoSQL)
- **PyMongo** (Connexion et extraction)
- **Python** (Pandas, custom package)
- **Folium** (Cartographie)
- **Jupyter Notebook** (Exploration)

---

## 📂 StructurRestaurantsMap/
├── anomalies/ # Détection des anomalies (Isolation Forest, Z-score)
├── connexion/ # Connexion à MongoDB
├── drop/ # Fonctions de suppression (NA, doublons)
├── imputation/ # Fonctions d'imputation (moyenne, médiane, mode)
├── package_exploration_data/ # Exploration (valeurs manquantes, doublons)
├── transformation/ # Transformation (type, rename, normalisation)
├── restaurants.ipynb # Notebook principal
├── restaurants_map.html # Carte des restaurants
├── top20_restaurants_map.html # Carte des top 20 restaurants
└── requirements.txt # Dépendances Python


---

## ⚙️ Installation et Configuration

### **Cloner le projet**
```bash
git clone https://github.com/younesda/RestaurantsMap.git
cd RestaurantsMap

### **Installer les dépendances**
pip install -r requirements.txt

### **Exporter les données depuis MongoDB**
python connexion/conn_mongo.py

### **Nettoyer les données**


🔥 Auteur

Younes Hachami – LinkedIn