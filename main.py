import streamlit as st

# Título da página
st.title("Cadastro de Produtos")

# Barra lateral para seleção de ações
opcao = st.sidebar.selectbox("Selecione uma opção", ("Adicionar Produto", "Listar Produtos"))

# Dicionário simulado de uma base de dados de produtos
produtos = [

  {"ID": 1, "Nome": "Abacaxi", "Preço": 5.99},
  {"ID": 2, "Nome": "Abacate", "Preço": 4.99},
  {"ID": 3, "Nome": "Banana", "Preço": 1.99}
  
]

# Função para listar produtos
def listar_produtos():
  st.subheader("Lista de Produtos")
  for produto in produtos:
    st.write(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Preço: {produto['Preço']}")

# Função para adicionar produto
def adicionar_produto():
  st.subheader("Adicionar Produto")
  nome = st.text_input("Nome do Produto")
  preco = st.number_input("Preço do Produto")
  if st.button("Adicionar"):
    novo_produto = {"ID": len(produtos) + 1, "Nome": nome, "Preço": preco}
    produtos.append(novo_produto)
    st.sucess("Produto adicionado com sucesso!")

# Lógica para as opções selecionadas na barra lateral
if opcao == "Adicionar Produto":
  adicionar_produto()

elif opcao == "Listar Produtos":
  listar_produtos()