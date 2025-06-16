import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Scanner scanner = new Scanner(System.in);
        //int numero = scanner.nextInt();
        //scanner.close();

        int numero = 7;

        if (numero % 2 == 0) {
            System.out.println("o numero " + numero + " é par");
        } else {
            System.out.println("o numero " + numero + " é impar");
        }

        System.out.println("-".repeat(50));

        double nota1 = 5.0;
        double nota2 = 9.0;
        double nota3 = 9.0;
        //double media = (nota1 + nota2 + nota3) / 3;
        double media = 4.3;
        System.out.println(media);

        if (media >= 7) {
            System.out.println("O estudante teve média " + media + " e foi aprovado.");
        } else if (media >= 5 || media <= 6.9) {
            System.out.println("O estudante teve média " + media + " e está de recuperação.");
        } else if (media > 5) {
            System.out.println("O estudante teve média " + media + " e foi reprovado. ");
        }

        System.out.println("-".repeat(50));

        int senha = 1236;
        int senhaCorreta = 123456;

        if (senhaCorreta == senha) {
            System.out.println("Acesso permitido! ");
        } else {
            System.out.println("Acesso negado! ");
        }

        System.out.println("-".repeat(50));

        int primeiroNumero = 40;
        int segundoNumero = 25;

        if (primeiroNumero > segundoNumero) {
            System.out.println("O maior número é " + primeiroNumero);
        } else if (segundoNumero > primeiroNumero) {
            System.out.println("O maior número é " + segundoNumero);
        }

        System.out.println("-".repeat(50));

        double compra = 90.0;

        if (compra > 100.0) {
            System.out.println("Desconto de 10% aplicado. ");
            System.out.println("Novo valor: R$" + (compra - (compra * 0.10)));
        } else {
            System.out.println("Nenhum desconto aplicado. ");
            System.out.println("Valor total: R$" + compra);
        }

        System.out.println("-".repeat(50));

        String diaDaSemana = "quarta";

        if (diaDaSemana.equals("segunda") || diaDaSemana.equals("terca") ||
                diaDaSemana.equals("quarta") || diaDaSemana.equals("quinta") ||
                diaDaSemana.equals("sexta")) {
            System.out.println(diaDaSemana + " é um dia útil.");
        } else {
            System.out.println(diaDaSemana + " não é um dia útil.");
        }

        System.out.println("-".repeat(50));

        double emprestimo = 4050.00;

        if (emprestimo >= 1000 && emprestimo <= 5000) {
            System.out.println("O valor " + emprestimo + " está dentro do intervalo permitido para empréstimo.");
        } else {
            System.out.println("O valor " + emprestimo + " não está dentro do intervalo permitido para empréstimo.");
        }

        System.out.println("-".repeat(50));

        int primerioLado = 3;
        int segundoLado = 4;
        int terceiroLado = 5;

        if (
                primerioLado + segundoLado > terceiroLado &&
                        terceiroLado + segundoLado > primerioLado &&
                        primerioLado + terceiroLado > segundoLado
        ) {
            System.out.println("Os lados podem formar um triângulo.");
        } else {
            System.out.println("Os lados não podem formar um triângulo.");
        }

        System.out.println("-".repeat(50));

        int idade = 20;
        int peso = 45;

        if (idade >= 18 && idade <= 65 && peso>50) {
            System.out.println("O doador é compatível.");
        }else {
            System.out.println("O doador não é compatível.");
            if (idade <= 18 || idade >= 65){
                System.out.println("Motivo: Deve ter entre 18 e 65 anos.");
            }else{
                System.out.println("Motivo: Deve ter mais que 50Kg.");
            }
        }
    }
}