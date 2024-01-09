#include <chrono>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

using namespace std::chrono;

int main() {
  int server_fd;
  int new_socket;
  struct sockaddr_in address;
  int addrlen = sizeof(address);
  char buffer = 0;

  if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
    return 1;
  }

  int opt = 1;
  if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
    return 2;
  }
  address.sin_family = AF_INET;
  address.sin_addr.s_addr = INADDR_ANY;
  address.sin_port = htons(8087);

  if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
    return 3;
  }
  if (listen(server_fd, 3) < 0) {
    return 4;
  }
  if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
    return 5;
  }

  steady_clock::time_point bigstart;
  steady_clock::time_point start = steady_clock::now();
  steady_clock::time_point stop = steady_clock::now();
  int phase = 0;
  // int allocations = 0;
  // int reallocations = 0;

  do {
    int num_bytes = recv(new_socket, &buffer, 1, 0);
    if (num_bytes < 0) {
      return 6;
    }

    if (phase == 0) {
      bigstart = steady_clock::now();
      phase = 1;
    }

    stop = steady_clock::now();

    if (phase == 1  &&  duration_cast<microseconds>(stop - bigstart).count() >= 5000000) {
      phase = 2;
      bigstart = steady_clock::now();
    }
    else if (phase == 2) {
      printf("%ld\n", duration_cast<microseconds>(stop - start).count());
      // if (buffer == '1') {
      //   allocations++;
      // }
      // else if (buffer == '2') {
      //   reallocations++;
      // }
    }

    start = stop;
  }
  while (phase < 2  ||  duration_cast<microseconds>(stop - bigstart).count() < 60000000);

  close(new_socket);
  close(server_fd);

  // printf("allocations %d reallocations %d\n", allocations, reallocations);

  return 0;
}
