package com.akshith.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class HomeController {

    @GetMapping("/message")
    public Map<String, String> getMessage() {
        return Map.of(
                "message",
                "Backend server is running"
        );
    }
}