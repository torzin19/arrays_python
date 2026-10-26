# Lista de itens do cardápio
cardapio = ['pastel', 'pizza', 'coxinha']

print("Cardápio inicial:", cardapio)

# Adiciona "lasanha" no COMEÇO da lista (índice 0)
cardapio.insert(0, "lasanha")
print("Após insert no começo:", cardapio)

# Adiciona "empada" no FINAL da lista
cardapio.append("empada")
print("Após append no final:", cardapio)

# Remove "lasanha" do cardápio pelo nome
cardapio.remove("lasanha")
print("Após remove da lasanha:", cardapio)

# Remove o ÚLTIMO item da lista ("empada") usando pop()
item_removido = cardapio.pop()
print(f"Item removido com pop(): {item_removido}")
print("Cardápio após o pop():", cardapio)

# Solicita a escolha do usuário
pedido = input("O que você quer comer hoje? ")

# Verifica se o pedido NÃO está no cardápio
if pedido not in cardapio:
    print(f"{pedido} não está no cardápio, que tal você pedir {cardapio}")
else:
    print(f"Saindo um pedido de {pedido}!")
