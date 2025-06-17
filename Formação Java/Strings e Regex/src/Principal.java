import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Principal {
    public static void main(String[] args) {
        String texto = "Meu nome e julia@gmail.com";
        Pattern pattern = Pattern.compile("\\w+@\\w+.\\w+");
        Matcher matcher = pattern.matcher(texto);
        
        if (matcher.find()){
            System.out.println(matcher.group());
        }
        
    }
}
