public class Funcionario {
    private String nome;
    private String cargo;
    private double salario;
    private int controleReajuste = 0;


    public Funcionario(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }

    public double getSalario() {
        return salario;
    }

    public String getNome() {
        return nome;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public void reajustarSalario(double percentual) {
        if(controleReajuste>=1){
            System.out.println("\nNão pode fazer mais reajustes!!!");
        }else {
            controleReajuste++;
            salario += salario * (percentual / 100);
            System.out.printf("\nNovo salario de %s é %.2f ", nome, salario);
        }
    }
}
