# Erkekler için bazal metabolizma hızı = 66.5 + (13.75 x vücut ağırlığınız (kg)) + (5 x boyunuz (cm.)) - (6.77 x yaş)
# Kadınlar için bazal metabolizma hızı = 655.1 + (9.56 x vücut ağırlığınız (kg)) + (1.85 x boyunuz (cm.)) - (4.67 x yaş)
print("\nKalori hesaplama programına hoşgeldiniz!\n")

cinsiyet = input("Cinsiyetinizi yazın: ").lower()
kilo = float(input("Kilonuzu yazın: "))
boy = float(input("Boyunuzu cm cinsinden yazın: "))
yaş = float(input("Yaşınızı girin: "))

if(cinsiyet == "erkek"):{
    print("vücudunuzun bazal metobolizma hızı: " + str(66.5 + (13.75 * kilo) + (5 * boy) - (6.77 * yaş)) + " kcal")
}
    
elif(cinsiyet == "kadın"):{
    print("vücudunuzun bazal metobolizma hızı: " + str(655.1 + (9.56 * kilo) + (1.85 * boy) - (4.67 * yaş)) + " kcal")
}
    
else:{
    print("Lütfen cinsiyetinizi hepsi küçük harf ile ve doğru yazdığınızdan emin olun...")
}
