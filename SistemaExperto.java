import java.util.Scanner;

public class SistemaExperto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bienvenido al Sistema Experto de Diagnostico Medico");
        System.out.println("Por favor, responde con 'si' o 'no' a las siguientes preguntas:");

        String fiebre = obtenerRespuesta(scanner, "1. Tienes fiebre?");
        String tos = obtenerRespuesta(scanner, "2. Tienes tos?");
        String dolorGarganta = obtenerRespuesta(scanner, "3. Tienes dolor de garganta?");
        String fatiga = obtenerRespuesta(scanner, "4. Sientes fatiga o cansancio extremo?");
        String dolorCabeza = obtenerRespuesta(scanner, "5. Tienes dolor de cabeza?");
        String dolorMuscular = obtenerRespuesta(scanner, "6. Tienes dolor muscular?");
        String dificultadRespirar = obtenerRespuesta(scanner, "7. Tienes dificultad para respirar?");
        String perdidaOlfatoGusto = obtenerRespuesta(scanner, "8. Tienes perdida de olfato o gusto?");
        String escalofrios = obtenerRespuesta(scanner, "9. Tienes escalofrios?");
        String nauseasVomitos = obtenerRespuesta(scanner, "10. Tienes nauseas o vomitos?");
        String dolorPecho = obtenerRespuesta(scanner, "11. Tienes dolor en el pecho?");
        String dolorEstomago = obtenerRespuesta(scanner, "12. Tienes dolor de estomago?");
        String diarrea = obtenerRespuesta(scanner, "13. Tienes diarrea?");
        String secrecionNasal = obtenerRespuesta(scanner, "14. Tienes secrecion nasal?");

        diagnosticar(fiebre, tos, dolorGarganta, fatiga, dolorCabeza, dolorMuscular, dificultadRespirar, perdidaOlfatoGusto, escalofrios, nauseasVomitos, dolorPecho, dolorEstomago, diarrea, secrecionNasal);
    }

    private static String obtenerRespuesta(Scanner scanner, String pregunta) {
        System.out.println(pregunta);
        String respuesta = scanner.nextLine().toLowerCase();

        while (!respuesta.equals("si") && !respuesta.equals("no")) {
            System.out.println("Por favor, responde con 'si' o 'no'.");
            respuesta = scanner.nextLine().toLowerCase();
        }

        return respuesta;
    }

    public static void diagnosticar(String fiebre, String tos, String dolorGarganta, String fatiga, String dolorCabeza, String dolorMuscular, String dificultadRespirar, String perdidaOlfatoGusto, String escalofrios, String nauseasVomitos, String dolorPecho, String dolorEstomago, String diarrea, String secrecionNasal) {

        // Verifica si el usuario no tiene ningun malestar
        if (fiebre.equals("no") && tos.equals("no") && dolorGarganta.equals("no") && fatiga.equals("no") && dolorCabeza.equals("no") && dolorMuscular.equals("no") && dificultadRespirar.equals("no") && perdidaOlfatoGusto.equals("no") && escalofrios.equals("no") && nauseasVomitos.equals("no") && dolorPecho.equals("no") && dolorEstomago.equals("no") && diarrea.equals("no") && secrecionNasal.equals("no")) {
            System.out.println("No tienes ningun malestar. Parece que estas saludable.");
            return; 
        }

        // Reglas basadas en sintomas
        if (fiebre.equals("si") && tos.equals("si") && dificultadRespirar.equals("si") && perdidaOlfatoGusto.equals("si")) {
            System.out.println("Posible diagnostico: COVID-19");
        } else if (fiebre.equals("si") && dolorCabeza.equals("si") && fatiga.equals("si") && dolorMuscular.equals("si") && escalofrios.equals("si")) {
            System.out.println("Posible diagnostico: Gripe");
        } else if (fiebre.equals("si") && tos.equals("si") && dolorGarganta.equals("si") && escalofrios.equals("no")) {
            System.out.println("Posible diagnostico: Faringitis");
        } else if (fiebre.equals("si") && tos.equals("si") && dolorCabeza.equals("si") && fatiga.equals("no") && dificultadRespirar.equals("no")) {
            System.out.println("Posible diagnostico: Resfriado comun");
        } else if (tos.equals("si") && dolorGarganta.equals("si") && secrecionNasal.equals("si") && fiebre.equals("no")) {
            System.out.println("Posible diagnostico: Alergia");
        } else if (fiebre.equals("si") && nauseasVomitos.equals("si") && dolorCabeza.equals("si") && escalofrios.equals("si") && diarrea.equals("si")) {
            System.out.println("Posible diagnostico: Gastroenteritis");
        } else if (dificultadRespirar.equals("si") && fatiga.equals("si") && dolorMuscular.equals("no") && fiebre.equals("no") && dolorCabeza.equals("no")) {
            System.out.println("Posible diagnostico: Asma");
        } else if (tos.equals("si") && dificultadRespirar.equals("si") && fiebre.equals("si") && fatiga.equals("si") && dolorMuscular.equals("si")) {
            System.out.println("Posible diagnostico: Neumonia");
        } else if (dolorPecho.equals("si") && dificultadRespirar.equals("si") && fiebre.equals("si")) {
            System.out.println("Posible diagnostico: Bronquitis o infeccion pulmonar");
        } else if (dolorEstomago.equals("si") && diarrea.equals("si") && fiebre.equals("no")) {
            System.out.println("Posible diagnostico: Intoxicacion alimentaria");
        } else {
            // Diagnostico generico si no coincide con las reglas anteriores
            System.out.println("Posible diagnostico: Infeccion viral o bacteriana no especificada. Se recomienda consultar a un medico para una evaluacion mas detallada.");
        }
    }
}
