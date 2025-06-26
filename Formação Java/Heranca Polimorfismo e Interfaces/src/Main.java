public class Main {
    public static void main(String[] args) {
        Funcionario gerente = new Gerente("Mario",15000);
        gerente.reajustarSalario(2);
        ((Gerente) gerente).setBonus(1000);
        gerente.exibirInformacoes();
        ((Gerente) gerente).aprovarProjeto("uso de Ia nos codgos");

        Funcionario desenvolvedor = new Desenvolvedor("Carla", 1200, "Backend Java");
        desenvolvedor.reajustarSalario();
        desenvolvedor.exibirInformacoes();


    }
}
