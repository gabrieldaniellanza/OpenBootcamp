/* package com.gdlservicios;

import java.util.Scanner;

public class CuatroListas {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        String[][] nombres = new String[4][100];
        Integer[] ultimo = new Integer[] {0,0,0,0};

        int grupo = 0;
        String nombre;

        while(true) {
            System.out.println("Ingrese el grupo [Sale con 0]:");
            grupo = reader.nextInt();

            if(grupo < 1 || grupo > 4) break;

            grupo--;
            if(ultimo[grupo] < 100){
                System.out.println("Ingrese el nombre:");
                reader = new Scanner(System.in);
                nombre = reader.nextLine();

                nombres[grupo][ultimo[grupo]] = nombre;
                ultimo[grupo]++;
            }
            System.out.println("");
        };

        System.out.println("Seleccione el grupo a imprimir:");
        grupo = reader.nextInt()-1;

        System.out.println("");
        System.out.println("Grupo ordenado:");

        String[] grupoOrdenar = nombres[grupo];

        for(int i = 0; i < grupoOrdenar.length - 1; i++)
        {
            if(grupoOrdenar[i] == null) break;

            for(int j = i+1; j < grupoOrdenar.length; j++)
            {
                if(grupoOrdenar[j] == null) break;

                if(grupoOrdenar[i].compareTo(grupoOrdenar[j]) > 0)
                {
                    String temp = grupoOrdenar[i];
                    grupoOrdenar[i] = grupoOrdenar[j];
                    grupoOrdenar[j] = temp;
                }
            }
        }

        for (String nom: nombres[grupo])
        {
            if(nom == null) break;
            System.out.println(nom);
        }

    }
}

 */
