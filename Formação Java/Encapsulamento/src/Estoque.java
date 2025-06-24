public class Estoque {
    private String nome;
    private double preco;

    public Estoque(double preco, String nome) {
        this.preco = preco;
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public void validar(){
        if(preco<=0){
            System.out.println("Preço inválido.");
            System.out.println("Produto: "+ nome);
            System.out.println(("Preço: 0,00"));
        }else {
            System.out.println("Preço Válido.");
            System.out.println("Produto: "+ nome);
            System.out.println(("Preço: "+ preco));
        }
    }

}
