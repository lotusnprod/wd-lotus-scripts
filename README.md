# SPARQL Query Runner for Qlever Endpoint

This Python script allows you to execute SPARQL queries stored in `.rq` files on the Qlever endpoint for Wikidata or any other SPARQL endpoint. The results are saved as JSON files.

## Requirements

Ensure you have Python 3 installed and install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Usage

### Clone this repository

```bash
git clone https://github.com/lotusnprod/wd-lotus-scripts.git
cd wd-lotus-scripts
```

### Running the Script

To run the script, use the following command:

```bash
python src/query_maker.py
```
By default this will retrieve the highest peaks in the world and their associated country from Wikidata and save the results as a JSON file (`sparql_results.json`).

You can specify the query file, endpoint, and output file using the following arguments:

- `--query`: (optional) The path to the .rq file containing the SPARQL query.
- `--endpoint`: (optional) The URL of the SPARQL endpoint. If not provided, the script defaults to the Qlever Wikidata endpoint (https://qlever.cs.uni-freiburg.de/api/wikidata).
- `--output`: (optional) The file path where the JSON results will be saved. If not specified, it defaults to sparql_results.json.

### Example 

For example, to retrieve the full LOTUS dataset from the Qlever endpoint and save the results as `lotus_results.json`, you can run:

```bash
python src/query_maker.py --query data/queries/compound_taxon_ref_full.rq --output data/results/full_lotus_results.json
```

### Query Files description

- **compound_taxon_ref_full.rq** : This query retrieves the Wikidata QID of the chemical compounds, their canonical SMILES, the Wikidata QID of the taxon they are associated with, the taxon name, the Wikidata QID of the reference, and the DOI for the reference.

- **compound_taxon_ref.rq** : This query retrieves the Wikidata QID of the chemical compounds, the Wikidata QID of the taxon they are associated with and the Wikidata QID of the reference. No additional information.

- **compound_canonical_smiles.rq** : This query retrieves the Wikidata QID of the chemical compounds and their canonical SMILES.

- **compound_isomeric_smiles.rq** : This query retrieves the Wikidata QID of the chemical compounds and their isomeric SMILES.

- **ref_doi.rq** : This query retrieves the Wikidata QID of the reference and the DOI.

- **taxo_taxo_name.rq** : This query retrieves the Wikidata QID of the taxon and the taxon name.
