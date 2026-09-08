#include <iostream>
#include "KeyValueStore.hpp"

using namespace std;

int main() {
    KeyValueStore store;

    store.set("name", "Akshith");
    store.set("language", "C++");

    cout << store.get("name") << endl;
    cout << store.get("language") << endl;

    cout << store.exists("name") << endl;

    store.remove("name");

    cout << store.exists("name") << endl;

    return 0;
}