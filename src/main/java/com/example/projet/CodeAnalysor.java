package com.example.projet;

import java.io.File;
import java.util.Scanner;
public class CodeAnalysor {
  Scanner scanner;
  File pythonFile;
  public CodeAnalysor(File inputFile_) throws Exception {
    pythonFile = inputFile_;
    scanner = new Scanner(pythonFile);
  }

  public void read() {
    while (scanner.hasNextLine()) {
      System.out.println(scanner.nextLine());
    }
  }
}