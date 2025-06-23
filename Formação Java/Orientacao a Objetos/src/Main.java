import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Funcionario funcionario1 = new Funcionario();
        funcionario1.nome = "Pele";
        funcionario1.cargo = "Gerente";
        funcionario1.salario = 9000;

        Funcionario funcionario2 = new Funcionario();
        funcionario2.nome = "Joao";
        funcionario2.cargo = "Desenvolvedor";
        funcionario2.salario = 5000;

        funcionario1.exibirInformacoes();
        funcionario2.exibirInformacoes();

        funcionario2.reajustarSalario(5);

        funcionario2.exibirInformacoes();

        System.out.println("-".repeat(50));

        Produto produto1 = new Produto();
        produto1.nome = "Mouse Gamer";
        produto1.preco = 159.90;
        produto1.quantidade = 25;

        produto1.exibirInformacoes();

        System.out.println("-".repeat(50));

        Biblioteca livro1 = new Biblioteca();
        livro1.titulo = "O Guia do Mochileiro das Galáxias";
        livro1.autor = "Douglas Adams";
        livro1.paginas = 208;

        livro1.exibirInformacoes();

        System.out.println("-".repeat(50));

        Banco saldo1 = new Banco();
        saldo1.salario = 1579.42 ;

        saldo1.exibirSaldo();
        saldo1.zerarSaldo();
        saldo1.exibirSaldo();

        System.out.println("-".repeat(50));

        Temperatura setor1 = new Temperatura();
        setor1.local = "Setor A";
        setor1.temperatura = 39.2;

        setor1.verificarTemperatura();

        System.out.println("-".repeat(50));

        Escola aluno1 = new Escola();

        aluno1.aluno = "João Silva";
        aluno1.nota1 = 6.5;
        aluno1.nota2 = 7.5;

        aluno1.calcularMedia();

        System.out.println("-".repeat(50));

        Tarefa t1 = new Tarefa();
        t1.descricao = "Estudar Java";
        t1.concluida = false;

        Tarefa t2 = new Tarefa();
        t2.descricao = "Fazer exercícios";
        t2.concluida = true;

        List<Tarefa> lista = new ArrayList<>();
        lista.add(t1);
        lista.add(t2);

        for (Tarefa t : lista) {
            t.consultarTarefas();
        }
    }
}