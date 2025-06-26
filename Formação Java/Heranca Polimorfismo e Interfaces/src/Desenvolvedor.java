public class Desenvolvedor extends Funcionario{
    private String stack;

    public Desenvolvedor(String nome, double salario, String stack) {
        super(nome, salario);
        this.stack = stack;
    }

    @Override
    public void exibirInformacoes() {
        System.out.printf("\nDesenvolvedor: %s salário %.2f - Stack: %s",
                nome, salario, stack);
    }

    @Override
    public void calculaPLR() {
        System.out.println("PLR do desenvolvedor");
    }
}
