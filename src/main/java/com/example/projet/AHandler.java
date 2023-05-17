package com.example.projet;

import java.io.IOException;
import java.io.OutputStream;

import org.json.JSONObject;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

public abstract class AHandler implements HttpHandler {
    /**
     * Generate simple response html page
     * 
     * @param httpExchange
     * @param requestParamVaue
     */
    protected void handleResponse(HttpExchange httpExchange, String requestParamValue, JSONObject returnJsonObject)
            throws IOException {
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
        String htmlResponse = returnJsonObject.toString();
        // this line is a must
        httpExchange.sendResponseHeaders(200, htmlResponse.length());
        outputStream.write(htmlResponse.getBytes());
        outputStream.flush();
        outputStream.close();
    }

    /**
     * Gets the body of a file from a raw formdata
     * 
     * @param formData
     * @return
     */
    protected String getFileContent(String formData) {
        Serveur.LOGGER.info(formData);
        var start = formData.indexOf("; filename=");
        if (start >= 0) {
            var nameEnd = formData.indexOf("\n", start);
            var filename = formData.substring(start + 11, nameEnd);
            Serveur.LOGGER.info(filename);

            var fileContentStart = formData.indexOf("\n\n", nameEnd);
            var fileContentEnd = formData.indexOf("------", fileContentStart);
            var fileContent = formData.substring(fileContentStart, fileContentEnd);
            Serveur.LOGGER.info(fileContent);
            return fileContent;
        }
        return "";

    }
}
