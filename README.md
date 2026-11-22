# Object-Oriented-Programming-16-09

Cours ESSEC / CentraleSupelec : Object-Oriented Programming & Design Patterns in Python (Benjamin Dallard).

Exercices du cours, un dossier par exo.

| Dossier | Slide | Contenu |
|---|---|---|
| 01-bash/ | 18 | Script Bash qui installe un environnement de dev (git, python, venv, pytest) |
| 02-git/ | 26 | Reponses a l'exo Git en 11 parties, script qui rejoue le workflow, questions de reflexion |
| 03-oop/ | 67 | Surcharge d'operateurs et heritage, avec tests |
| 04-uml/ | 68 | Hospital Management et ABCD Records en diagrammes Mermaid |
| 05-design-patterns/ | 84 | Singleton, Factory, Builder, Adapter, Decorator, Facade, Observer, Strategy, Template Method |
| 06-testing/ | 93 | Tests unitaires avec mock d'un client LLM |

## Lancer les tests

```
pip install -r requirements.txt
python -m pytest
python 05-design-patterns/patterns.py
```

Python 3.10+. Aucun test n'appelle de vraie API.
