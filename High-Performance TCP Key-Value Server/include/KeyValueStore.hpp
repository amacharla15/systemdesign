#pragma once

#include <string>
#include <unordered_map>

using namespace std;

class KeyValueStore {
private:
    unordered_map<string, string> map;

public:
    void set(string key, string value);
    string get(string key);
    bool remove(string key);
    bool exists(string key);
    void commandparser(string command);
};