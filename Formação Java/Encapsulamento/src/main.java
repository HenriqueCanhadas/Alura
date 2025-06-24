public class main {
    public static void main(String[] args) {
        Funcionario funcionario = new Funcionario("Joao", 8500);
        funcionario.setCargo("Desenvolvedor");

        System.out.println("Funcionario tem o nome:"+ funcionario.getNome());
        System.out.println("Funcionario tem o cargo:"+ funcionario.getCargo());
        System.out.println("Funcionario tem o salario:"+ funcionario.getSalario());

        funcionario.reajustarSalario(5);

        funcionario.reajustarSalario(15);

        System.out.println("-".repeat(50));

        Carro gol = new Carro("Gol", "ABC-1234", 2020);

        System.out.println("Veículo cadastrado:");
        System.out.println("Modelo: " + gol.getModelo());
        System.out.println("Placa:" + gol.getPlaca());
        System.out.println("Ano:" + gol.getAno());

        System.out.println("-".repeat(50));

        Estoque mouse = new Estoque(59.90,"Mouse");

        mouse.validar();

        System.out.println("-".repeat(50));

        Usuario user = new Usuario("123456");
        user.setSenha("12346","abc123");

        System.out.println("-".repeat(50));

        Bateria b = new Bateria();
        b.setNivel(85);

        System.out.println("-".repeat(50));

        Banco conta = new Banco("Ana");
        conta.depositar(1000.00);
        conta.sacar(200.00);
        conta.exibirSaldo();

        System.out.println("-".repeat(50));

        Filme matrix = new Filme("Matrix");
        matrix.adicionarAvaliacao(5);
        matrix.adicionarAvaliacao(4);
        matrix.adicionarAvaliacao(5);
        matrix.adicionarAvaliacao(3);
        matrix.adicionarAvaliacao(4);

        matrix.verMedia();

    }
}
