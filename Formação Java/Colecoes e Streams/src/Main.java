import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<String> funcionarios = new ArrayList<>();

        funcionarios.add("Jõao");
        funcionarios.add("Maria");
        funcionarios.add("Jose");
        funcionarios.add("Jõao");

        System.out.println(funcionarios);
        System.out.println(funcionarios.getFirst());
        System.out.println(funcionarios.getLast());
        System.out.println(funcionarios.get(1));

        Set<String> produtos = new HashSet<>();

        produtos.add("Agua");
        produtos.add("Coca-Cola");
        produtos.add("Agua");

        System.out.println(produtos);

        Map<Integer,String> cliente = new HashMap<>();
        cliente.put(1,"Maria");
        cliente.put(2,"Joana");
        cliente.put(3,"Julia");
        cliente.put(4,"Bia");

        System.out.println(cliente.get(1));

        List<String> funcionarios1 = List.of("Ana", "Bruno", "Carlos", "Amanda");

        List<String> funcionariosLetraA = funcionarios1.stream().
                filter(f -> f.startsWith("A")).
                collect(Collectors.toList());

        System.out.println(funcionarios1);
        System.out.println(funcionariosLetraA);

        List<Double> valorVendas = List.of(500.0, 1800.0, 6200.0);

        List<Double> comisao = valorVendas.stream().
                map(v -> v * 0.05)
                .collect(Collectors.toList());

        System.out.println(valorVendas);
        System.out.println(comisao);


        double totalVendas = valorVendas.stream()
        .reduce(0.0,Double::sum);

        System.out.println(totalVendas);

        System.out.println("-".repeat(50));

        List<String> funcionarios2 = new ArrayList<>();

        funcionarios2.add("Jõao");
        funcionarios2.add("Maria");
        funcionarios2.add("Vitor");
        funcionarios2.add("Ana");

        System.out.println("Lista de funcionários: "+funcionarios2);

        System.out.println("-".repeat(50));

        List<String> funcionarios3 = new ArrayList<>();

        funcionarios3.add("Joana");
        funcionarios3.add("Lucas");
        funcionarios3.add("Pedro");
        funcionarios3.add("Antônio");

        System.out.println("Lista inicial: "+funcionarios3);

        funcionarios3.remove("Pedro");

        System.out.println("Lista após a exclusão: "+funcionarios3);

        System.out.println("-".repeat(50));

        List<String> funcionarios4 = new ArrayList<>();
        funcionarios4.add("João");
        funcionarios4.add("Maria");
        funcionarios4.add("Ana");
        funcionarios4.add("Pedro");
        funcionarios4.add("Antônio");

        System.out.println("A segunda pessoa da lista é: "+funcionarios4.get(1));
        System.out.println("Total de funcionários: "+ funcionarios4.size());

        System.out.println("-".repeat(50));

        Set<String> eventos = new HashSet<>();
        eventos.add("IA Conference Brasil");
        eventos.add("AI Summit");
        eventos.add("DevFest");
        eventos.add("Cloud Expo");
        eventos.add("IA Conference Brasil");
        eventos.add("DevFest");

        System.out.println("Lista de eventos: "+eventos);

        System.out.println("-".repeat(50));

        Map<Integer,String> cliente1 = new HashMap<>();
        cliente1.put(1,"Maria");
        cliente1.put(2,"Joana");
        cliente1.put(3,"Julia");
        cliente1.put(4,"Bia");

        System.out.println("O nome do cliente com ID 2 é: "+cliente1.get(2));

        System.out.println("-".repeat(50));

        int id = 4;

        Map<Integer,String> clientes = new HashMap<>();
        clientes.put(1, "Maria");
        clientes.put(2, "Marcos");
        clientes.put(3, "Ana");
        clientes.put(4, "Joana");
        clientes.put(5, "Karen");

        if(clientes.containsKey(id)){
            System.out.println("O nome do cliente com ID "+id+" é: "+clientes.get(id));
        }else {
            System.out.println(" Cliente com ID "+id+" não encontrado.");
        }

        System.out.println("-".repeat(50));

        List<String> funcionarios5 = List.of("Ana", "Bruno", "Carlos", "Amanda", "Alice", "Daniel", "Caroline");

        List<String> funcionarios5digitos = funcionarios5.stream().
                filter(f -> f.length()<=5).
                collect(Collectors.toList());

        System.out.println(funcionarios5digitos);

        System.out.println("-".repeat(50));

        List<Integer> numeros = List.of(2, 3, 5, 7, 11);

        List<Integer> quadrado = numeros.stream().
                map(v -> v * v)
                .collect(Collectors.toList());

        System.out.println(quadrado);

        System.out.println("-".repeat(50));

        List<Double> precosProdutos = List.of(29.99, 49.50, 15.75, 99.99);

        double antesImposto = precosProdutos.stream()
                .reduce(0.0,Double::sum);
        
        double imposto = antesImposto * 0.08;
        double totalComImposto = antesImposto + imposto;

        System.out.println("Valor total antes do imposto: " + String.format("%.2f", antesImposto));
        System.out.println("Valor total com imposto de 8%: " + String.format("%.2f", totalComImposto));

    }
}