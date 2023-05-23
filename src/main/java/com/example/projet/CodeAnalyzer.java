package com.example.projet;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class CodeAnalyzer {
  private Scanner scanner;
  private File pythonFile;
  private LinkedList<String> lines;
  
  private int functionNumber;
  private LinkedList<Integer> nbLineFunction;
  private String fileContent;
  
  // Constructor if argument is a file
  public CodeAnalyzer(File inputFile) throws FileNotFoundException { 
    pythonFile = inputFile;
    scanner = new Scanner(pythonFile);
    lines = new LinkedList<>();
    nbLineFunction = new LinkedList<>();

    readFile();
    calculateFunctionLine();
    calculateFunctionNb();
  }

  // Constructor if argument is a String
  public CodeAnalyzer(String fileContent) { 
    this.fileContent = fileContent;
    lines = new LinkedList<>();
    nbLineFunction = new LinkedList<>();

    readString();
    calculateFunctionLine();
    calculateFunctionNb();
  }

  // Adds each useful line (not empty or only spaces) to the linkedList of lines (File case)
  private void readFile() { 
    String nextLine;
    while (scanner.hasNextLine()) {
      nextLine = scanner.nextLine();
      if (valid(nextLine)) {
        lines.add(nextLine);
      }
    }
  }

  // Adds each useful line (not empty or only spaces) to the linkedList of lines (String case)
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

  // Returns false if the line is only spaces or empty, true otherwise
  private boolean valid(String line) { 
    return !removeSpaces(line).equals("");
  }

  // Returns the number of useful lines in the file
  public int getNbLines() { 
    int nbLines;
    nbLines = lines.size();
    return nbLines;
  }

  // Removes the spaces before the first non-space character and return the resulted String
  private String removeSpaces(String s) {     int start = 0;
    if (s.length() == 0) {
      return s;
    }
    while (start < s.length() && s.charAt(start) == ' ') {
      start++;
    }
    return s.substring(start);
  }

  // Returns the number of spaces before the first non-space character, to keep track of the indentation in the python code
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

  // Calculates the number of lines in each function and store the results in the linkedList nbLineFunction
  // Uses Stack (Deque) because declaring a function in a function is allowed in python
  private void calculateFunctionLine() {
    nbLineFunction.clear();
    
    Deque<Integer> stack = new ArrayDeque<>();
    Deque<Integer> indents = new ArrayDeque<>();
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

  // Gets the minimum amongst the functions line numbers
  public int getFunctionMin() {
    int min = 0;
    for (int nbLine : nbLineFunction) {
      if (nbLine < min || min == 0) {
        min = nbLine;
      }
    }
    return min;
  }

  // Gets the maximum amongst the functions line numbers
  public int getFunctionMax() {
    int max = 0;
    for (int nbLine : nbLineFunction) {
      if (nbLine > max) {
        max = nbLine;
      }
    }
    return max;
  }

  // Calculates the average of the functions line numbers
  public float getFunctionAvg() {
    int total = 0;
    for (int nbLine : nbLineFunction) {
      total += nbLine;
    }
    return (float)total / functionNumber;
  }

  // Calculates the number of functions in the file and stores the result
  private void calculateFunctionNb() {
    functionNumber = 0;
    for (String line : lines) {
      if (removeSpaces(line).startsWith("def ")) {
        functionNumber++;
      }
    }
  }

  // Returns the number of functions in the file
  public int getFunctionNb() {
    return functionNumber;
  }

  // Returns the number of occurences of the argument in the file
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

  public List<Integer> getNbLineFunction() {
      return nbLineFunction;
  }
}