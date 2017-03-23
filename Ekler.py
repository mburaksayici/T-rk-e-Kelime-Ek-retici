
global sozcuk
sozcuk = input("Sözcüğü Giriniz:")

def uyum(sozcuk): 
    
    print("Eklerde ince sesliler mi kalın sesliler mi kullanılacak kontrol ediliyor...")
    
    if (str(sozcuk[len(sozcuk)-2])   == 'a'  ):
        import kalinunluai
    elif (str(sozcuk[len(sozcuk)-2])   == 'ı'  ):
        import kalinunluai
    elif (str(sozcuk[len(sozcuk)-2])   == 'o'  ):
        import kalinunluai
    elif (str(sozcuk[len(sozcuk)-2])   == 'u'  ):
        import kalinunluai
    elif (str(sozcuk[len(sozcuk)-1])   == 'a'  ):
        import kalinunluai
    elif (str(sozcuk[len(sozcuk)-1])   == 'ı'  ):
        import kalinunluai
    elif (str(sozcuk[len(sozcuk)-1])   == 'o'  ):
        import kalinunluai       
    elif (str(sozcuk[len(sozcuk)-1])   == 'u'  ):
        import kalinunluai         
    else:
        import kalinunluai
        

