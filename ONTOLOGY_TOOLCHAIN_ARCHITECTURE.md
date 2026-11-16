# Ontology Toolchain Architecture — UNIVERSALIS

**Owner:** The UNIVERSALIS Ontology repository  
**Boundary:** Public, open, inspectable, independently operable  
**Status:** Contract foundation and toolchain mapping; specialized engines remain candidates pending verification  
**Canonical ontology:** `Master_Ontology_Human_and_Intelligence.md` (eight foundation schemes: H-K, H-C, H-S, H-P, I-K, I-C, I-S, I-P). This toolchain does not replace or rewrite it.

## 1. Architectural position

The ontology is a versioned, machine-checkable artifact. Validation, reasoning, alignment, change planning and writes are separate operations, each with provenance and explicit results. An ontology node is not automatically a fact about an actor. A mapping candidate is not an accepted equivalence. Confidence is not truth. A successful reasoner call is not proof that its input, engine or deployment is sound.

Preserve the canonical master ontology's type discipline:
- A concept belongs to a concept scheme; it is not automatically assigned to an individual human or intelligence system.
- H-K/H-C/H-S/H-P and I-K/I-C/I-S/I-P remain distinct schemes. Knowledge, capabilities, skills and powers have typed relations, not automatic one-to-one or subclass equivalence.
- Power/capacity and legitimate authority remain distinct. Access to an ontology tool does not authorize a write or a schema change.
- Missing edges mean unrecorded, not impossible.
- Actor assignments require version, context, task, inputs, tools, access, resources, evaluator, date, evidence, uncertainty, limitations and outcome.

## 2. Open tool inventory

### Ontology engine and reasoning
- **open-ontologies (fabio-rovai):** Rust MCP/CLI candidate with RDF/Oxigraph, SPARQL, OWL reasoning, SHACL, ontology lifecycle, alignment, change planning and Lean-checkable derivation certificates. Its README describes optional Cargo features and states that published default binaries omit eight feature-gated tools. Tool count and capability availability must be pinned to the exact release/build.
- **Ontosphere:** browser RDF/OWL editor, Konclude/WASM reasoning, MCP interface and PROV-O edit provenance; verify current repository identity, source, 43-tool count and release status.
- **graph-mcp-driver:** Neo4j + Jena Fuseki SPARQL/OWL/SHACL overlay; verify the supported UAF profile, reasoning regime and operational security.

### Agent-writable and compiled ontology
- **MNEME / FlowX.AI Ontology Layer:** staged agent writes with provenance/confidence, conflict screening, quarantine, reinforcement/human promotion and one-way read-only institutional source-of-truth import.
- **Ontology-to-Tools Compilation / The World Avatar:** compile domain ontology constraints into agent-callable tool interfaces so semantic constraints participate in generation and writes, rather than relying only on post-hoc checks.
- **Entigram:** closed-world schema/action admission, deterministic conflict ledger and approved semantic alignments; verify canonical source and actual ledger format.

### Schema governance and business knowledge
- **OpenBKN:** ontology-driven business knowledge network, private deployment, identity/access, action policy and traceability; treat the described deployment pattern as candidate until tested.
- **Semantica:** OWL/SHACL/SKOS graph/context/provenance reasoning candidate.
- **ontobricks:** Databricks Unity Catalog to knowledge graph with OWL/SWRL/SHACL and MCP.
- **cassis-cli:** CLI ontology check/test and offline source-schema snapshots.
- **Quipu:** Rust/SQLite bitemporal governed graph candidate; pending-state write gate, named-graph trust/authority composition, signed verdicts and as-of query pattern. Independently verify crate/release/tool manifest: public crate documentation currently describes an immutable bitemporal EAVT fact log backed by SQLite, but source-supplied MCP tool counts are not accepted without pinning.

### Open standards and vocabularies
- RDF 1.1 / RDF serialization; OWL 2 DL semantics; SHACL validation reports; PROV-O provenance; SKOS concept schemes and mapping properties. W3C standard terms are identifiers and contracts, not claims that every tool fully implements every profile.

All product claims, tool counts, advertised MCP surfaces, reasoner completeness, Lean certificates, supported serialization, licence and security statements remain release-specific candidates until independently verified.

## 3. Portable shared contracts

The shared v1 schema family defines:
1. Ontology artifact identity, version, serialization, logic profile and digest.
2. Cross-ontology alignment mappings using SKOS mapping properties, with evidence, confidence, provenance and review status.
3. PROV-O-aligned provenance event records.
4. SHACL validation report metadata and result entries.
5. Reasoning certificate metadata with a declared asserted-graph digest, assumptions, checker, trusted-computing-base profile and restricted claim scope.
6. Bitemporal facts with valid time, transaction time, named graph, trust label and close-don't-overwrite behavior.
7. As-of query records identifying both valid-time and transaction-time cutoffs.
8. CrosswalkResolutionReceipt with event CID, grounding confidence and resolution decision.
9. Agent write provenance/confidence and staging/quarantine/promotion state.
10. Named-graph authority profiles with non-widening composition.
11. Conflict records.
12. Schema-evolution proposals with blast radius, SHACL, reasoning, rollback and admission evidence.
13. Ontology-to-tool compilation contracts.
14. Closed-world action-admission receipts.

Only versioned schemas, approved ontology artifacts, selected mapping triples, digests and sanitized evidence cross an ecosystem boundary. No C2O-private ontology, named-graph grant, private policy, signing key, authority token, identity mapping or operational trace is part of this public repository.

## 4. Normative semantic distinctions

### Alignment
Use SKOS mapping properties precisely: `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`. Only `skos:exactMatch` is transitive in the SKOS mapping model; do not infer transitivity for the other mappings. Label/embedding similarity and structural graph analysis propose candidates, not semantic truth. Acceptance requires evidence and review policy.

### SHACL
The portable report uses SHACL Validation Report concepts: `sh:conforms` and individual results with `sh:focusNode`, `sh:resultSeverity` and `sh:sourceConstraintComponent`; `sh:resultPath`, `sh:resultMessage`, `sh:sourceShape` and value are optional as permitted by SHACL. In this v1 profile, conforms=true requires no results; conforms=false requires at least one. SHACL 1.2 is recorded as a draft profile separately from the stable SHACL 1.0 target.

### Reasoning certificates
A Lean checker may independently check a derivation certificate relative to the asserted graph, premises and declared assumptions. It does not automatically prove that the Rust engine supplied the same graph/steps it actually reasoned over, that the source graph is true, or that the complete reasoner is sound. The trusted-computing-base profile is mandatory metadata; no fixture or producer-signed claim is called verified.

### Bitemporal and graph authority
Valid time records when a fact applies in the modeled world; transaction time records when the store knew/recorded it. Close prior intervals and append revisions; do not overwrite. Named graphs carry trust/authority metadata. Composition must not widen capability or trust scope.

### Agent write-back
Institutional source-of-truth imports are read-only to agents. Agent writes begin staged or quarantined, carry provenance/confidence and conflict-screen results, and enter canonical retrieval only after recorded human review or reinforcement evidence. Do not invent the three conflict categories before the source defines them.

### Closed-world admission and compilation
Ontology-to-tools compilation binds generated interfaces to ontology and shape digests. Unknown entities, attributes and relationships are rejected, quarantined or sent for review according to declared policy. Allow is impossible while any unknown item remains unresolved. Every admitted write has a pre-write action-admission receipt.

### Evolution
Stable concept IDs are preserved. Add narrower concepts; deprecate with explicit replacement/provenance; never silently mutate meaning. Before a proposal is applied, require a version bump, blast-radius evidence, SHACL report, reasoning certificate, rollback plan, action-admission receipt and reviewers according to the declared risk policy.

## 5. Current implementation limits

The companion JSON Schema contracts, synthetic fixtures and semantic validator provide a basic portable record model. They do not deploy an RDF triple store, OWL reasoner, SHACL engine, Lean proof checker, ontology alignment service, bitemporal database, MCP registry, ontology-to-tools compiler, conflict-resolution service or schema deployment pipeline. No external candidate is marked installed or integrated.

## 6. Current source references

- Open Ontologies source and release/build caveats: https://github.com/fabio-rovai/open-ontologies
- Open Ontologies Lean certificate trusted-computing-base statement: https://github.com/fabio-rovai/open-ontologies/blob/main/docs/trusted-computing-base.md
- PROV-O W3C Recommendation: https://www.w3.org/TR/prov-o/
- OWL 2 Direct Semantics W3C Recommendation: https://www.w3.org/TR/owl2-direct-semantics/
- SKOS W3C Recommendation and mapping-property semantics: https://www.w3.org/TR/skos-reference/
- SHACL Validation Report vocabulary: https://www.w3.org/TR/shacl/
- SHACL 1.2 Core current Working Draft: https://www.w3.org/TR/shacl12-core/
- Ontology-to-Tools Compilation research: https://arxiv.org/abs/2602.03439
- MNEME / FlowX.AI source description: https://www.flowx.ai/research/mneme
- Quipu crate documentation: https://docs.rs/quipu-ai/latest/quipu/

## 7. Unresolved verification queue

Canonical source identity, release and licence must be confirmed for Ontosphere, graph-mcp-driver, Entigram, OpenBKN, Semantica, ontobricks and cassis-cli. For Quipu, verify source/release and whether advertised MCP tool counts apply to the exact build. For open-ontologies, independently assess the reasoner's supported description logic, proof checker and Rust-to-certificate trusted boundary, default/feature-gated tool availability, rollback semantics and adversarial fixtures. No source-reported tool count or performance claim is promoted to verified status by this architecture document.
