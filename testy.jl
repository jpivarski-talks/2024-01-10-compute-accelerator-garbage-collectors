using Sockets

shuffle3::Vector{Int64} = [0, 2, 3]
shuffle7::Vector{Int64} = [1, 2, 0, 6, 4, 7, 5]
shuffle13::Vector{Int64} = [1, 2, 9, 13, 10, 12, 0, 6, 5, 11, 4, 8, 14]
shuffle31::Vector{Int64} = [21, 1, 17, 30, 11, 19, 24, 8, 14, 3, 0, 16, 18, 20, 31, 27, 22, 9, 28, 10, 5, 13, 2, 26, 12, 6, 15, 29, 25, 7, 4]
shuffle61::Vector{Int64} = [47, 51, 60, 44, 7, 5, 17, 25, 14, 63, 62, 37, 21, 9, 4, 56, 15, 3, 26, 28, 41, 6, 31, 52, 2, 1, 11, 10, 23, 59, 13, 8, 42, 39, 55, 54, 0, 27, 58, 16, 20, 38, 35, 45, 61, 12, 57, 30, 53, 32, 34, 29, 46, 50, 49, 33, 40, 48, 19, 43, 22]

client = connect("127.0.0.1", 8080)

array::Vector{Union{Vector{Int32}, Nothing}} = fill(nothing, 4 * 8 * 16 * 32 * 64)
# array::Vector{Int64} = fill(0, 4 * 8 * 16 * 32 * 64)

function run()
    count::Int64 = 0
    while true
        for i61 in shuffle61
            for i31 in shuffle31
                for i13 in shuffle13
                    for i7 in shuffle7
                        for i3 in shuffle3

                            array[(((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3 + 1] = []
                            # array[(((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3 + 1] = count

                            if count & 0x7ff == 0
                                write(client, [UInt8('.')])
                            end
                            count += 1
                        end
                    end
                end
            end
        end
        for i3 in shuffle3
            for i7 in shuffle7
                for i13 in shuffle13
                    for i31 in shuffle31
                        for i61 in shuffle61

                            array[(((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3 + 1] = []
                            # array[(((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3 + 1] = count

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

Base.exit_on_sigint(false)
try
    run()
finally
    write(client, [UInt8('X')])
end

close(client)
