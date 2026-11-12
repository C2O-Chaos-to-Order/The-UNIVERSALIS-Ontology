#!/usr/bin/env python3
"""Validate portable ontology toolchain contracts and critical semantic invariants."""
from __future__ import annotations
import copy,json,sys
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator
from rdflib import Graph
ROOT=Path(__file__).resolve().parents[2]
SCHEMA=json.loads((ROOT/"schemas/ontology/ontology-toolchain-contracts.v1.schema.json").read_text())
FIX=json.loads((ROOT/"examples/ontology/ontology-toolchain-contracts.v1.json").read_text())
KEYS={
 "ontology_artifact":"ontologyArtifact","alignment_mapping":"alignmentMapping","prov_event":"provEvent",
 "shacl_report":"shaclValidationReport","reasoning_certificate":"reasoningCertificate",
 "bitemporal_fact":"bitemporalFact","as_of_query":"asOfQuery",
 "crosswalk_resolution_receipt":"crosswalkResolutionReceipt","agent_ontology_write":"agentOntologyWrite",
 "named_graph_authority_profile":"namedGraphAuthorityProfile","conflict_record":"conflictRecord",
 "ontology_change_proposal":"ontologyChangeProposal","compiled_tool_contract":"compiledToolContract",
 "action_admission_receipt":"actionAdmissionReceipt"}
def validate(key,obj):
 schema={"$schema":SCHEMA["$schema"],"$ref":"#/$defs/"+KEYS[key],"$defs":SCHEMA["$defs"]}
 Draft202012Validator.check_schema(schema); Draft202012Validator(schema).validate(obj)
 if key=="reasoning_certificate" and obj.get("fixture_only") and obj.get("checker_status")=="accepted":
  raise ValueError("synthetic proof fixture cannot claim checker acceptance")
 if key=="shacl_report":
  if obj.get("conforms") != (len(obj.get("results",[])) == 0):
   raise ValueError("SHACL conforms must be true exactly when the validation report has no results")
 if key=="bitemporal_fact":
  if obj.get("valid_to") is not None and parse_time(obj["valid_to"]) <= parse_time(obj["valid_from"]):
   raise ValueError("valid-time interval end must be after its start")
  if obj.get("transaction_to") is not None and parse_time(obj["transaction_to"]) <= parse_time(obj["transaction_from"]):
   raise ValueError("transaction-time interval end must be after its start")
 if key=="named_graph_authority_profile":
  composed=set(obj.get("composed_capabilities",[]))
  if not composed <= set(obj.get("own_capabilities",[])):
   raise ValueError("composed graph authority exceeds the graph's own capabilities")
  for parent in obj.get("parent_capability_sets",[]):
   if not composed <= set(parent):
    raise ValueError("named-graph composition widens a parent capability set")
 if key=="agent_ontology_write":
  origin=obj.get("origin"); state=obj.get("staging_state")
  if origin=="pdm_import" and (obj.get("source_of_truth_mode")!="read-only" or state!="canonical-import"):
   raise ValueError("institutional source-of-truth imports must remain read-only")
  if origin=="agent_write" and state not in {"staged","quarantined","promoted","rejected"}:
   raise ValueError("agent writes cannot bypass staging and review")
  if state=="promoted" and (not obj.get("promotion_basis") or not obj.get("promotion_evidence_refs")):
   raise ValueError("promotion requires human-review or reinforcement evidence")
 if key=="action_admission_receipt" and obj.get("decision")=="allow":
  if obj.get("unknown_entity_refs") or obj.get("unknown_attribute_refs") or obj.get("unknown_relationship_refs"):
   raise ValueError("closed-world admission cannot allow unresolved unknowns")
 if key=="ontology_change_proposal" and obj.get("status")=="applied":
  for field in ("blast_radius_report_ref","shacl_report_ref","reasoning_certificate_ref","action_admission_receipt_ref"):
   if not obj.get(field): raise ValueError("applied ontology changes require "+field)
def parse_time(v):
 return datetime.fromisoformat(v.replace("Z","+00:00"))
def expr_ok(expr,active):
 if expr["kind"]=="grant-ref": return expr["grant_ref"] in active
 vals=[expr_ok(x,active) for x in expr["children"]]
 return all(vals) if expr["kind"]=="all-of" else any(vals)
def main():
 for key,obj in FIX.items(): validate(key,obj)
 # Parse standards-based RDF fixtures. This checks Turtle syntax only, not OWL entailment or SHACL execution.
 alignment_graph=Graph().parse(ROOT/"examples/ontology/alignment-provenance-example.ttl",format="turtle")
 shacl_graph=Graph().parse(ROOT/"examples/ontology/shacl-validation-report-example.ttl",format="turtle")
 assert len(alignment_graph)>0 and len(shacl_graph)>0
 report=FIX["shacl_report"]
 assert report["conforms"] is False and len(report["results"])>0
 # SHACL report invariants: conformance is true iff there are no results.
 bad=copy.deepcopy(report); bad["conforms"]=True
 try: validate("shacl_report",bad)
 except Exception: pass
 else: raise AssertionError("SHACL report with results cannot conform")
 fact=FIX["bitemporal_fact"]
 if fact["valid_to"] is not None: assert parse_time(fact["valid_to"])>parse_time(fact["valid_from"])
 if fact["transaction_to"] is not None: assert parse_time(fact["transaction_to"])>parse_time(fact["transaction_from"])
 assert fact["close_dont_overwrite"] is True
 # Quipu-style authority composition must not widen any contributing graph.
 profile=FIX["named_graph_authority_profile"]
 composed=set(profile["composed_capabilities"])
 assert composed<=set(profile["own_capabilities"])
 for parent in profile["parent_capability_sets"]: assert composed<=set(parent)
 # Imported institutional source stays read-only; agent writes cannot directly enter canonical state.
 write=FIX["agent_ontology_write"]
 if write["origin"]=="pdm_import": assert write["source_of_truth_mode"]=="read-only" and write["staging_state"]=="canonical-import"
 if write["origin"]=="agent_write": assert write["staging_state"] in {"staged","quarantined","promoted","rejected"}
 if write["staging_state"]=="promoted": assert write.get("promotion_basis") and write.get("promotion_evidence_refs")
 # Accepted mappings require review; confidence is not a truth score.
 mapping=FIX["alignment_mapping"]
 assert 0<=mapping["grounding_confidence"]<=1 and mapping["decision_status"]!="accepted"
 # Closed-world allow cannot carry unknown entities/attributes/relationships.
 admission=FIX["action_admission_receipt"]
 if admission["decision"]=="allow":
  assert not (admission["unknown_entity_refs"] or admission["unknown_attribute_refs"] or admission["unknown_relationship_refs"])
 # Versioned evolution: applied changes need full validation, reasoning, blast-radius and admission evidence.
 proposal=FIX["ontology_change_proposal"]
 if proposal["status"]=="applied":
  for k in ("blast_radius_report_ref","shacl_report_ref","reasoning_certificate_ref","action_admission_receipt_ref"):
   assert proposal.get(k)
 # Parent/child graph capabilities use subset composition (intersection or stricter), never union.
 negative=[]
 x=copy.deepcopy(FIX); x["shacl_report"]["conforms"]=True; negative.append(("SHACL conforms with results","shacl_report",x))
 x=copy.deepcopy(FIX); x["ontology_change_proposal"]["status"]="applied"; negative.append(("applied change lacks evidence","ontology_change_proposal",x))
 x=copy.deepcopy(FIX); x["alignment_mapping"]["decision_status"]="accepted"; negative.append(("accepted mapping lacks reviewer","alignment_mapping",x))
 x=copy.deepcopy(FIX); x["agent_ontology_write"]["origin"]="pdm_import"; x["agent_ontology_write"]["source_of_truth_mode"]="writable"; negative.append(("institutional import cannot be writable","agent_ontology_write",x))
 x=copy.deepcopy(FIX); x["action_admission_receipt"]["decision"]="allow"; negative.append(("closed-world admission with unknown attribute","action_admission_receipt",x))
 x=copy.deepcopy(FIX); x["named_graph_authority_profile"]["composed_capabilities"]=["read","write","admin"]; negative.append(("graph composition cannot widen","named_graph_authority_profile",x))
 x=copy.deepcopy(FIX); x["bitemporal_fact"]["valid_to"]="2020-01-01T00:00:00Z"; negative.append(("bitemporal interval end before start","bitemporal_fact",x))
 x=copy.deepcopy(FIX); x["reasoning_certificate"]["checker_status"]="accepted"; negative.append(("fixture proof cannot claim accepted","reasoning_certificate",x))
 x=copy.deepcopy(FIX); x["crosswalk_resolution_receipt"]["grounding_confidence"]=2; negative.append(("crosswalk confidence range","crosswalk_resolution_receipt",x))
 for label,key,obj in negative:
  try:
   for k,v in obj.items(): validate(k,v)
  except Exception: continue
  raise AssertionError("negative test unexpectedly passed: "+label)
 print(f"PASS: {len(KEYS)} positive ontology contract fixtures and {len(negative)} negative cases")
 print("LIMIT: no live RDF/OWL reasoner, SHACL engine, Lean checker, graph store, bitemporal query engine, signer, or schema deployment")
if __name__=="__main__":
 try: main()
 except Exception as exc: print("FAIL:",exc,file=sys.stderr); raise SystemExit(1)
