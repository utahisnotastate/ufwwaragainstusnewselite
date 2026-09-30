# Translations

Each language has its own self-contained copy of the curriculum. Pages are **not** mixed — open the folder for the language you want and read only that version.

Every language folder now matches the English three-layer layout: story lesson (`readme.md`), reality check (`SCIENCE.md`), and in-universe proof (`PHYSICS_PROOF.md`). Lab code (`simulation.py`) stays at the English module folders in the repository root; translated pages link to those files.

| Language | Folder | Start here |
|----------|--------|------------|
| English (original) | [`/`](../) (repository root) | [`README.md`](../README.md) |
| Estonian | [`Estonian/`](Estonian/) | [`Estonian/README.md`](Estonian/README.md) |
| Finnish | [`Finnish/`](Finnish/) | [`Finnish/README.md`](Finnish/README.md) |
| Russian | [`Russian/`](Russian/) | [`Russian/README.md`](Russian/README.md) |
| Japanese | [`Japanese/`](Japanese/) | [`Japanese/README.md`](Japanese/README.md) |
| Chinese (Simplified) | [`Chinese/`](Chinese/) | [`Chinese/README.md`](Chinese/README.md) |

## Folder layout (every language)

```
translations/<Language>/
├── README.md
├── ABOUT.md
├── CONTRIBUTING.md
├── Module_01_Zero_Point_Energy/
│   ├── readme.md
│   ├── PHYSICS_PROOF.md
│   ├── SCIENCE.md
│   └── ZEO_ARCHITECT_ANALYSIS.md
├── Module_02_Gravity_Is_Pushing/
│   ├── readme.md
│   ├── PHYSICS_PROOF.md
│   └── SCIENCE.md
├── … (Modules 03–12, same pattern)
└── Module_12_The_Psychotronic_Internet/
    ├── readme.md
    ├── PHYSICS_PROOF.md
    └── SCIENCE.md
```

Module folder names match the English originals so paths stay predictable across languages. Run labs from the repository root, for example:

```bash
python Module_01_Zero_Point_Energy/simulation.py
python -m pytest
```
