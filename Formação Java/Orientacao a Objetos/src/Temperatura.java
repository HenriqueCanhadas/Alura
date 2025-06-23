public class Temperatura {
    String local;
    double temperatura;

    public void verificarTemperatura(){
        if (temperatura >= 37.5 && local.equals("Setor A")){
            System.out.println("Alerta: Temperatura acima do limite!");
        }else {
            System.out.println("Temperatura abaixo do limite!");
        }

    }
}
