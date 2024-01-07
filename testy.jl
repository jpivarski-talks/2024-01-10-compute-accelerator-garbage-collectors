using Sockets

shuffleA::Vector{Int64} = [7, 6, 4, 10, 0, 15, 9, 8, 13, 5, 12, 14, 3, 11, 2, 1]
shuffleB::Vector{Int64} = [3, 8, 0, 15, 11, 2, 6, 7, 12, 9, 1, 14, 5, 13, 4, 10]
shuffleC::Vector{Int64} = [2, 13, 6, 7, 4, 5, 10, 3, 12, 15, 8, 9, 14, 1, 0, 11]
shuffleD::Vector{Int64} = [7, 5, 9, 15, 4, 2, 13, 12, 0, 8, 11, 6, 3, 1, 10, 14]
shuffleE::Vector{Int64} = [14, 11, 10, 8, 0, 6, 5, 1, 13, 9, 7, 4, 2, 12, 3, 15]
shuffleF::Vector{Int64} = [10, 5, 4, 6, 15, 1, 9, 13, 7, 2, 11, 12, 0, 8, 3, 14]
shuffleG::Vector{Int64} = [5, 12, 6, 14, 4, 13, 3, 0, 7, 9, 15, 2, 11, 8, 1, 10]

client = connect("127.0.0.1", 8080)

array::Vector{Union{Vector{Int32}, Nothing}} = fill(nothing, 16^7)
# array::Vector{Int64} = fill(0, 4 * 8 * 16 * 32 * 64)

# GC.gc()
# GC.enable(false)

function run()
    count::Int64 = 0

    for iA in shuffleA
        for iB in shuffleB
            for iC in shuffleC
                for iD in shuffleD
                    for iE in shuffleE
                        for iF in shuffleF
                            for iG in shuffleG

                                array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG + 1] = []
                                # array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG + 1] = count

                                if count & 0x7ff == 0
                                    write(client, [UInt8('.')])
                                end
                                count += 1
                            end
                        end
                    end
                end
            end
        end
    end

    for iA in shuffleA
        for iB in shuffleB
            for iC in shuffleC
                for iD in shuffleD
                    for iE in shuffleE
                        for iF in shuffleF
                            for iG in shuffleG

                                array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG + 1] = []
                                # array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG + 1] = count

                                if count & 0x7ff == 0
                                    write(client, [UInt8('.')])
                                end
                                count += 1
                            end
                        end
                    end
                end
            end
        end
    end

end

run()
