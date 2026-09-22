#include <iostream>
#include <cstdio>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

using namespace std;

int main(){
    // 1. Create TCP/IPv4 socket
    int server_fd=socket(AF_INET,SOCK_STREAM,0);
    if(server_fd==-1){
        perror("socket");
        return 1;
    }
    cout<<"Socket created. fd="<<server_fd<<endl;

    // 2. Configure socket
    int opt=1;
    if(setsockopt(server_fd,SOL_SOCKET,SO_REUSEADDR,&opt,sizeof(opt))==-1){
        perror("setsockopt");
        close(server_fd);
        return 1;
    }

    // 3. Describe local IPv4 address and port
    sockaddr_in address{};
    address.sin_family=AF_INET;
    address.sin_addr.s_addr=INADDR_ANY;
    address.sin_port=htons(8080);

    // 4. Bind socket to 0.0.0.0:8080
    if(bind(server_fd,reinterpret_cast<sockaddr*>(&address),sizeof(address))==-1){
        perror("bind");
        close(server_fd);
        return 1;
    }

    // 5. Start listening for incoming connections
    if(listen(server_fd,5)==-1){
        perror("listen");
        close(server_fd);
        return 1;
    }
    cout<<"Listening on port 8080..."<<endl;

    // 6. Keep accepting clients
    while(true){
        sockaddr_in client_address{};
        socklen_t client_length=sizeof(client_address);

        int client_fd=accept(server_fd,reinterpret_cast<sockaddr*>(&client_address),&client_length);
        if(client_fd==-1){
            perror("accept");
            continue;
        }
        cout<<"Client connected. fd="<<client_fd<<endl;

        char buffer[1024];

        // 7. Keep receiving data from the same client
        while(true){
            ssize_t bytes_received=recv(client_fd,buffer,sizeof(buffer),0);
            if(bytes_received==-1){
                perror("recv");
                break;
            }
            if(bytes_received==0){
                cout<<"Client disconnected"<<endl;
                break;
            }

            // 8. Send all received bytes back
            ssize_t total_sent=0;
            while(total_sent<bytes_received){
                ssize_t bytes_sent=send(client_fd,buffer+total_sent,bytes_received-total_sent,0);
                if(bytes_sent==-1){
                    perror("send");
                    break;
                }
                total_sent+=bytes_sent;
            }
        }

        // 9. Close this client's connection
        close(client_fd);
    }

    // Normally unreachable in this version
    close(server_fd);
    return 0;
}