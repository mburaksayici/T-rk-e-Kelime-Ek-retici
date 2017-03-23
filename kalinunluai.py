import Ekler
from Ekler import sozcuk

print(sozcuk ,"Eklerde kalın ünlü harfler kullanılacak.")

def lıkkalınaı(sozcuk):
    print("-lık ekleniyor.")
    sozcuklık = sozcuk +'lık'
    print(sozcuklık)
    print("-lar ekleniyor.")
    sozcuklıklar = sozcuklık + 'lar'
    print(sozcuklıklar)
    def dorthal(sozcuklık):
        
        
        print("-ı, -a, -dan, -ta ekleniyor.")
        sozcuklıkdan = sozcuklık + 'tan'
        
        print(sozcuklıkdan)
        
        print("Ünsüz yumuşaması kontrol ediliyor")
        
        
        if ((str(sozcuklık[len(sozcuklık)-1])   == 'k')): # Yumuşama
            sozcuklıkğ = sozcuklık[:(len(sozcuklık)-1)] + "ğ"
            print("Sondaki k, ğ ile değiştirildi")
            
        
            sozcuklıkğa = sozcuklıkğ + 'a'
            sozcuklıkğı = sozcuklıkğ + 'ı'
            print(sozcuklıkğa)
            print(sozcuklıkğı)
        print("-da, -daki, -dakinden, -dakinde, -dakilerce ekleniyor.")     
        sozcuklıkta = sozcuklık + 'ta'
        sozcuklıktaki = sozcuklıkta + 'ki'
        sozcuklıktakiler = sozcuklıktaki + 'ler'
        sozcuklıktakinden = sozcuklıktaki + 'nden'
        sozcuklıktakinde = sozcuklıktaki + 'nde'
        sozcuklıktakilerce = sozcuklıktakiler + 'ce'
        print(sozcuklıkta)
        print(sozcuklıktaki)
        print(sozcuklıktakiler)
        print(sozcuklıktakinden)
        print(sozcuklıktakinde)
        print(sozcuklıktakilerce)
    dorthal(sozcuklık)
    def iyelik(sozcuklık):
        print("İyelik Ekleri ekleniyor.")
        print("-ı eki yukarıda iyelik olarak kullanılmıştı.")
        print("Ünsüz yumuşaması kontrol ediliyor.")
        
        
        if ((str(sozcuklık[len(sozcuklık)-1])   == 'k')): # Yumuşama
            sozcuklıkğ = sozcuklık[:(len(sozcuklık)-1)] + "ğ"
            print("Sondaki k, ğ ile değiştirildi")
            print("-ın, -ım, -ımız ekleniyor.")
            sozcuklıkğın = sozcuklıkğ + 'ın'
            sozcuklıkğım = sozcuklıkğ + 'ım'
            sozcuklıkğımız = sozcuklıkğ + 'ımız'
            print(sozcuklıkğın)
            print(sozcuklıkğım)
            print(sozcuklıkğımız)
            print("-da, -daki, -dakinden, -dakinde, -dakilerce ekleniyor.")     
            sozcuklıkğında = sozcuklıkğın + 'da'
            sozcuklıkğındaki = sozcuklıkğında + 'ki'
            sozcuklıkğındakiler = sozcuklıkğındaki + 'ler'
            sozcuklıkğındakilerden = sozcuklıkğındakiler + 'den'
            sozcuklıkğındakinden = sozcuklıkğındaki + 'nden'
            sozcuklıkğındaakinde = sozcuklıkğındaki + 'nde'
            sozcuklıkğındakilerce = sozcuklıkğındakiler + 'ce'
            print(sozcuklıkğında)
            print(sozcuklıkğındaki)
            print(sozcuklıkğındakiler)
            print(sozcuklıkğındakilerden)
            print(sozcuklıkğındakinden)
            print(sozcuklıkğındaakinde)
            print(sozcuklıkğındakilerce)
    iyelik(sozcuklık)     

    def msı(sozcuklık):       
        print("-msı ekleniyor.")
        print("Yumuşama kontrol ediliyor")
        if ((str(sozcuklık[len(sozcuklık)-1])   == 'k')): # Yumuşama
            sozcuklıkğ = sozcuklık[:(len(sozcuklık)-1)] + "ğ"
            print("Sondaki k, ğ ile değiştirildi")
            sozcuklıkğmsı = sozcuklıkğ + 'ımsı'
            print(sozcuklıkğmsı)
    msı(sozcuklık)
    def sal(sozcuklık):
        print("-sal ekleniyor.")
        sozcuklıksal = sozcuklık + 'sal'
        print(sozcuklıksal)
    sal(sozcuklık)

    
lıkkalınaı(sozcuk)

