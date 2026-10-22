# benchmark-pareto-audit

## Français

Calculer un front de Pareto en conservant les mesures manquantes.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m benchmark_pareto_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Compare des mesures ponctuelles ou intervalles par objectifs min/max. Sépare dominance certaine, dominance possible et mesures absentes ; ne crée pas un classement total arbitraire quand qualité et coût se compensent.

### Limites

Bornes rectangulaires déclarées, comparaison limitée aux lignes complètes ; sans calibration d’intervalles ni preuve de supériorité SOTA générale.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compute a Pareto frontier while retaining missing measurements.

Synthetic data; no network access or secret required.

```sh
python -m benchmark_pareto_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compares point or interval measurements under min/max objectives. Separates certain dominance, possible dominance and missing measurements; does not invent a total ranking when quality and cost trade off.

### Limits

Declared rectangular bounds, comparison limited to complete rows; no interval calibration or general SOTA superiority proof.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Calcular una frontera de Pareto conservando medidas faltantes.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m benchmark_pareto_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Compara medidas puntuales o intervalos con objetivos min/max. Separa dominación cierta, posible y medidas ausentes; no inventa ranking total cuando calidad y coste se compensan.

### Límites

Cotas rectangulares declaradas, comparación limitada a filas completas; sin calibración de intervalos ni prueba de superioridad SOTA general.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/gbesse/decision-taskfit
