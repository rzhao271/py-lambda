Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

# target_cell_acc: cells: [int] -> target_ind: int -> ind_acc: int -> cells_acc: [int] -> target_val: int -> out new_cells: [int]
target_cell_acc = lambda f: lambda cai: lambda ti: lambda ia: lambda ca: lambda tv: ca + [tv] + cai[ti + 1:] if ia == ti else (f)(cai)(ti)(ia + 1)(ca + [cai[ia]])(tv)

assert (Z)(target_cell_acc)([0, 1, 2])(2)(0)([-5])(5) == [-5, 0, 1, 5]

# search_forward_acc: ins: str -> cells: [int] -> cell_ind: int -> ins_ind: int -> bracket_char: length-1-str -> anti_bracket_char: length-1-str -> brackets_acc: int -> out new_ins_ind: int
search_forward_acc = lambda f: lambda ins: lambda cai: lambda ci: lambda ini: lambda bc: lambda abc: lambda ba: ini + 1 if cai[ci] != 0 or ba == 1 and ins[ini] == abc else (f)(ins)(cai)(ci)(ini + 1)(bc)(abc)(ba + 1 if ins[ini] == bc else ba - 1 if ins[ini] == abc else ba)

# search_backward_acc: (see search_forward_acc for typesig)
search_backward_acc = lambda f: lambda ins: lambda cai: lambda ci: lambda ini: lambda bc: lambda abc: lambda ba: ini + 1 if cai[ci] == 0 or ba == 1 and ins[ini] == abc else (f)(ins)(cai)(ci)(ini - 1)(bc)(abc)(ba + 1 if ins[ini] == bc else ba - 1 if ins[ini] == abc else ba)

assert (Z)(search_forward_acc)('[[]]')([1, 0, 0])(0)(0)('[')(']')(0) == 1
assert (Z)(search_forward_acc)('[[]]')([1, 0, 0])(0)(2)('[')(']')(0) == 3
assert (Z)(search_forward_acc)('[[]]')([0, 0, 0])(0)(1)('[')(']')(0) == 3
assert (Z)(search_forward_acc)('[[]]')([0, 0, 0])(0)(0)('[')(']')(0) == 4

assert (Z)(search_backward_acc)('[[]]')([0, 0, 0])(0)(3)(']')('[')(0) == 4
assert (Z)(search_backward_acc)('[[]]')([0, 0, 0])(0)(1)(']')('[')(0) == 2
assert (Z)(search_backward_acc)('[[]]')([1, 0, 0])(0)(2)(']')('[')(0) == 2
assert (Z)(search_backward_acc)('[[]]')([1, 0, 0])(0)(3)(']')('[')(0) == 1

# parse: ins: str -> cells: [int] -> cell_ind: int -> ins_ind: int -> acc_out: string -> out acc_out
parse = lambda f: lambda ins: lambda cai: lambda ci: lambda ini: lambda acc_out: acc_out if ini == len(ins) else (f)(ins)((Z)(target_cell_acc)(cai)(ci)(0)([])(cai[ci] + 1))(ci)(ini + 1)(acc_out) if ins[ini] == '+' else (f)(ins)((Z)(target_cell_acc)(cai)(ci)(0)([])(cai[ci] - 1))(ci)(ini + 1)(acc_out) if ins[ini] == '-' else (f)(ins)(cai)(ci + 1)(ini + 1)(acc_out) if ins[ini] == '>' else (f)(ins)(cai)(ci - 1)(ini + 1)(acc_out) if ins[ini] == '<' else (f)(ins)(cai)(ci)((Z)(search_forward_acc)(ins)(cai)(ci)(ini)('[')(']')(0))(acc_out) if ins[ini] == '[' else (f)(ins)(cai)(ci)((Z)(search_backward_acc)(ins)(cai)(ci)(ini)(']')('[')(0))(acc_out) if ins[ini] == ']' else (f)(ins)(cai)(ci)(ini + 1)(acc_out + str(chr(cai[ci]))) if ins[ini] == '.' else (f)(ins)((Z)(target_cell_acc)(cai)(ci)(0)([])(ord(input()[0])))(ci)(ini + 1)(acc_out) if ins[ini] == ',' else (f)(ins)(cai)(ci)(ini + 1)(acc_out)

interactive = lambda f: lambda ins: lambda cai: lambda ci: lambda ini: lambda acc_out: acc_out if ini == len(ins) else (f)(ins)((Z)(target_cell_acc)(cai)(ci)(0)([])(cai[ci] + 1))(ci)(ini + 1)(acc_out) if ins[ini] == '+' else (f)(ins)((Z)(target_cell_acc)(cai)(ci)(0)([])(cai[ci] - 1))(ci)(ini + 1)(acc_out) if ins[ini] == '-' else (f)(ins)(cai)(ci + 1)(ini + 1)(acc_out) if ins[ini] == '>' else (f)(ins)(cai)(ci - 1)(ini + 1)(acc_out) if ins[ini] == '<' else (f)(ins)(cai)(ci)((Z)(search_forward_acc)(ins)(cai)(ci)(ini)('[')(']')(0))(acc_out) if ins[ini] == '[' else (f)(ins)(cai)(ci)((Z)(search_backward_acc)(ins)(cai)(ci)(ini)(']')('[')(0))(acc_out) if ins[ini] == ']' else [print(str(chr(cai[ci])), end=''), (f)(ins)(cai)(ci)(ini + 1)(acc_out + str(chr(cai[ci])))][1] if ins[ini] == '.' else (f)(ins)((Z)(target_cell_acc)(cai)(ci)(0)([])(ord(input()[0])))(ci)(ini + 1)(acc_out) if ins[ini] == ',' else (f)(ins)(cai)(ci)(ini + 1)(acc_out)

assert (Z)(parse)('')([])(0)(0)('') == ''

# From Wikipedia
assert (Z)(parse)('++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.')([0]*10)(0)(0)('') == 'Hello World!\n'
print((Z)(parse)('++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.')([0]*10)(0)(0)(''))
