import java.util.Scanner;

public class Leitura {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);

        System.out.println("Digite seu Filme Favorito");
        String filme = leitura.nextLine();
        System.out.println(filme);
        System.out.println("Qual ano de lançamento?");
        int anoDeLacamento = leitura.nextInt();
        System.out.println(anoDeLacamento);
        System.out.println("Qual a avaliação?");
        double avaliacao = leitura.nextDouble();
        System.out.println(avaliacao);
        
    }
}
