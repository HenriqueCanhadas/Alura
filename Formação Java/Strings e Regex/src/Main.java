import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
    public static void main(String[] args) {
        /*
        String professor = "Jacqueline Oliveira";
        String disciplina = "Java e Programação Orientada a Objetos";
        String curriculo = """
                "Pós-graduada em Engenharia e "
                "Arquitetura de Software; "
                "Desenvolvedora backend Java desde 2010; "
                """;

        String texto = String.format("Disciplina: %s - %s", disciplina, professor);
        System.out.println(texto);
        System.out.printf("Nome: %s %nDisciplina: %s", professor, disciplina);
        System.out.println("\n"+curriculo);
        */
        System.out.println("-".repeat(50));

        String nome = "Digite o nome:    João Silva ";
        String nomeFormatado = nome.trim();
        System.out.println("teste " + nomeFormatado);

        System.out.println("-".repeat(50));

        String texto = "Digite o texto: Olá, Mundo!";
        System.out.println(texto.toLowerCase());
        System.out.println(texto.toUpperCase());

        System.out.println("-".repeat(50));

        String texto1 = "O gato caça o rato.";
        String texto2 = "gato";
        String texto3 = "cachorro";
        System.out.println(texto1.replace(texto2,texto3));

        System.out.println("-".repeat(50));

        String texto4 = "relatorio_final.pdf";
        int index = texto4.lastIndexOf('.');
        if (index != -1) {
            System.out.println(texto4.substring(0, index));
        } else {
            System.out.println("Erro");
        }

        System.out.println("-".repeat(50));

        String texto5 = "O gato caça o rato.";
        String texto6 = "gato";
        System.out.println(texto5.contains(texto6));

        System.out.println("-".repeat(50));

        Double texto7 = 19.9876;
        System.out.printf("Valor formatado: R$ %.2f", texto7);

        System.out.println("-".repeat(50));

        String texto8 = "ABC-1234";
        Pattern pattern = Pattern.compile("^[A-Z]{3}-\\d{4}$");
        Matcher matcher = pattern.matcher(texto8);
        if (matcher.find()){
            System.out.println(matcher.group());
        }else{
            System.out.println("Erro");
        }

        System.out.println("-".repeat(50));

        String texto9 = "123.456.789-09";
        String regex = "\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}";

        if (texto9.matches(regex)) {
            System.out.println("O CPF " + texto9  + " está no formato válido.");
        } else {
            System.out.println("O CPF " + texto9  + " não está no formato válido.");
        }

        System.out.println("-".repeat(50));

        String texto10 = " Olá #mundo! Estou aprendendo #Java e #programação.";
        Pattern pattern1 = Pattern.compile("#\\w+");
        Matcher matcher1 = pattern1.matcher(texto10);
        ArrayList<String> hashtags = new ArrayList<>();
        while (matcher1.find()) {
            hashtags.add(matcher1.group());
        }
        if (hashtags.isEmpty()) {
            System.out.println("Nenhuma hashtag encontrada.");
        } else {
            System.out.println("Hashtags encontradas: " + String.join(", ", hashtags));
        }

        System.out.println("-".repeat(50));

        String senha1 = "abc123";

        String regex1 = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$";
        if (senha1.matches(regex1)) {
            System.out.println("A senha é válida.");
        } else {
            System.out.println("A senha não é válida.");
        }
    }
}