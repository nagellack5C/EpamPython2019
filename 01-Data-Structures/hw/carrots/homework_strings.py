""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta
with open("files/dna.fasta") as dna_file:
    dna_lines = [line.replace("\n", "") for line in dna_file.readlines()]
    # making a dict of genes with a list of gene names
    # will keep the input order when outputting
    dna = {}
    genes = []
    for line in dna_lines:
        if ">" in line:
            key = line
            genes.append(key)
            dna[line] = ""
        else:
            dna[key] += line #assuming that every file is formatted like this

with open("files/rna_codon_table.txt") as codon_table_file:
    codon_table = {}
    for line in codon_table_file.readlines():
        #doing some weird things to parse the codons table
        line = line.replace("\n", "").replace(" "*6, " "*3).split(" "*3)
        for codon_trans in line:
            seq, codon = codon_trans.strip().split(" ")
            codon_table[seq] = codon


def translate_from_dna_to_rna(dna):
    
    return dna.replace("T", "U")


def count_nucleotides(dna):

    num_of_nucleotides = f'G - {dna.count("G")}, ' \
                         f'A - {dna.count("A")}, ' \
                         f'T - {dna.count("T")}, ' \
                         f'C - {dna.count("C")}'
    
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    
    index = 3
    protein = []
    while index <= len(rna):
        # pass over the rna
        # will skip trailing symbols if they do not form a triplet
        protein.append(codon_table[rna[index-3:index]])
        index += 3
    
    return protein


with open("nucl_stats.txt", "w") as nucl_stats,\
        open("rnas.txt", "w") as rnas,\
        open("proteins.txt", "w") as proteins:
    for gene in genes:
        nucl_stats.write(gene + "\n")
        nucl_stats.write(count_nucleotides(dna[gene]) + "\n")

        rnas.write(gene + "\n")
        rna = translate_from_dna_to_rna(dna[gene])
        rna_prettified = [rna[i:i + 75] for i in range(0, len(rna), 75)]
        for line in rna_prettified:
            rnas.write(line + "\n")

        proteins.write(gene + "\n")
        prot = translate_rna_to_protein(rna)
        prot_prettified = [prot[i:i + 40] for i in range(0, len(prot), 40)]
        for line in prot_prettified:
            proteins.write(" ".join(line) + "\n")
