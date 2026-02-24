# 304Assignment04

# PokeAPI Data Pull → Raw JSON → DataFrame → CSV

## Documentation Review
- Base URL: https://pokeapi.co/api/v2/
- List endpoint: GET /pokemon (returns paginated results)
- Detail endpoint: GET /pokemon/{id or name}/
- Query parameters (list endpoint): 
  - limit: number of records returned
  - offset: starting index into the full list
- Pagination:
  - The list response includes `count`, `next`, `previous`, and `results`.
  - `results` is an array of objects containing `{ name, url }`.
- Authentication:
  - No authentication required (public API).
- Rate limits:
  - Docs state rate limiting was removed after moving to static hosting (Nov 2018).
  - Fair-use policy still applies; excessive requests can lead to IP bans.

## What this project does
1. Requests the list of Pokémon from the PokeAPI.
2. Saves the exact raw JSON response body to `pokemon_list_raw.json`.
3. Requests Pokémon detail records from the URLs in the list response.
4. Normalizes selected fields into a pandas DataFrame.
5. Exports the DataFrame to `pokemon.csv`.

## How to run
Requirements:
- Python
- requests
- pandas

Run:
```bash
python your_script_name.py
