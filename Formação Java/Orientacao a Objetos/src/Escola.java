public class Escola {
    String aluno;
    double nota1;
    double nota2;
    double media;

    public void calcularMedia() {
        System.out.println("Aluno: "+ aluno);
        System.out.println("Nota 1: "+ nota1);
        System.out.println("Nota 2: "+ nota2);

        media = (nota1 + nota2) / 2;

        System.out.println("Média: "+ media);

        if (media>= 7.0){
            System.out.println("Situação: Aprovado");
        }else {
            System.out.println("Situação: Reprovado");
        }
    }
}
