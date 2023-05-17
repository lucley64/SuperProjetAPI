package com.example.projet;

import java.io.File;
import java.util.Scanner;
import java.util.LinkedList;
import java.util.Stack;

public class CodeAnalyzer {
  private Scanner scanner;
  private File pythonFile;
  private LinkedList<String> lines;
  private int nbLines;
  private int functionNumber;
  private LinkedList<Integer> nbLineFunction;
  private String fileContent;
  
  public CodeAnalyzer(File inputFile_) throws Exception {
    pythonFile = inputFile_;
    scanner = new Scanner(pythonFile);
    lines = new LinkedList<String>();
    nbLineFunction = new LinkedList<Integer>();

    readFile();
    calculateFunctionLine();
    calculateFunctionNb();
  }

  public CodeAnalyzer(String fileContent_) {
    fileContent = fileContent_;
    lines = new LinkedList<String>();
    nbLineFunction = new LinkedList<Integer>();

    readString();
    calculateFunctionLine();
    calculateFunctionNb();
  }

  private void readFile() {
    String nextLine;
    while (scanner.hasNextLine()) {
      nextLine = scanner.nextLine();
      if (valid(nextLine)) {
        lines.add(nextLine);
      }
    }
  }

  private void readString() {
    int start = 0;
    int end = fileContent.indexOf("\n");
    String line;
    while (end != -1) {
      line = fileContent.substring(start, end);
      if (valid(line)) {
        lines.add(line);
      }
      start = end + 1;
      end = fileContent.indexOf("\n", start);
    }
    if (start < fileContent.length()) {
      lines.add(fileContent.substring(start));
    }
  }

  private boolean valid(String line) {
    int start = 0;
    while (start != -1) {
      start++;
      line = line.substring(start);
    } 
    return !line.equals("");
  }

  public int getNbLines() {
    nbLines = lines.size();
    return nbLines;
  }

  private String removeSpaces(String s) {
    int start = 0;
    if (s.length() == 0) {
      return s;
    }
    while (s.charAt(start) == ' ') {
      start++;
    }
    return s.substring(start);
  }

  private int nbIndent(String s) {
    int res = 0;
    if (s.length() == 0) {
      return 0;
    }

    while (res < s.length() && s.charAt(res) == ' ') {
      res++;
    }
    return res;
  }

  private void calculateFunctionLine() {
    nbLineFunction.clear();
    Stack<Integer> stack = new Stack<Integer>();
    Stack<Integer> indents = new Stack<Integer>();
    int lineIndex = 0;

    for (String line : lines) {
      int nbIndentsCurrent = nbIndent(line);
      if (!indents.isEmpty()) {
        while (!indents.isEmpty() && nbIndentsCurrent <= indents.peek()) {
          nbLineFunction.add(lineIndex - stack.pop());
          indents.pop();
        }
      }
      if (removeSpaces(line).startsWith("def ")) {
        stack.push(lineIndex);
        indents.push(nbIndentsCurrent);
      }
      lineIndex++;
    }

    while (!stack.isEmpty()) {
      nbLineFunction.add(lineIndex - stack.pop());
    }
  }

  public int getFunctionMin() {
    int min = 0;
    for (int nbLine : nbLineFunction) {
      if (nbLine < min || min == 0) {
        min = nbLine;
      }
    }
    return min;
  }

  public int getFunctionMax() {
    int max = 0;
    for (int nbLine : nbLineFunction) {
      if (nbLine > max) {
        max = nbLine;
      }
    }
    return max;
  }

  public float getFunctionAvg() {
    int total = 0;
    for (int nbLine : nbLineFunction) {
      total += nbLine;
    }
    return (float)total / functionNumber;
  }

  private void calculateFunctionNb() {
    functionNumber = 0;
    for (String line : lines) {
      if (removeSpaces(line).startsWith("def ")) {
        functionNumber++;
      }
    }
  }

  public int getFunctionNb() {
    return functionNumber;
  }

  public int getNbOccurence(String s) {
    int nbOccurence = 0;

    for (String line : lines) {
      int start = 0;
      nbOccurence--;
      do {
        nbOccurence++;
        start = line.indexOf(s, start);
        if (start != -1) {
          start++;
        }
      } while (start != -1 && start < line.length() - 1);
    }

    return nbOccurence;
  }
}