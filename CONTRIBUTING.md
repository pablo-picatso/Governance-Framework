# Contributing to Municipal Governance Framework

🎉 Vielen Dank für Ihr Interesse am Municipal Governance Framework! 

## 🎯 Übersicht

Dieses Framework dient der wissenschaftlichen Analyse kommunaler Digitalisierungs-Governance. Beiträge sind in folgenden Bereichen besonders willkommen:

- 📊 **Datenquellen-Erweiterung**: Neue RIS-Systeme, Open Data-Portale
- 🔬 **Methodische Verbesserungen**: NLP-Algorithmen, Analysemethoden
- 🏛️ **Kommunen-Abdeckung**: Weitere Bundesländer, internationale Kommunen
- 📚 **Dokumentation**: Beispiele, Tutorials, API-Dokumentation

## 🚀 Quick Start für Contributors

### 1. Development Environment Setup

```bash
# Repository forken und klonen
git clone https://github.com/YOUR_USERNAME/municipal-governance-framework.git
cd municipal-governance-framework

# Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Development Dependencies
pip install -e ".[dev]"

# Pre-commit Hooks installieren
pre-commit install
```

### 2. Framework verstehen

```python
# Framework-Architektur erkunden
from governance_framework import GovernanceAnalyzer

analyzer = GovernanceAnalyzer()
print(analyzer.governance_dimensions)

# 120-Kommunen-Datenbank
from governance_framework import get_municipalities_database
db = get_municipalities_database()
print(f"Verfügbar: {len(db.municipalities)} Kommunen")
```

### 3. Tests schreiben und ausführen

```bash
# Alle Tests ausführen
pytest

# Spezifische Tests
pytest tests/test_core.py -v

# Coverage Report
pytest --cov=governance_framework --cov-report=html
```

## 🏗️ Architektur & Module

```
src/governance_framework/
├── core.py                 # Basis-Framework (GovernanceAnalyzer, MunicipalityDatabase)
├── nlp_analyzer.py         # Quantitative NLP-Pipeline
├── stellenplan_analyzer.py # Qualitative Stellenplan-Analyse  
├── mixed_methods.py        # Integration quant./qual. Methoden
├── data_collectors.py      # RIS-Scraper, Datensammlung
├── visualizations.py       # Charts, Plots, Dashboards
└── cli.py                  # Command Line Interface
```

## 📊 Datenstrukturen

### Kommunen-Datenbank Schema:
```json
{
  "name": "String",
  "bundesland": "String", 
  "population": "Integer",
  "ris_system": "String",
  "api_available": "Boolean",
  "governance_scores": {
    "macht": "Float",
    "legitimation": "Float", 
    "institution": "Float",
    "souveraenitaet": "Float"
  }
}
```

### NLP-Ergebnisse Schema:
```json
{
  "municipality": "String",
  "governance_keywords": {
    "macht_keywords": "Integer",
    "legitimation_keywords": "Integer",
    "institution_keywords": "Integer", 
    "souveraenitaet_keywords": "Integer"
  },
  "topics": "Array",
  "sentiment_scores": "Object"
}
```

## 🤝 Contribution Types

### 🔬 **Methodische Verbesserungen**
- Neue NLP-Algorithmen (z.B. GPT-basierte Analyse)
- Erweiterte Stellenplan-Parser
- Statistische Analysemethoden
- Mixed-Methods-Integrationsstrategien

### 📊 **Datenquellen-Erweiterung**  
- Neue RIS-System-Unterstützung
- Zusätzliche Open Data-Portale
- Haushaltsplan-Parser
- API-Konnektoren

### 🏛️ **Kommunen-Abdeckung**
- Weitere Bundesländer
- Internationale Kommunen
- Spezialkommumen (Landkreise, etc.)

### 📚 **Dokumentation & Beispiele**
- Jupyter Notebooks
- Colab-Templates  
- API-Dokumentation
- Methodische Tutorials

## ✅ Code Quality Standards

### Code Style:
```bash
# Formatting
black src/

# Linting  
flake8 src/

# Type Checking
mypy src/
```

### Testing Guidelines:
- **Unit Tests**: Für alle neuen Funktionen
- **Integration Tests**: Für API-Endpunkte
- **Docstring Tests**: Für komplexe Algorithmen
- **>80% Coverage**: Für neue Module

### Documentation Standards:
- **Docstrings**: Google Style für alle Public Functions
- **Type Hints**: Für alle Function Parameters & Returns
- **README Updates**: Für neue Features
- **Changelog**: Für alle Breaking Changes

## 🔄 Development Workflow

### 1. Issue-based Development:
```bash
# Neuen Branch für Issue erstellen
git checkout -b feature/issue-123-stellenplan-parser

# Entwicklung + Tests
# ... Code changes ...

# Commit mit Issue-Referenz
git commit -m "feat: Add Stellenplan PDF parser (closes #123)"
```

### 2. Pull Request Guidelines:
- **Beschreibung**: Klare Beschreibung der Änderungen
- **Tests**: Alle Tests müssen passieren
- **Documentation**: Neue Features dokumentieren
- **Breaking Changes**: In PR-Titel kennzeichnen

### 3. Review Process:
- **Code Review**: Mind. 1 Reviewer erforderlich
- **CI/CD**: Alle Checks müssen grün sein
- **Manual Testing**: Besonders für UI/UX-Änderungen

## 🌟 Spezielle Contribution-Bereiche

### 🔬 **Für Wissenschaftler**:
- Methodische Paper-Implementierungen
- Benchmark-Datasets erstellen
- Validation Studies durchführen
- Peer Review von Algorithmen

### 💻 **Für Entwickler**:
- Performance-Optimierungen
- API-Erweiterungen  
- Frontend/Dashboard-Entwicklung
- CI/CD-Pipeline-Verbesserungen

### 🏛️ **Für Praktiker**:
- Real-world Use Cases
- User Experience-Feedback
- Domain-spezifische Validierung
- Policy-Implikationen bewerten

## 📞 Contact & Community

- **GitHub Discussions**: Für allgemeine Fragen
- **GitHub Issues**: Für Bugs und Feature Requests
- **Email**: governance-framework@research.org
- **Twitter**: @GovernanceFramework

## 🎓 Academic Contributions

Das Framework wird für wissenschaftliche Publikationen verwendet. Bei substantiellen Beiträgen können Contributors als Co-Autoren wissenschaftlicher Papers aufgenommen werden.

### Citation für Contributors:
```bibtex
@software{municipal_governance_framework,
  title = {Municipal Governance Analysis Framework},
  author = {Governance Research Team and Contributors},
  year = {2024},
  url = {https://github.com/governance-research/municipal-governance-framework}
}
```

---

**🏛️ Gemeinsam schaffen wir bessere Tools für die Analyse kommunaler Governance. Vielen Dank für Ihren Beitrag! 🚀**
