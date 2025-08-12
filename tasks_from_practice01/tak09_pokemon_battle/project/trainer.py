from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for poke in self.pokemons:
            if poke.name == pokemon_name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        output = [f"Pokemon Trainer {self.name}",
                  f"Pokemon count {len(self.pokemons)}"]
        for pokemon in self.pokemons:
            output.append(f"- {pokemon.pokemon_details()}")

        return "\n".join(output)








