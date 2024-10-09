import requests
import json
import argparse

# Define the default Qlever endpoint
DEFAULT_ENDPOINT_URL = "https://qlever.cs.uni-freiburg.de/api/wikidata"
DEFAULT_QUERY_FILE = "data/queries/highest_peak_per_contry.rq"

# Function to read the SPARQL query from a file
def read_sparql_query(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to execute the SPARQL query
def execute_sparql_query(endpoint_url, query):
    # Define the query parameters
    params = {
        'query': query
    }
    
    # Send the request to the endpoint
    response = requests.get(endpoint_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Assuming the endpoint returns a JSON response
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Function to save results as a JSON file
def save_results_as_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Results saved to {file_path}")

# Main execution
def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description="Run SPARQL queries on the Qlever endpoint")
    
    parser.add_argument(
        '--endpoint',
        type=str,
        default=DEFAULT_ENDPOINT_URL,
        help="SPARQL endpoint URL (default: Qlever Wikidata endpoint)"
    )
    
    parser.add_argument(
        '--query',
        type=str,
        default=DEFAULT_QUERY_FILE,
        help="Path to the SPARQL query file"
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='sparql_results.json',
        help="Output file path to save the JSON results (default: sparql_results.json)"
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Read the SPARQL query from the file
    sparql_query = read_sparql_query(args.query)
    
    # Execute the SPARQL query and get the results
    results = execute_sparql_query(args.endpoint, sparql_query)
    
    # If results are obtained, save them as JSON
    if results:
        save_results_as_json(results, args.output)

# Entry point of the script
if __name__ == "__main__":
    main()
