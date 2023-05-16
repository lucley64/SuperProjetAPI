package com.example.projet;

import java.io.File;
import java.util.Scanner;
import java.util.List;

public class CodeAnalyzer {
  private Scanner scanner;
  private File pythonFile;
  private List<String> lines;
  private int nbLines;
  private int functionNumber;
  private List<Integer> nbLineFunction;
  
  public CodeAnalyzer(File inputFile_) throws Exception {
    pythonFile = inputFile_;
    scanner = new Scanner(pythonFile);
    read();
  }

  private void read() {
    String nextLine;
    while (scanner.hasNextLine()) {
      nextLine = scanner.nextLine();
      if (valid(nextLine)) {
        lines.add(nextLine);
      }
    }
  }

  private boolean valid(String line) {
    return !line.equals("\n");
  }

  public int getNbLines() {
    nbLines = lines.size();
    return nbLines;
  }

  private String removeSpaces(String s) {
    int start = 0;
    while (s.charAt(start) == ' ' || s.charAt(start) == '\t') {
      start++;
    }
    return s.substring(start);
  }

  private void getFunctionLine() {
    boolean inFunction = false;
    int nbLines = 0;
    for (String line : lines) {
      if (removeSpaces(line).startsWith("def ")) {
        inFunction = true;
      }
    }
  }

  public int getFunctionMin() {
    return 0;
  }

  public int getFunctionMax() {
    return 0;
  }

  public int getFunctionAvg() {
    return 0;
  }

  public int getFunctionNb() {
    functionNumber = 0;
    for (String line : lines) {
      if (removeSpaces(line).startsWith("def ")) {
        functionNumber++;
      }
    }
    return functionNumber;
  }

  public int nbOccurence(String s) {
    int nbOccurence = 0;

    for (String line : lines) {
      int start = 0;
      nbOccurence--;
      while (start != -1) {
        nbOccurence++;
        start = line.indexOf(s, start);
      }
    }

    return nbOccurence;
  }
}