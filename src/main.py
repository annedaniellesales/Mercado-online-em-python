from Cliente import Cliente
from Funcionario import Funcionario
from Pedido import Pedido
from Produto import Produto
from Estoque import Estoque

def main ():
   while(True):
        escolha = int(input("BEM VINDO AO CAIXA DE AUTOATENDIMENTO\n1 - Acessar aba de cliente\n2- Acessar aba de Funcionário\n"))

        if escolha == 1:
            Cliente.ValidarCliente()
            while escolha != 4:
                escolha = int(input("O que deseja fazer?\n1-Adicionar um item ao carrinho de compras\n2-Exibir Carrinho\n3-Editar Carrinho de compras\n4-Finalizar compra\n"))
                if escolha == 1:
                    Pedido.FazerPedido()
                if escolha == 2:
                    Pedido.ExibirCarrinho()
                if escolha == 3:
                    Pedido.EditarCarrinho()
                if escolha == 4:
                    Pedido.FinalizarCompra()
            
        elif escolha == 2:
            Funcionario.ValidarFuncionario()
            while escolha != 5:
                escolha = int(input("O que deseja fazer?\n1-Adicionar produto ao estoque\n2-Excluir Produto do Estoque\n3-Listar Produtos do Estoque\n4-Valor total em estoque\n5-Filtrar por tipo de produto"))
                print("\n")
                if escolha == 1:
                    Funcionario.AdicionarProduto()
                if escolha == 2:
                    Funcionario.ExcluirProduto()
                if escolha == 3:
                    Funcionario.ListarEstoque()
                if escolha == 4:
                    Funcionario.ValorEstoque()   
                if escolha == 5:
                    Funcionario.FiltroTipoProduto()     



    
main()