# Q10
wc -l nlp100/popular-names.txt

# Q11
sed -e 's/\t/ /g' nlp100/popular-names.txt | head -n 5

# Q12
cut -f 1 nlp100/popular-names.txt > nlp100/col1.txt
cut -f 2 nlp100/popular-names.txt > nlp100/col2.txt

# Q13
paste nlp100/col1.txt nlp100/col2.txt | head -n 5

# Q14
head -n 10 nlp100/popular-names.txt

# Q15
tail -n 10 nlp100/popular-names.txt

# Q16
split -l 200 -d nlp100/popular-names.txt sp

# Q17
cut -f 1 nlp100/popular-names.txt | sort | uniq | wc -l

# Q18
cat nlp100/popular-names.txt | sort -rnk 3 | head -n 20

# Q19
cut -f 1 nlp100/popular-names.txt | sort | uniq -c | sort -rn | head -n 10 