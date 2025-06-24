public class Filme {
    private String nome;
    private double total = 0;
    private double media = 0;

    public Filme(String nome) {
        this.nome = nome;
    }

    public void adicionarAvaliacao(int avaliacao){
        total += avaliacao;
        media++;
    }

    public void verMedia(){
        media = total / media;
        System.out.println("Média de avaliações para Matrix: " + media);
    }

}
