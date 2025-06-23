public class Banco {
    double salario;

    public void exibirSaldo(){
        System.out.println("Saldo atual: R$ "+salario);
    }

    public void zerarSaldo(){
        salario = 0;
    }
}
