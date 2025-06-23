public class Produto {
    String nome;
    double preco;
    int quantidade;

    public void exibirInformacoes(){
        System.out.println("Produto: "+nome+" - Preço: R$ "+preco+" - Quantidade em estoque: "+quantidade);
    }

}
