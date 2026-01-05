import asyncio

# Corrotinas
async def introducao(nome):
    print(f"{nome} começou na Empresa..."   )
    await asyncio.sleep(5) # Simulando E/S
    print(f"{nome} manda saudações")

# Corrotinas
async def main ():
    await introducao("Pessoa 1") # Atuação Síncrona
    await asyncio.gather(
        introducao("Pessoa 2"),
        introducao("Pessoa 3"), # Atuação Assincrona
)

asyncio.run(main())
