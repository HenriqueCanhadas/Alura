import java.time.*;
import java.time.format.DateTimeFormatter;

public class Main {
    public static void main(String[] args) {
        System.out.println("Oi");

        LocalDate dataCompra = LocalDate.now();
        LocalDate dataPrimeiraParcela = LocalDate.of(2025,5,15);
        LocalDate dataSegundaParcela = dataPrimeiraParcela.plusDays(30);

        if(dataPrimeiraParcela.isBefore(LocalDate.now())){
            System.out.println("Vence hoje");
        }else{
            System.out.println("ainda nao");
        }

        System.out.println(dataCompra);
        System.out.println(dataPrimeiraParcela);
        System.out.println(dataSegundaParcela);

        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println(dataCompra.format(formato));

        ZonedDateTime dataConclusaoCompra = ZonedDateTime.now();
        System.out.println(dataConclusaoCompra);

        ZonedDateTime dataCompraNy = dataConclusaoCompra.withZoneSameInstant(ZoneId.of("America/New_York"));
        System.out.println(dataCompraNy);

        LocalTime inicio = LocalTime.of(7,30);
        LocalTime fim = LocalTime.of(17,30);
        Duration duracao = Duration.between(inicio,fim);

        System.out.println("Duração do expediente: " + duracao.toHours() + " horas e " + duracao.toMinutesPart() + " minutos.");

        LocalDate dataPagamento = LocalDate.parse("2025-10-30");
        Period periodo = Period.between(dataCompra,dataPagamento);
        System.out.println("Diferença em dias: " + periodo.getDays());

        System.out.println("-".repeat(50));

        LocalDate dataAtual = LocalDate.now();
        LocalTime horaAtual = LocalTime.now();

        System.out.println("Data atual: "+dataAtual);
        System.out.println("Hora atual: "+horaAtual);

        System.out.println("-".repeat(50));

        DateTimeFormatter dataFormatada = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        DateTimeFormatter horaFormatada = DateTimeFormatter.ofPattern("HH:mm");

        System.out.println("Data formatada: "+dataAtual.format(dataFormatada));
        System.out.println("Hora formatada: "+horaAtual.format(horaFormatada));

        System.out.println("-".repeat(50));

        LocalTime hora1 = LocalTime.of(14,30);
        LocalTime hora2 = LocalTime.of(16,45);
        Duration tempo = Duration.between(hora1,hora2);

        System.out.println("Diferença de tempo: " + tempo.toHours() + " horas e " + tempo.toMinutesPart() + " minutos.");

        System.out.println("-".repeat(50));

        LocalDate dataFinal = dataAtual.plusDays(30);

        DateTimeFormatter dataFinalFormatada = DateTimeFormatter.ofPattern("dd-MM-yyyy");

        System.out.println("Data de entrega: "+dataFinal.format(dataFinalFormatada));

        System.out.println("-".repeat(50));

        LocalDate dataVencimento = dataFinal.plusMonths(2);
        DateTimeFormatter dataVencimentoFormatada = DateTimeFormatter.ofPattern("dd-MM-yyyy");

        System.out.println("Nova data de vencimento: "+ dataVencimento.format(dataVencimentoFormatada));

        System.out.println("-".repeat(50));

        LocalDate dataEvento = LocalDate.of(2025,6,18);
        //dataAtual
        DateTimeFormatter dataEventoFormatada = DateTimeFormatter.ofPattern("dd-MM-yyyy");

        System.out.println("Data do evento: "+dataEvento.format(dataEventoFormatada));
        System.out.println("Data atual: "+dataAtual.format(dataEventoFormatada));

        if(dataAtual.isEqual(dataEvento)){
            System.out.println("Evento hoje");
        }else if(dataAtual.isAfter(dataEvento)){
            System.out.println("O evento já ocorreu.");
        }else{
            System.out.println("O evento ainda não ocorreu.");
        }

        System.out.println("-".repeat(50));

        //ZonedDateTime horarioSP = ZonedDateTime.now();
        //ZonedDateTime horarioTokyo = horarioSP.withZoneSameInstant(ZoneId.of("Asia/Tokyo"));
        ZonedDateTime horarioTokyo = ZonedDateTime.now(ZoneId.of("Asia/Tokyo"));
        DateTimeFormatter horaFormatadaTokyo = DateTimeFormatter.ofPattern("HH:mm:ss");

        System.out.println("Horário atual em Tóquio: "+ horarioTokyo.format(horaFormatadaTokyo));

        System.out.println("-".repeat(50));

        ZonedDateTime horarioSP = ZonedDateTime.now();
        ZonedDateTime horarioSydney = horarioSP.withZoneSameInstant(ZoneId.of("Australia/Sydney"));
        DateTimeFormatter horaFormatadaSydney = DateTimeFormatter.ofPattern("HH:mm");

        System.out.println("Horário atual no sistema: "+horarioSP.format((horaFormatadaSydney)));
        System.out.println("Horário atual em Sydney: "+ horarioSydney.format(horaFormatadaSydney));

    }

}