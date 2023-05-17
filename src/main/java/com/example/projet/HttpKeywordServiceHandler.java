package com.example.projet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

import org.json.JSONObject;

import com.sun.net.httpserver.HttpExchange;

public class HttpKeywordServiceHandler extends AHandler {

    /**
     * Handles a post request and gets the first file which is in it
     * For example to trigger this correctly, you can use:
     * 
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
    private String handlePostRequest(HttpExchange httpExchange) {
        return new BufferedReader(new InputStreamReader(httpExchange.getRequestBody(), StandardCharsets.UTF_8)).lines()
                .collect(Collectors.joining("\n"));
    }

    private List<String> getKeywords(String input) {
        var start = input.indexOf("keywords");
        if (start >= 0){
            var end = input.indexOf("\n------", start);
            var kw = input.substring(start + 11, end);
            var kws = kw.split("\s");
            return Arrays.asList(kws);

        }
        return new LinkedList<>();
    }

    private JSONObject createJson(String content, List<String> keywords) {
        var json = new JSONObject();

        var analyzer = new CodeAnalyzer(content);


        keywords.forEach(k -> {
            json.put(k, analyzer.getNbOccurence(k));
        });

        return json;
    }

    @Override
    public void handle(HttpExchange httpExchange) throws IOException {
        Serveur.LOGGER.info(" Je réponds lines");
        String requestParamValue = null;
        if ("POST".equals(httpExchange.getRequestMethod())) {
            requestParamValue = handlePostRequest(httpExchange);
            Serveur.LOGGER.info(requestParamValue);
            handleResponse(httpExchange, requestParamValue, createJson(getFileContent(requestParamValue), getKeywords(requestParamValue)));
        } else {
            // TODO handle non supported http
        }
    }

}
