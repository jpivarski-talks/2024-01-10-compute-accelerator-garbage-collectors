import java.net.Socket

val shuffleA = Array[Int](7, 6, 4, 10, 0, 15, 9, 8, 13, 5, 12, 14, 3, 11, 2, 1)
val shuffleB = Array[Int](3, 8, 0, 15, 11, 2, 6, 7, 12, 9, 1, 14, 5, 13, 4, 10)
val shuffleC = Array[Int](2, 13, 6, 7, 4, 5, 10, 3, 12, 15, 8, 9, 14, 1, 0, 11)
val shuffleD = Array[Int](7, 5, 9, 15, 4, 2, 13, 12, 0, 8, 11, 6, 3, 1, 10, 14)
val shuffleE = Array[Int](14, 11, 10, 8, 0, 6, 5, 1, 13, 9, 7, 4, 2, 12, 3, 15)

val client = new Socket("127.0.0.1", 8080)
val stream = client.getOutputStream

val array = Array.fill(Math.pow(16, 5).toInt)(Option.empty[Array[Int]])
// val array = Array.fill(Math.pow(16, 5).toInt)(0)

def run() {
  var count: Int = 0

  for (_ <- 1 to 20) {
    for (iA <- shuffleA) {
      for (iB <- shuffleB) {
        for (iC <- shuffleC) {
          for (iD <- shuffleD) {
            for (iE <- shuffleE) {

              array(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)) = Some(Array[Int]())
              // array(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)) = 123

              if ((count & 0x7ff) == 0) {
                stream.write('.')
              }
              count += 1
            }
          }
        }
      }
    }
    for (iE <- shuffleE) {
      for (iD <- shuffleD) {
        for (iC <- shuffleC) {
          for (iB <- shuffleB) {
            for (iA <- shuffleA) {

              array(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)) = Some(Array[Int]())
              // array(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)) = 123

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
