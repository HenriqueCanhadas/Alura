public class Main {
    public static void main(String[] args) {
        //int quantidadePassos = 500;
        //double alturaEmMetros = 1.60;
        //String nome = "Jose";

        //int alturaEmCentimetros = 170;
        //alturaEmMetros = alturaEmCentimetros;
        //System.out.println(alturaEmMetros / 100);

        String nome = "Maria";
        int idade = 25;
        double altura = 1.68;
        boolean estudante = true;
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + altura);
        System.out.println("É estudante: " + estudante);

        System.out.println("-".repeat(50));

        double valorDouble = 19.5;
        System.out.println("O valor inteiro do produto é: " + (int) valorDouble);

        System.out.println("-".repeat(50));

        double nota1 = 7.5;
        double nota2 = 8.0;
        double nota3 = 9.0;
        double media = (nota1+nota2+nota3) / 3;
        System.out.println("A média das notas é: " + media);

        System.out.println("-".repeat(50));

        int celsius = 20;
        double fahrenheit = (celsius * 9 / 5) + 32;
        System.out.println("A temperatura em graus Fahrenheit é:" + fahrenheit);

        System.out.println("-".repeat(50));

        String titulo = "O Pequeno Príncipe";
        String autor = "Antoine de Saint-Exupéry";
        int numeroDePaginas = 96;
        double precoDoLivro = 39.9;
        char categoria = 'F';
        String categoriaDescricao;
        if (categoria == 'F') {
            categoriaDescricao = "Ficção";
        } else if (categoria == 'N') {
            categoriaDescricao = "Não-ficção";
        } else if (categoria == 'T') {
            categoriaDescricao = "Tecnologia";
        } else if (categoria == 'H') {
            categoriaDescricao = "História";
        } else {
            categoriaDescricao = "Categoria inválida";
        }
        System.out.println("Livro cadastrado: \"" + titulo + "\", de " + autor + ". Ele possui " + numeroDePaginas + " páginas, custa R$" + precoDoLivro + " e pertence à categoria " + categoriaDescricao + ".");

        System.out.println("-".repeat(50));

        double preco = 150.00;
        String categoriaPreco;
        if (preco <= 50.00) {
            categoriaPreco = "Econômico";
        } else if (preco > 50.00 && preco <= 200.00) {
            categoriaPreco = "Intermediário";
        } else if (preco > 200.00) {
            categoriaPreco = "Premium";
        }else {
            categoriaPreco = "Categoria inválida";
        }
        System.out.println("Categoria do produto: " + categoriaPreco);

        System.out.println("-".repeat(50));

        int numero = 7;

        if (numero % 2 == 0) {
            System.out.println("O número é par.");
        } else {
            System.out.println("O número é ímpar.");
        }

        System.out.println("-".repeat(50));

        double valorReais = 451.50;

        System.out.println("O valor em dólares é:" + valorReais / 5.25);

    }
}