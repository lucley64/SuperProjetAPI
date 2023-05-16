package com.example.projet;

import java.io.File;
import java.util.Scanner;
import java.util.List;

public class CodeAnalysor {
  private Scanner scanner;
  private File pythonFile;
  private List<String> lines;
  private int nbLines;
  private int functionNumber;
  
  public CodeAnalysor(File inputFile_) throws Exception {
    pythonFile = inputFile_;
    scanner = new Scanner(pythonFile);
  }

  public void read() {
    String nextLine;
    while (scanner.hasNextLine()) {
      nextLine = scanner.nextLine();
      if (valid(nextLine)) {
        lines.add(nextLine);
      }
    }
  }

  private boolean valid(String line) {
    return true;
  }

  public int getNbLines() {
    nbLines = lines.size();
    return nbLines;
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
      if (line.startsWith("def ")) {
        functionNumber++;
      }
    }
    return functionNumber;
  }

  public int nbOccurence() {
    return 0;
  }
}