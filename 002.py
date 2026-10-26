# Lista de itens do cardápio
cardapio = ['pastel', 'pizza', 'coxinha']

print("Cardápio inicial:", cardapio)

# Adiciona a lasanha ao cardápio
cardapio.append("lasanha")
print("Cardápio após adicionar lasanha:", cardapio)

# Remove a lasanha do cardápio
cardapio.remove("lasanha")
print("Cardápio após remover lasanha:", cardapio)

# Solicita a escolha do usuário
pedido = input("O que você quer comer hoje? ")

# Verifica se o pedido NÃO está no cardápio
if pedido not in cardapio:
    print(f"{pedido} não está no cardápio, que tal você pedir {cardapio}")
else:
    print(f"Saindo um pedido de {pedido}!")
