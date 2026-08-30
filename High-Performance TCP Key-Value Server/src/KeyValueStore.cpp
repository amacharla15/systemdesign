#include "KeyValueStore.hpp"

void KeyValueStore::set(string key, string value) {
    map[key] = value;
}

string KeyValueStore::get(string key) {
    if (map.find(key) != map.end()) {
        return map[key];
    }

    return "";
}

bool KeyValueStore::remove(string key) {
    if (map.find(key) != map.end()) {
        map.erase(key);
        return true;
    }

    return false;
}

bool KeyValueStore::exists(string key) {
    if (map.find(key) != map.end()) {
        return true;
    }

    return false;
}

string KeyValueStore::commandparser(string command){
    int n=command.length();
    vector<string> temp;
    string d="";
    int i=0;
    while(i<n){
        while(i<n&&command[i]==' '){
            i++;
        }
        while(i<n&&command[i]!=' '){
            d=d+command[i];
            i++;
        }
        if(!d.empty()){
            temp.push_back(d);
            d="";
        }
    }
    int veclength=temp.size();
    if(veclength==0){
        return "ERROR";
    }
    if(temp[0]=="SET"){
        if(veclength!=3){
            return "ERROR";
        }
        set(temp[1],temp[2]);
        return "OK";
    }
    else if(temp[0]=="GET"){
        if(veclength!=2){
            return "ERROR";
        }
        auto result=get(temp[1]);
        if(result.has_value()){
            return result.value();
        }
        return "NOT_FOUND";
    }
    else if(temp[0]=="DELETE"){
        if(veclength!=2){
            return "ERROR";
        }
        if(remove(temp[1])){
            return "OK";
        }
        return "NOT_FOUND";
    }
    else if(temp[0]=="EXISTS"){
        if(veclength!=2){
            return "ERROR";
        }
        if(exists(temp[1])){
            return "1";
        }
        return "0";
    }
    return "ERROR";
}