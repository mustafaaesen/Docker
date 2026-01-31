#Container silindiğinde bile verilerin nasıl kaybolmadığını anlamak için pratik yapıldı

#volume nne işe yarar volume olmadan ne olur volume ile ne değişir sorularının cevapları gözlemlendi

with open("data.txt", "a") as f:
    f.write("Docker volume test\n")

print("Dosyaya yazıldı")
