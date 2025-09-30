"""
Municipal Governance Analysis Framework - Core Module
Mixed-Methods Framework für kommunale Digitalisierungs-Governance-Analyse
"""

__version__ = "1.0.0"
__author__ = "Governance Research Team"

from typing import Dict, List, Optional, Any, Tuple
import pandas as pd
import numpy as np
import logging
from pathlib import Path
import json

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GovernanceAnalyzer:
    """
    Haupt-Framework-Klasse für Mixed-Methods Governance-Analyse.

    Verbindet quantitative NLP-Analyse mit qualitativer Stellenplan-Vertiefung
    über 120 deutsche Kommunen in 4 theoretischen Governance-Dimensionen.
    """

    def __init__(self, config_path: Optional[str] = None):
        """Initialize Governance Analyzer."""
        self.config_path = config_path or "config/settings.yaml"
        self.governance_dimensions = {
            "macht": {
                "description": "IT-Abhängigkeiten und Vendor-Kontrolle",
                "keywords": ["IT-Vergabe", "externe Dienstleister", "Cloud-Anbieter", 
                           "Vendor", "Abhängigkeit", "Microsoft", "SAP"],
                "color": "#E74C3C"
            },
            "legitimation": {
                "description": "Transparenz und demokratische Teilhabe", 
                "keywords": ["Bürgerbeteiligung", "Transparenz", "Open Data", 
                           "Partizipation", "Vertrauen", "Rechenschaft"],
                "color": "#3498DB"
            },
            "institution": {
                "description": "Pfadabhängigkeiten und Wandelfähigkeit",
                "keywords": ["Verfahren", "Zuständigkeit", "Modernisierung", 
                           "Legacy-System", "Wandel", "Innovation"],
                "color": "#F39C12"
            },
            "souveraenitaet": {
                "description": "Digitale Selbstbestimmung und OSS-Adoption",
                "keywords": ["digitale Souveränität", "Open Source", "Eigenentwicklung", 
                           "Unabhängigkeit", "Kontrolle", "Linux"],
                "color": "#27AE60"
            }
        }

        logger.info("🏛️ Governance Analyzer initialized")

    def analyze_municipality(self, municipality_name: str) -> Dict[str, Any]:
        """
        Analysiere eine spezifische Kommune über alle 4 Governance-Dimensionen.

        Args:
            municipality_name: Name der Kommune

        Returns:
            Dict mit Governance-Scores und Analyse-Ergebnissen
        """
        logger.info(f"Analyzing municipality: {municipality_name}")

        # Placeholder für echte Implementierung
        analysis_result = {
            "municipality": municipality_name,
            "timestamp": pd.Timestamp.now().isoformat(),
            "governance_scores": {
                dim: np.random.uniform(0.3, 0.95) 
                for dim in self.governance_dimensions
            },
            "overall_score": np.random.uniform(0.5, 0.9),
            "data_quality": "simulated",
            "methodology": "mixed_methods"
        }

        return analysis_result

    def compare_municipalities(self, 
                             municipality_names: List[str]) -> pd.DataFrame:
        """
        Vergleiche mehrere Kommunen über alle Governance-Dimensionen.

        Args:
            municipality_names: Liste der zu vergleichenden Kommunen

        Returns:
            DataFrame mit Vergleichsergebnissen
        """
        logger.info(f"Comparing {len(municipality_names)} municipalities")

        results = []
        for name in municipality_names:
            result = self.analyze_municipality(name)
            result.update(result.pop("governance_scores"))
            results.append(result)

        return pd.DataFrame(results)

    def get_available_municipalities(self) -> List[Dict[str, Any]]:
        """
        Hole Liste aller verfügbaren Kommunen aus der 120-Städte-Datenbank.

        Returns:
            Liste mit Kommunen-Metadaten
        """
        # Placeholder - würde echte Konfigurationsdatei laden
        municipalities = [
            {"name": "München", "bundesland": "Bayern", "population": 1500000},
            {"name": "Kiel", "bundesland": "Schleswig-Holstein", "population": 247000},
            {"name": "Köln", "bundesland": "Nordrhein-Westfalen", "population": 1100000}
        ]

        return municipalities

    def generate_governance_report(self, 
                                 municipality_name: str,
                                 include_recommendations: bool = True) -> Dict[str, Any]:
        """
        Erstelle umfassenden Governance-Report für eine Kommune.

        Args:
            municipality_name: Name der Kommune
            include_recommendations: Ob Handlungsempfehlungen inkludiert werden sollen

        Returns:
            Umfassender Governance-Report
        """
        analysis = self.analyze_municipality(municipality_name)

        report = {
            "municipality": municipality_name,
            "executive_summary": f"Governance-Analyse für {municipality_name}",
            "governance_profile": analysis["governance_scores"],
            "overall_rating": analysis["overall_score"],
            "strengths": [],
            "development_areas": [],
            "methodology_note": "Mixed-Methods: Quantitative NLP + Qualitative Stellenplan-Analyse"
        }

        if include_recommendations:
            report["recommendations"] = [
                "Governance-Strukturen in Stellenplänen stärken",
                "Mixed-Methods-Ansatz für kontinuierliches Monitoring",
                "Diskurs-Struktur-Kongruenz verbessern"
            ]

        return report

class MunicipalityDatabase:
    """
    Verwaltung der 120-Kommunen-Datenbank mit Metadaten und Konfigurationen.
    """

    def __init__(self, data_file: str = "config/municipalities_120_stratified.json"):
        """Initialize municipality database."""
        self.data_file = data_file
        self.municipalities = self._load_municipalities()
        logger.info(f"📊 Municipality database loaded: {len(self.municipalities)} cities")

    def _load_municipalities(self) -> Dict[str, Any]:
        """Load municipality data from configuration file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Municipality data file not found: {self.data_file}")
            return {"municipalities": {}}

    def get_municipality(self, name: str) -> Optional[Dict[str, Any]]:
        """Get specific municipality data."""
        municipalities = self.municipalities.get("municipalities", {})

        # Fuzzy search
        for key, muni in municipalities.items():
            if muni.get("name", "").lower() == name.lower():
                return muni

        return None

    def filter_municipalities(self, 
                            bundesland: Optional[str] = None,
                            min_population: Optional[int] = None,
                            ris_system: Optional[str] = None,
                            api_available: Optional[bool] = None) -> List[Dict[str, Any]]:
        """Filter municipalities by criteria."""
        municipalities = list(self.municipalities.get("municipalities", {}).values())

        if bundesland:
            municipalities = [m for m in municipalities if m.get("bundesland") == bundesland]

        if min_population:
            municipalities = [m for m in municipalities if m.get("population", 0) >= min_population]

        if ris_system:
            municipalities = [m for m in municipalities if m.get("ris_system") == ris_system]

        if api_available is not None:
            municipalities = [m for m in municipalities if m.get("api_available") == api_available]

        return municipalities

# Convenience Imports
from .nlp_analyzer import QuantitativeNLPAnalyzer
from .stellenplan_analyzer import QualitativeStellenpladrivenAnalyzer  
from .mixed_methods import MixedMethodsIntegrator

# Main API Functions
def analyze_governance(municipality: str) -> Dict[str, Any]:
    """Quick analysis function."""
    analyzer = GovernanceAnalyzer()
    return analyzer.analyze_municipality(municipality)

def compare_governance(municipalities: List[str]) -> pd.DataFrame:
    """Quick comparison function.""" 
    analyzer = GovernanceAnalyzer()
    return analyzer.compare_municipalities(municipalities)

def get_municipalities_database() -> MunicipalityDatabase:
    """Get municipality database instance."""
    return MunicipalityDatabase()

__all__ = [
    "GovernanceAnalyzer",
    "MunicipalityDatabase", 
    "QuantitativeNLPAnalyzer",
    "QualitativeStellenpladrivenAnalyzer",
    "MixedMethodsIntegrator",
    "analyze_governance",
    "compare_governance", 
    "get_municipalities_database"
]
