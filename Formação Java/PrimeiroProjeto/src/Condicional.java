public class Condicional {

    public static void main(String[] args) {
        int anoDeLancamento = 1995;
        boolean incluidoNoPlano = false;
        double notaDoFilme = 8.1;
        String tipoDoPlano = "plus";

        if (anoDeLancamento >= 2025){
            System.out.println(("Lançamentos que os clientes gostam"));
        } else {
            System.out.println("Os clientes não gostam de filmes antigos");
        }

        if (tipoDoPlano.equals("plus") && incluidoNoPlano == true){
            System.out.println(("Tipo de plano Plus"));
        } else {
            System.out.println("Não e o plano Plus");
        }
    }
}
