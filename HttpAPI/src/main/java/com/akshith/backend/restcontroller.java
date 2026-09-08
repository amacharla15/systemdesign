package com.akshith.backend;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class HomeController {

    @GetMapping("/message")
    public Map<String, String> getMessage() {
        return Map.of("message", "Backend server is running");
    }

    @GetMapping("/users/{id}")
    public String getUser(@PathVariable int id) {

        Map<Integer, String> users = new HashMap<>();

        users.put(0, "Akshay");
        users.put(1, "Rahul");
        users.put(2, "Bob");

        return users.get(id);
    }
}