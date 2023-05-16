package com.example.projet;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.Executors;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class Serveur {
    // logger pour trace
    private static final Logger LOGGER = Logger.getLogger( Serveur.class.getName() );
    private static final String SERVEUR = "localhost"; // url de base du service
    private static final int PORT = 8001; // port serveur
    private static final String URL = "/test"; // url de base du service
    // boucle principale qui lance le serveur sur le port 8001, à l'url test
    public static void main(String[] args) {
        HttpServer server = null;
        try {
            server = HttpServer.create(new InetSocketAddress(SERVEUR, PORT), 0);

            server.createContext(URL, new  MyHttpHandler());
            ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor) Executors.newFixedThreadPool(10);
            server.setExecutor(threadPoolExecutor);
            server.start();
            LOGGER.info(" Server started on port " + PORT);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class MyHttpHandler implements HttpHandler {
        /**
         * Manage GET request param
         * @param httpExchange
         * @return first value
         */
        private String handleGetRequest(HttpExchange httpExchange) {
            return httpExchange.getRequestURI()
                    .toString()
                    .split("\\?")[1]
                    .split("=")[1];
        }

        /** 
         * Generate simple response html page
         * @param httpExchange
         * @param requestParamVaue
         */
        private void handleResponse(HttpExchange httpExchange, String requestParamValue)  throws  IOException {
            OutputStream outputStream = httpExchange.getResponseBody();
            StringBuilder htmlBuilder = new StringBuilder();
            htmlBuilder.append("<html>")
                    .append("<body>")
                    .append("<h1>")
                    .append("Hello ")
                    .append(requestParamValue)
                    .append("</h1>")
                    .append("</body>")
                    .append("</html>");
            // encode HTML content
            String htmlResponse = htmlBuilder.toString();
            // this line is a must
            httpExchange.sendResponseHeaders(200, htmlResponse.length());
            outputStream.write(htmlResponse.getBytes());
            outputStream.flush();
            outputStream.close();
        }

        private String getFileContent(String formData){
            var start = formData.indexOf("; filename=");
            if (start >= 0){
                var nameEnd = formData.indexOf("\n", start);
                var filename = formData.substring(start + 11, nameEnd);
                LOGGER.info(filename);

                var fileContentStart = formData.indexOf("\n", nameEnd);
                var fileContentEnd = formData.indexOf("------WebKitFormBoundary", fileContentStart);
                var fileContent = formData.substring(fileContentStart, fileContentEnd);
                LOGGER.info(fileContent);
                return fileContent;
            }
            return "";

        }

        private String handlePostRequest(HttpExchange httpExchange){
            var body = new BufferedReader(new InputStreamReader(httpExchange.getRequestBody(), StandardCharsets.UTF_8)).lines().collect(Collectors.joining("\n"));
            


            return getFileContent(body);
        }

        // Interface method to be implemented
        @Override
        public void handle(HttpExchange httpExchange) throws IOException {
            LOGGER.info(" Je réponds");
            String requestParamValue=null;
            if("GET".equals(httpExchange.getRequestMethod())) {
                requestParamValue = handleGetRequest(httpExchange);
            }
            else if("POST".equals(httpExchange.getRequestMethod())) {
                requestParamValue = handlePostRequest(httpExchange);
            }
            LOGGER.info(requestParamValue);
            handleResponse(httpExchange,requestParamValue);

        }
    }
}