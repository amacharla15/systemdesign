#include <iostream>
#include <unordered_map>
using namespace std;

struct Node{
    int key;
    int val;
    Node *next;
    Node *prev;
    Node(int k, int v) {
        key = k;
        val = v;
        next = nullptr;
        prev = nullptr;
    }
};

class LRUcache{
    private:
    int capacity;
    unordered_map<int, Node*> dict;
    Node *start;
    Node *end;
    public:
    LRUcache(int capacity){
        this->capacity = capacity;
        start=nullptr;
        end=nullptr;
    }
    int get(int key){
        if(dict.find(key)!=dict.end()){
            return dict[key]->val;
        }
        return -1;
    }
    void put(int key, int value){
        if(dict.find(key)==dict.end()){
            if(dict.size()>=this->capacity){
                evict();
            }
            Node *newNode= new Node(key,value);
            if (this->end==nullptr){
                this->end=newNode;
            }
            if (this->start==nullptr){
               this->start=newNode;
            }else{
                newNode->next=start;
                this->start->prev=newNode;
                this->start=newNode;
            }
            dict[key] = newNode;
        }
        else{
            Node* temp=dict[key];
            temp->val=value;
            temp->prev->next=temp->next;
            temp.next=start;
            this->start=temp;
        }
    }
    void evict(){
        int temp=this->end->key;
        dict.erase(temp);
        this->end=end->prev;
    }
};