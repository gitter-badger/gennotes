# GenNotes

**GenNotes** and **Genevieve** are a pair of projects designed to empower individuals to understand putative diseases or traits reported for variants in a personal genome.

## Motivation

We’d like to empower understanding about claims of diseases or traits caused by variants in a personal genome, and comment upon these claims.

ClinVar a public domain resource that aggregates and reports assertions of clinical impact of genetic variants. While invaluable, these assertions can be flawed – this is especially apparent when evaluating assertions made for a personal genome. Coupling genome reports with consensus, structured note-taking helps re-evaluate assertions efficiently, and improves the quality of reports generated for future genomes.

To this end, we’d like to develop a series of related open source tools:
- **GenNotes** A server storing publicly shared and flexibly structured tags associated with genetic variants. These tags are structured as key/value tags, in the manner of Open Street Map. These can be arbitrary keys, but initially we'd like to focus on ClinVar and Genevieve tags.
- **Genevieve** A client web app that can process individual genomes to find variants matching ClinVar positions. Using GenNotes, the client retrieves and reports the latest ClinVar and Genevieve tags for this variant list.

## Pre-sprint goals

We'd like to have the following in place to support the sprint.
- GenNotes server (web app)
-- User accounts
-- Variant model, pre-populated with variants found in ClinVar
-- Key/value tag model
- Genevieve client (web app)
-- User accounts
-- VCF file upload
-- process VCF to store in db list of variants matching ClinVar records ("variant report")

## Sprint goals
- on GenNotes server, import ClinVar key/value tags for variant positions
- Specify the method (widget/API) for client apps to update or submit new tags.
- display Genevieve client variant report w/AJAX GenNotes query & display ClinVar/Genevieve tag data

## Stretch goals
- Implement the API/widget on Genevieve client
- Import ExAC key/value tags for variant positions