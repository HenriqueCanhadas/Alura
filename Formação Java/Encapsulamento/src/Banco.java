public class Banco {
    private String nome;
    private double saldo;

    public Banco(String nome) {
        this.nome = nome;
        this.saldo = 0;
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public void sacar(double valor) {
        if (valor > saldo){
            System.out.println("Saldo insuficiente para saque.");
            System.out.println("Saldo atual de Ana: "+saldo);
        }else {
            saldo -= valor;
            System.out.println("Saldo atual de" +nome+ ": "+saldo);
        }
    }

    public void exibirSaldo() {
        System.out.println("Saldo atual de" +nome+ ": "+saldo);
    }

}
