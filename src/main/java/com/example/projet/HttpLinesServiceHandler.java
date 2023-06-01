package com.example.projet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

import org.json.JSONArray;
import org.json.JSONObject;

import com.sun.net.httpserver.HttpExchange;

class HttpLinesServiceHandler extends AHandler {
    /**
     * Handles a post request and gets the first file which is in it
     * For example to trigger this correctly, you can use:
     * <pre>
     * let input = document.querySelector("input[type=file]");
     * let data = new FormData();
     * data.append("file", inp.files[0]);
     * data.append("user", username);
     * fetch("http://localhost:8001/lines", {method: 'POST', body: data})
     * </pre>
     * 
     * 
     * @param httpExchange the content of the request
     * @return a string containing the body of the file
     */
    private String handlePostRequest(HttpExchange httpExchange){
        var body = new BufferedReader(new InputStreamReader(httpExchange.getRequestBody(), StandardCharsets.UTF_8)).lines().collect(Collectors.joining("\n"));
        return getFileContent(body);
    }

    private JSONObject createJson(String content){
        var json = new JSONObject();

        var analyzer = new CodeAnalyzer(content);

        var functionData = new JSONObject();
        functionData.put("count", analyzer.getFunctionNb());
        functionData.put("minLines", analyzer.getFunctionMin());
        functionData.put("maxLines", analyzer.getFunctionMax());
        functionData.put("avgLines", analyzer.getFunctionAvg());
        var linesFunctions = new JSONArray();
        analyzer.getNbLineFunction().forEach(linesFunctions::put);
        functionData.put("linesPerFunction", linesFunctions);
        json.put("functionData", functionData);
        json.put("lines", analyzer.getNbLines());

        return json;
    }

    // Interface method to be implemented
    @Override
    public void handle(HttpExchange httpExchange) throws IOException {
        Serveur.LOGGER.info(" Je réponds lines");
        String requestParamValue=null;
        if("POST".equals(httpExchange.getRequestMethod())) {
            requestParamValue = handlePostRequest(httpExchange);
            Serveur.LOGGER.info(requestParamValue);
            handleResponse(httpExchange, createJson(requestParamValue));
        }
        else{
            // TODO handle non supported http
        }

    }
}