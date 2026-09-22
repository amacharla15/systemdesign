package com.akshith.backend.controller;

import com.akshith.backend.model.User;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class UserController {

    private final Map<Integer, User> users = new HashMap<>();

    public UserController() {
        users.put(0, new User(0, "Akshay", 25));
        users.put(1, new User(1, "Rahul", 26));
        users.put(2, new User(2, "Bob", 25));
    }

    @GetMapping("/users/{id}")
    public User getUser(@PathVariable int id) {
        return users.get(id);
    }

    @GetMapping("/users")
    public List<User> getUsersByAge(@RequestParam int age) {

        List<User> result = new ArrayList<>();

        for (User user : users.values()) {
            if (user.getAge() == age) {
                result.add(user);
            }
        }

        return result;
    }
}