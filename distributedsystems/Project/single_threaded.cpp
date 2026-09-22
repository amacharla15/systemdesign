#include <iostream>
using namespace std;
#include <string>
#include <unordered_map>
#include <list>


struct Node{
    public:
        string key;
        int value;
    public:
        Node(string key, int value){
            this->key= key;
            this->value = value;
        }
};

class Cache{
    private:
        string key;
        unordered_map<string, list<Node> :: iterator> dict;
        list<Node> items;
    public:
        bool set(string key, int value){
            if(dict.find(key)!=dict.end()){
                dict[key]->value=value;
                items.splice(items.begin(), items, dict[key]);
                return True;
            }else{
                items.push_front(Node(key,value));
                dict[key]=items.begin();
                return True;
            }
        }
        string get(string key){

        }

        boot del(string key){

        }

        size_t size(){

        }




};