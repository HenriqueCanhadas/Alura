public class Funcionario {
    String nome;
    String cargo;
    double salario;

    public void exibirInformacoes(){
        System.out.println("Funcionario "+nome+" - Cargo: "+cargo+" - Salário "+salario);
    }

    public void reajustarSalario(double percentual){
        salario += salario * (percentual / 100);
        System.out.println("Novo salario: "+salario);
    }
}
