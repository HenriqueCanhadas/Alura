public class Bateria {
    private int porcentagem;

    public void setNivel(int porcentagem) {
        if (porcentagem >= 0 && porcentagem <= 100){
            if(porcentagem <= 20){
                System.out.println("Status: Bateria fraca ");
            } else if (porcentagem >= 21 && porcentagem <= 79) {
                System.out.println("Status: Bateria ok ");
            }else{
                System.out.println("Status: Bateria cheia ");
            }
        }else {
            System.out.println("Valor de Nivel Invalido");
        }
    }

}
