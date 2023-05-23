package com.example.projet;

import java.io.File;
import java.util.List;

import org.junit.jupiter.api.Test;

class TestCodeAnalyzer {

    @Test
    void testInitialisationClasse() throws Exception {
        File myFile = new File("./src/main/res/python/test.py");
        CodeAnalyzer test = new CodeAnalyzer(myFile);
    }

    @Test
    void testNbLines() throws Exception {
        File myFile = new File("./src/main/res/python/test.py");
        CodeAnalyzer test = new CodeAnalyzer(myFile);
        System.out.println(test.getNbLines());
    }

    public static void main(String[] args) throws Exception{
        File myFile = new File("./src/main/res/python/timer.py");
        CodeAnalyzer test = new CodeAnalyzer(myFile);
        List<Integer> list = test.getNbLineFunction();
        for (int i : list) {
            System.out.println(i);
        }

    }
}