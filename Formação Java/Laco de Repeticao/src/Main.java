import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        int degrau = 5;
        System.out.println("Digite a quantidade de degraus:" + degrau);
        for (int i = 0; i < degrau; i++) {
            System.out.println("Subindo o degrau " + (i + 1));
        }
        System.out.println("Você chegou ao topo!");

        System.out.println("-".repeat(50));

        int[] valores = {10, 20, 30, 40, 50};
        int total = 0;
        for (int valor : valores) {
            total += valor;
        }
        System.out.println("A soma total das receitas é: " + total);

        System.out.println("-".repeat(50));

        int inicio = 0;
        int fim = 101;
        int soma = 0;
        while (inicio < fim) {
            if (inicio % 2 == 0) {
                soma += inicio;
            }
            inicio++;
        }
        System.out.println("A soma dos números pares de 1 a 100 é: " + soma);

        System.out.println("-".repeat(50));

        int numero = 6;
        int fatorial = 1;
        for (int i = 1; i < numero; i++) {
            fatorial *= i;
        }
        System.out.println("O fatorial de 5 é: "+ fatorial);

        System.out.println("-".repeat(50));

        int tentativa = 3;
        int senha = 1234;

        while(tentativa>0){
            int entrada = 123;
            if (entrada == senha){
                System.out.println("Senha Correta! Acesso concedido!");
                break;
            }else if (tentativa > 1) {
                System.out.println("Senha incorreta. Você tem " + (tentativa - 1) + " tentativas restantes.");
                tentativa--;
            } else {
                System.out.println("Conta bloqueada temporariamente.");
                break;
            }
        }

        System.out.println("-".repeat(50));

        int num = 20;

        for(int i=0; i<num; i++){
            if (i % 10 == 5){
                continue;
            }
            System.out.printf(" "+i);
        }
    }
}
