package com.example.projet;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.Executors;
import java.util.logging.Logger;

public class Serveur {
    // logger pour trace
    static final Logger LOGGER = Logger.getLogger( Serveur.class.getName() );
    private static final String SERVEUR_NAME = "localhost"; // url de base du service
    private static final int PORT = 8001; // port serveur
    private static final String URL_LINES = "/lines"; // url d'acces au service de comptage de lignes et de fonctions
    private static final String URL_KW = "/keywords"; // url d'acces au service de comptage de nombred'occurences d'un mot clé
    // boucle principale qui lance le serveur sur le port 8001, à l'url test
    public static void main(String[] args) {
        HttpServer server = null;
        try {
            server = HttpServer.create(new InetSocketAddress(SERVEUR_NAME, PORT), 0);

            server.createContext(URL_LINES, new  HttpLinesServiceHandler());
            server.createContext(URL_KW, new  HttpKeywordServiceHandler());
            ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor) Executors.newFixedThreadPool(10);
            server.setExecutor(threadPoolExecutor);
            server.start();
            LOGGER.info(" Server started on port " + PORT);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}