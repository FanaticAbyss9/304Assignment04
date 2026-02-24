import requests
import pandas as pd

class PokeAPI:
    base_url = "https://pokeapi.co/api/v2"

    def get_pokemon_list_page(self, limit=20, offset=0):
        """
        GET /pokemon?limit=...&offset=...
        Returns the raw requests.Response and parsed JSON dict.
        """
        url = f"{self.base_url}/pokemon"
        params = {"limit": limit, "offset": offset}
        r = requests.get(url, params=params)
        r.raise_for_status()
        return r, r.json()

    def get_pokemon_detail(self, pokemon_url):
        """
        GET a pokemon detail URL from results[i]['url'].
        Returns parsed JSON dict.
        """
        r = requests.get(pokemon_url)
        r.raise_for_status()
        return r.json()

    def get_all_pokemon_refs(self):
        """Return list of all pokemon name/url pairs"""
        url = f"{self.base_url}/pokemon?limit=100000"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()["results"]

    def get_pokemon_stats(self, pokemon_url):
        """Fetch stats for a single pokemon"""
        r = requests.get(pokemon_url)
        r.raise_for_status()
        data = r.json()

        return {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_experience": data["base_experience"],
            "types": data["types"],
            "stats": data["stats"],
            "forms": data["forms"],
            "species": data["species"],
            "is_default": data["is_default"]
        }

    def get_all_pokemon(self, limit=None):
        """Return DataFrame of pokemon stats"""
        refs = self.get_all_pokemon_refs()

        if limit is not None:
            refs = refs[:limit]

        rows = []
        for ref in refs:
            rows.append(self.get_pokemon_stats(ref["url"]))

        return pd.DataFrame(rows)
