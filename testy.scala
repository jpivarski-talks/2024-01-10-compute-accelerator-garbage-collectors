import java.net.Socket

val shuffle3 = Array[Int](0, 2, 3)
val shuffle7 = Array[Int](1, 2, 0, 6, 4, 7, 5)
val shuffle13 = Array[Int](1, 2, 9, 13, 10, 12, 0, 6, 5, 11, 4, 8, 14)
val shuffle31 = Array[Int](21, 1, 17, 30, 11, 19, 24, 8, 14, 3, 0, 16, 18, 20, 31, 27, 22, 9, 28, 10, 5, 13, 2, 26, 12, 6, 15, 29, 25, 7, 4)
val shuffle61 = Array[Int](47, 51, 60, 44, 7, 5, 17, 25, 14, 63, 62, 37, 21, 9, 4, 56, 15, 3, 26, 28, 41, 6, 31, 52, 2, 1, 11, 10, 23, 59, 13, 8, 42, 39, 55, 54, 0, 27, 58, 16, 20, 38, 35, 45, 61, 12, 57, 30, 53, 32, 34, 29, 46, 50, 49, 33, 40, 48, 19, 43, 22)

val client = new Socket("127.0.0.1", 8080)
val stream = client.getOutputStream

val array = Array.fill(4 * 8 * 16 * 32 * 64)(Option.empty[Array[Int]])
// val array = Array.fill(4 * 8 * 16 * 32 * 64)(0)

def run() {
  var count: Int = 0

  for (_ <- 1 to 20) {
    for (i61 <- shuffle61) {
      for (i31 <- shuffle31) {
        for (i13 <- shuffle13) {
          for (i7 <- shuffle7) {
            for (i3 <- shuffle3) {

              array(((((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3)) = Some(Array[Int]())
              // array(((((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3)) = 123

              if ((count & 0x7ff) == 0) {
                stream.write('.')
              }
              count += 1
            }
          }
        }
      }
    }
    for (i3 <- shuffle3) {
      for (i7 <- shuffle7) {
        for (i13 <- shuffle13) {
          for (i31 <- shuffle31) {
            for (i61 <- shuffle61) {

              array(((((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3)) = Some(Array[Int]())
              // array(((((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3)) = 123

              if ((count & 0x7ff) == 0) {
                stream.write('.')
              }
              count += 1
            }
          }
        }
      }
    }
  }
}

try {
  run()
}
finally {
  stream.write('X')
  client.close()
}
