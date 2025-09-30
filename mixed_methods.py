"""
Mixed-Methods Integration für Governance-Analyse.
Verbindet quantitative NLP-Befunde mit qualitativen Stellenplan-Analysen.
"""

from typing import Dict, List, Optional, Any, Tuple
import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class MixedMethodsIntegrator:
    """
    Integriert quantitative NLP-Analyse mit qualitativer Stellenplan-Vertiefung.

    Kern des Mixed-Methods-Ansatzes: Erklärt quantitative Muster durch
    qualitative organisatorische Strukturen.
    """

    def __init__(self):
        """Initialize Mixed Methods Integrator."""
        self.integration_strategies = {
            "sequential": "Quantitative Phase → Case Selection → Qualitative Vertiefung",
            "concurrent": "Parallele quantitative und qualitative Analyse",
            "explanatory": "Qualitative Erklärung quantitativer Muster"
        }

        logger.info("🔄 Mixed Methods Integrator initialized")

    def select_cases_for_qualitative_analysis(self, 
                                            quantitative_results: pd.DataFrame,
                                            n_cases: int = 12,
                                            strategy: str = "extreme_cases") -> List[Dict[str, Any]]:
        """
        Wähle Kommunen für qualitative Stellenplan-Vertiefung basiert auf quantitativen NLP-Ergebnissen.

        Args:
            quantitative_results: DataFrame mit NLP-Governance-Scores
            n_cases: Anzahl der auszuwählenden Cases
            strategy: Case-Selection-Strategie

        Returns:
            Liste der ausgewählten Cases für qualitative Analyse
        """
        logger.info(f"Selecting {n_cases} cases using {strategy} strategy")

        if strategy == "extreme_cases":
            return self._select_extreme_cases(quantitative_results, n_cases)
        elif strategy == "typical_cases":
            return self._select_typical_cases(quantitative_results, n_cases)
        elif strategy == "deviant_cases":
            return self._select_deviant_cases(quantitative_results, n_cases)
        else:
            return self._select_mixed_cases(quantitative_results, n_cases)

    def _select_extreme_cases(self, data: pd.DataFrame, n_cases: int) -> List[Dict[str, Any]]:
        """Wähle Extreme Cases (high/low performer pro Bundesland)."""
        selected = []
        cases_per_bl = n_cases // 3

        for bundesland in ["Bayern", "Schleswig-Holstein", "Nordrhein-Westfalen"]:
            bl_data = data[data['bundesland'] == bundesland]

            if len(bl_data) > 0:
                # High Performer (2 Cases)
                high = bl_data.nlargest(2, 'governance_index_nlp')
                selected.extend(high.to_dict('records'))

                # Low Performer (1 Case)  
                low = bl_data.nsmallest(1, 'governance_index_nlp')
                selected.extend(low.to_dict('records'))

                # Typical Case (1 Case - nahe Median)
                median_val = bl_data['governance_index_nlp'].median()
                typical = bl_data.iloc[(bl_data['governance_index_nlp'] - median_val).abs().argsort()[:1]]
                selected.extend(typical.to_dict('records'))

        return selected[:n_cases]

    def analyze_discourse_structure_congruence(self,
                                             nlp_results: pd.DataFrame,
                                             stellenplan_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analysiere Kongruenz zwischen NLP-Diskursen und Stellenplan-Strukturen.

        Args:
            nlp_results: Quantitative NLP-Ergebnisse
            stellenplan_results: Qualitative Stellenplan-Befunde

        Returns:
            Kongruenz-Analyse mit Gap-Identifikation
        """
        logger.info("Analyzing discourse-structure congruence")

        congruence_analysis = {
            "total_cases": len(stellenplan_results),
            "high_congruence": 0,
            "medium_congruence": 0, 
            "low_congruence": 0,
            "gaps_identified": [],
            "patterns": {}
        }

        for stellenplan_case in stellenplan_results:
            kommune_name = stellenplan_case['name']

            # Finde entsprechende NLP-Daten
            nlp_case = nlp_results[nlp_results['name'] == kommune_name]

            if not nlp_case.empty:
                nlp_row = nlp_case.iloc[0]

                # Berechne Kongruenz-Score
                congruence_score = self._calculate_congruence_score(nlp_row, stellenplan_case)
                stellenplan_case['congruence_score'] = congruence_score

                # Kategorisiere Kongruenz
                if congruence_score >= 0.7:
                    congruence_analysis["high_congruence"] += 1
                elif congruence_score >= 0.4:
                    congruence_analysis["medium_congruence"] += 1
                else:
                    congruence_analysis["low_congruence"] += 1
                    # Gap identifiziert
                    gap = {
                        "municipality": kommune_name,
                        "discourse_pattern": self._describe_nlp_pattern(nlp_row),
                        "structure_pattern": self._describe_stellenplan_pattern(stellenplan_case),
                        "gap_type": self._identify_gap_type(nlp_row, stellenplan_case)
                    }
                    congruence_analysis["gaps_identified"].append(gap)

        return congruence_analysis

    def _calculate_congruence_score(self, nlp_data: pd.Series, stellenplan_data: Dict[str, Any]) -> float:
        """Berechne Kongruenz zwischen NLP- und Stellenplan-Befunden."""

        # Dimensionale Kongruenz prüfen
        congruence_points = 0
        total_dimensions = 4

        # Macht: Hohe NLP-Macht-Keywords + CIO-Struktur im Stellenplan
        if (nlp_data.get('macht_keywords', 0) > 20) == (stellenplan_data.get('cio_struktur') == 'vorhanden'):
            congruence_points += 1

        # Legitimation: Hohe NLP-Legitimations-Keywords + Partizipationsbeauftragte
        if (nlp_data.get('legitimation_keywords', 0) > 15) == (stellenplan_data.get('partizipationsbeauftragte') == 'etabliert'):
            congruence_points += 1

        # Institution: Hohe NLP-Institutions-Keywords + Change Management
        if (nlp_data.get('institution_keywords', 0) > 18) == (stellenplan_data.get('change_management') == 'strukturiert'):
            congruence_points += 1

        # Souveränität: Hohe NLP-Souveränitäts-Keywords + IT-Sicherheits-Governance
        if (nlp_data.get('souveraenitaet_keywords', 0) > 12) == (stellenplan_data.get('it_sicherheit_governance') == 'CISO etabliert'):
            congruence_points += 1

        return congruence_points / total_dimensions

    def develop_governance_typology(self,
                                  quantitative_patterns: pd.DataFrame,
                                  qualitative_structures: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Entwickle Governance-Typologie basiert auf Mixed-Methods-Befunden.

        Args:
            quantitative_patterns: NLP-basierte Governance-Muster
            qualitative_structures: Stellenplan-basierte Governance-Strukturen

        Returns:
            Governance-Typologie mit Charakteristika
        """
        logger.info("Developing governance typology")

        # Klassifiziere jede Kommune
        classified_municipalities = []

        for struktur in qualitative_structures:
            kommune_name = struktur['name']

            # Finde NLP-Daten
            nlp_data = quantitative_patterns[quantitative_patterns['name'] == kommune_name]

            if not nlp_data.empty:
                nlp_row = nlp_data.iloc[0]
                gov_type = self._classify_governance_type(nlp_row, struktur)

                classified_municipalities.append({
                    'name': kommune_name,
                    'bundesland': struktur['bundesland'],
                    'governance_type': gov_type,
                    'nlp_score': nlp_row.get('governance_index_nlp', 0),
                    'structural_characteristics': self._extract_structural_chars(struktur)
                })

        # Entwickle Typologie
        typologie = {}
        for muni in classified_municipalities:
            gov_type = muni['governance_type']
            if gov_type not in typologie:
                typologie[gov_type] = {
                    "count": 0,
                    "municipalities": [],
                    "characteristics": set(),
                    "avg_nlp_score": 0
                }

            typologie[gov_type]["count"] += 1
            typologie[gov_type]["municipalities"].append(muni['name'])
            typologie[gov_type]["characteristics"].update(muni['structural_characteristics'])

        # Berechne Durchschnittswerte
        for gov_type in typologie:
            type_munis = [m for m in classified_municipalities if m['governance_type'] == gov_type]
            if type_munis:
                typologie[gov_type]["avg_nlp_score"] = np.mean([m['nlp_score'] for m in type_munis])
                typologie[gov_type]["characteristics"] = list(typologie[gov_type]["characteristics"])

        return {
            "typology": typologie,
            "classified_municipalities": classified_municipalities,
            "summary": {
                "total_types": len(typologie),
                "most_common_type": max(typologie.keys(), key=lambda k: typologie[k]["count"]),
                "methodology": "Mixed-Methods Classification based on NLP + Stellenplan"
            }
        }

    def _classify_governance_type(self, nlp_data: pd.Series, stellenplan_data: Dict[str, Any]) -> str:
        """Klassifiziere Governance-Typ basiert auf NLP + Stellenplan."""

        nlp_score = nlp_data.get('governance_index_nlp', 0)

        # High-Performance + Innovative Strukturen
        if nlp_score > 16 and stellenplan_data.get('innovationsbereitschaft') == 'hoch':
            return "Digitale Vorreiter"

        # High-Performance + Hierarchische Strukturen
        elif nlp_score > 14 and stellenplan_data.get('hierarchie_niveau') == 'hoch':
            return "Strukturiert-Konservativ"

        # Legitimation-dominiert
        elif nlp_data.get('legitimation_keywords', 0) > nlp_data.get('macht_keywords', 0):
            return "Partizipationsorientiert"

        # Souveränität-fokussiert
        elif stellenplan_data.get('it_sicherheit_governance') == 'CISO etabliert':
            return "Souveränitätsfokussiert"

        # Default
        else:
            return "Mainstream-Digitalisierer"

    def generate_mixed_methods_report(self,
                                    quantitative_results: pd.DataFrame,
                                    qualitative_results: List[Dict[str, Any]],
                                    integration_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Erstelle umfassenden Mixed-Methods-Report."""

        report = {
            "methodology": {
                "approach": "Sequential Explanatory Mixed-Methods",
                "quantitative_phase": "NLP-Analyse von 120 Ratsinformationssystemen",
                "qualitative_phase": "Stellenplan-Analyse von 12 ausgewählten Kommunen",
                "integration": "Diskurs-Struktur-Kongruenz-Analyse"
            },
            "quantitative_summary": {
                "total_municipalities": len(quantitative_results),
                "avg_governance_score": quantitative_results['governance_index_nlp'].mean(),
                "top_performer": quantitative_results.loc[quantitative_results['governance_index_nlp'].idxmax(), 'name'],
                "methodology_note": "BERTopic NLP + Governance-Keywords-Extraktion"
            },
            "qualitative_summary": {
                "case_studies": len(qualitative_results),
                "governance_structures_identified": len([r for r in qualitative_results if r.get('cio_struktur') == 'vorhanden']),
                "methodology_note": "Stellenplan-Dokumentenanalyse + Governance-Strukturen-Mapping"
            },
            "integration_findings": integration_analysis,
            "implications": self._derive_policy_implications(integration_analysis),
            "limitations": [
                "Stellenplan-Analyse basiert auf dokumentierten Strukturen (nicht gelebte Praxis)",
                "NLP-Analyse spiegelt diskursive Muster wider (nicht Implementierungsqualität)",
                "12 Cases für qualitative Vertiefung (nicht vollständige Abdeckung)"
            ],
            "future_research": [
                "Longitudinale Analyse der Diskurs-Struktur-Entwicklung 2018-2024",
                "Erweiterung auf alle 403 kreisfreien Städte Deutschlands",
                "Integration von Performance-Indikatoren (OZG-Umsetzung, Digitalisierungsindex)"
            ]
        }

        return report

    def _derive_policy_implications(self, integration_analysis: Dict[str, Any]) -> List[str]:
        """Leite Policy-Implikationen aus Mixed-Methods-Befunden ab."""

        implications = []

        # Gap-basierte Empfehlungen
        if integration_analysis.get("gaps_identified"):
            implications.append("🔄 Diskurs-Struktur-Gaps schließen: Governance-Diskurse in Stellenstrukturen überführen")

        # Kongruenz-basierte Empfehlungen
        high_congruence = integration_analysis.get("high_congruence", 0)
        total_cases = integration_analysis.get("total_cases", 12)

        if high_congruence / total_cases < 0.5:
            implications.append("⚖️ Governance-Kohärenz stärken: Diskurs und Struktur besser aufeinander abstimmen")

        implications.extend([
            "📋 Stellenplan-Governance-Standards: Mindestausstattung für digitale Governance definieren",
            "🏛️ Mixed-Methods-Monitoring: Kontinuierliche Diskurs-Struktur-Analyse etablieren",
            "🤝 Interkommunaler Austausch: Best Practices bei Governance-Strukturen teilen"
        ])

        return implications

__all__ = ["MixedMethodsIntegrator"]
