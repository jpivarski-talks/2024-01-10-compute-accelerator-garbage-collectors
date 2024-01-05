#include <chrono>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
  int server_fd;
  int new_socket;
  struct sockaddr_in address;
  int addrlen = sizeof(address);
  char buffer[1] = {0};

  if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
    return 1;
  }

  int opt = 1;
  if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
    return 2;
  }
  address.sin_family = AF_INET;
  address.sin_addr.s_addr = INADDR_ANY;
  address.sin_port = htons(8080);

  if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
    return 3;
  }
  if (listen(server_fd, 3) < 0) {
    return 4;
  }
  if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
    return 5;
  }

  std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();
  std::chrono::steady_clock::time_point stop = std::chrono::steady_clock::now();

  do {
    int num_bytes = recv(new_socket, buffer, 1, 0);
    if (num_bytes < 0) {
      return 6;
    }

    stop = std::chrono::steady_clock::now();
    printf("%d\n", std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count());
    start = stop;
  }
  while (buffer[0] == '.');

  close(new_socket);
  close(server_fd);

  return 0;
}
