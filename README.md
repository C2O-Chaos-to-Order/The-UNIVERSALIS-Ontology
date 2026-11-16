# The UNIVERSALIS Ontology

The Master Ontology of Human and Intelligence for UNIVERSALIS.

**Guiding principle:** *With Power, Comes Responsibility.*

**Current repository (dated 2026-11-10):** `C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology`. `main` is at `085fb79c8cb3ff42138d09aca8b4b2ebd8bf5d9d` (2026-10-25 7:49:23 AM CT (America/Chicago)). This is a public UNIVERSALIS satellite under the C2O-Chaos-to-Order organization.

## What is in this repository

On that `main` HEAD there are three files:

- `README.md` (this file)
- `Master_Ontology_Human_and_Intelligence.md` — canonical document text for Master Ontology (Human and Intelligence)
- `Master_Ontology_Human_and_Intelligence.docx` — companion Word copy, retained and not deleted

The Markdown file is the canonical text. The `.docx` is a convenience companion. If the two ever differ, prefer the Markdown unless the owner says otherwise.

## Related public UNIVERSALIS repositories

| Repository | What it holds |
|---|---|
| [The-UNIVERSALIS-Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem) | Public UNIVERSALIS product (`prototype/` and `scaffold/` on its `main`; LIMITED) |
| [Research-for-the-UNIVERSALIS-Ecosystem](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem) | Public UNIVERSALIS research workspace (packages currently in drafts) |
| [The-UNIVERSALIS-Human-Knowledge](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge) | Human Subjects of Knowledge (H-K) |
| [The-UNIVERSALIS-Human-Capabilities](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Capabilities) | Human Capabilities (H-C) |
| [The-UNIVERSALIS-Human-Skills](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Skills) | Human Skills (H-S) |
| [The-UNIVERSALIS-Human-Powers](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Powers) | Human Powers (H-P) |
| [The-UNIVERSALIS-Intelligence-Knowledge](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Knowledge) | Intelligence Subjects of Knowledge (I-K) |
| [The-UNIVERSALIS-Intelligence-Capabilities](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Capabilities) | Intelligence Capabilities (I-C) |
| [The-UNIVERSALIS-Intelligence-Skills](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills) | Intelligence Skills (I-S) |
| [The-UNIVERSALIS-Intelligence-Powers](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers) | Intelligence Powers (I-P) |
| [The-UNIVERSALIS-Ontology](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology) | Master Ontology: Human and Intelligence |
| [The-UNIVERSALIS-Encyclopedias](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias) | Public encyclopedia placeholder (no commits as of the 2026-11-10 inventory) |


## Ontology toolchain foundation

The canonical `Master_Ontology_Human_and_Intelligence.md` remains the source-of-truth ontology text; its eight foundation schemes and typed relations are unchanged. The implementation branch adds a separate open toolchain layer for versioned ontology artifacts, SKOS alignment, PROV-O provenance, SHACL reports, reasoning certificates, bitemporal records, schema evolution and closed-world write admission.

- [Open ontology toolchain architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/blob/implementation/repository-foundation-2026-11-12/ONTOLOGY_TOOLCHAIN_ARCHITECTURE.md)
- [Portable ontology contract schemas](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/tree/implementation/repository-foundation-2026-11-12/schemas/ontology)
- [RDF/Turtle examples: SKOS + PROV-O and SHACL report](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/tree/implementation/repository-foundation-2026-11-12/examples/ontology)
- [Validation and CI evidence](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/blob/implementation/repository-foundation-2026-11-12/ONTOLOGY_TOOLCHAIN_VALIDATION.md)

This public branch contains only portable schemas, synthetic fixtures, example ontology evidence and open toolchain documentation. It contains no C2O-private ontology, policy, named-graph grant, authority token, signing key or operational record.
