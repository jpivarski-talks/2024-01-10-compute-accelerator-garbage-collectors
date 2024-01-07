import java.net.Socket

val shuffleA = Array[Int](7, 6, 4, 10, 0, 15, 9, 8, 13, 5, 12, 14, 3, 11, 2, 1)
val shuffleB = Array[Int](3, 8, 0, 15, 11, 2, 6, 7, 12, 9, 1, 14, 5, 13, 4, 10)
val shuffleC = Array[Int](2, 13, 6, 7, 4, 5, 10, 3, 12, 15, 8, 9, 14, 1, 0, 11)
val shuffleD = Array[Int](7, 5, 9, 15, 4, 2, 13, 12, 0, 8, 11, 6, 3, 1, 10, 14)
val shuffleE = Array[Int](14, 11, 10, 8, 0, 6, 5, 1, 13, 9, 7, 4, 2, 12, 3, 15)
val shuffleF = Array[Int](10, 5, 4, 6, 15, 1, 9, 13, 7, 2, 11, 12, 0, 8, 3, 14)
val shuffleG = Array[Int](5, 12, 6, 14, 4, 13, 3, 0, 7, 9, 15, 2, 11, 8, 1, 10)

val client = new Socket("127.0.0.1", 8087)
val stream = client.getOutputStream

// val array = Array.fill(Math.pow(16, 7).toInt)(0)
val array = Array.fill(Math.pow(16, 7).toInt)(Option.empty[Array[Int]])

def run() {
  var count: Int = 0

  for (iA <- shuffleA) {
    for (iB <- shuffleB) {
      for (iC <- shuffleC) {
        for (iD <- shuffleD) {
          for (iE <- shuffleE) {
            for (iF <- shuffleF) {
              for (iG <- shuffleG) {

                // array((((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG) = count
                array((((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG) = Some(Array[Int]())

                if ((count & 0x7ff) == 0) {
                  stream.write('1')
                }
                count += 1
              }
            }
          }
        }

        for (iD <- shuffleD) {
          for (iE <- shuffleE) {
            for (iF <- shuffleF) {
              for (iG <- shuffleG) {

                // array((((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG) = count
                array((((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG) = Some(Array[Int]())

                if ((count & 0x7ff) == 0) {
                  stream.write('2')
                }
                count += 1
              }
            }
          }
        }
      }
    }
  }

}

run()
