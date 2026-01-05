import asyncio
import httpx

# Receber as Informações dos Pokémons
# Consumo de API externa simples

async def fetch_get(cliente: any, nome_pokemon: str):
    """Função fetch_get = baixar Informações da API"""
    link = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    response = await cliente.get(link) # E/S
    dados = response.json()

    nome = dados["name"]
    habilidade = dados["moves"][0]["move"]

    print(f"nome: {nome} / movimento: {habilidade}")
    print()
    print()

async def main():
    """Função main para colocar nossos pokémons"""
    async with httpx.AsyncClient() as cliente:
        #await fetch_get(cliente, "squirtle") # Atuação Síncrona
        await asyncio.gather(
            fetch_get(cliente, "squirtle"),
            fetch_get(cliente, "charmander" ),
            fetch_get(cliente, "bulbasaur")
        )
        print("Coleta de dados finalizada.")
asyncio.run(main())
