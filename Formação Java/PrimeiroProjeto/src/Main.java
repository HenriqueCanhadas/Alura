//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("Esse é o Screen Match");
        System.out.println("Filme: Pele");

        int anoDeLancamento = 1995;
        System.out.println("Ano de Laçamento: " +anoDeLancamento);

        boolean incluidoNoPlano = false;
        System.out.println("Incluido no Plano: " +incluidoNoPlano);

        double notaDoFilme = 8.1;

        //Media para Calcular
        double media = (9.8 +6.3+ 8.0)/3;
        System.out.println(media);

        String sinopse;
        sinopse = "Filme do grande rei Pele";
        System.out.println(sinopse);

        sinopse =
                """
                Filme do grande rei Pele
                VAmboraaaaa
                """+anoDeLancamento;
        System.out.println(sinopse);

        int classificacao;
        classificacao = (int) (media / 2);
        System.out.println(classificacao);

    }
}