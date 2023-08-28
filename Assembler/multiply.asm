@5
D = A
@1
M = D
@7
D = A
@2
M = D

@1
D = M-D
@Option1
D; JLT

(Option1)
    @1
    D = M
    @0
    M = D
    @2
    D = M
    @1
    M = D
    @0
    D = M
    @2
    M = D

(LOOP)
    @3
    D = M
    @2
    D = D + M
    @3
    M = D
    @1
    M = M - 1
    @1
    D = M
    @END 
    D; JEQ
    @LOOP
    0; JMP

(END)
    @3
    D=M
    @END
    0; JMP 