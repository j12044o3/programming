def comp(seq):                                          #상보적 변환 함수
    comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}    #DNA 영기서열 문자와 삼보적 변환 문자
    seq_comp = ""
    for char in seq:
        if char in comp_dict:
            seq_comp = seq_comp + comp_dict[char]
        else:
            seq_comp += '?'
    return seq_comp

def rev(seq):
    seq_dna = "ATGC"
    seq_rev = ""
    for char in seq:
        if char in seq_dna:
            seq_rev += char
        else:
            seq_rev += '?'
    seq_rev = "".join(reversed(seq_rev))
    return seq_rev

def rev_comp(seq):
    tmp = comp(seq)
    return rev(tmp)

src =input("DNA sequence : ")
cnvt =int(input("1(comp), 2(rev), 3(rev_comp) : "))
if(cnvt >=1 and cnvt <=3):
    if(cnvt == 1):
        rst = comp(src)
    elif(cnvt == 2):
        rst = rev(src)
    else:
        rst = rev_comp(src)
    print(src, "->", rst)
else:
    print("1(comp), 2(rev), 3(rev_comp)!!")
        
