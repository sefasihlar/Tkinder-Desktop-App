import tkinter as tk
from typing import Text
pencere = tk.Tk()
#ana sayfa 
pencere.geometry("1000x800")
pencere.wm_attributes("-alpha",0.8)
pencere.configure(background="black")
#başlık
label = tk.Label(text="Karar Verme Teknikleri",font="35",fg="white",bg="black")
label.pack()
#amaç yazısı
labelu = tk.Label(text="İyimserlik Ölçütü",font="70",fg="white",bg="black")
labelu.pack()
b=[]

#matrix algoritması beyaz ksımlalrın olusturlması

for i in range(0,20):
    b.append(tk.Entry(pencere,width="15"))
    
sayac=0

for i in range(0,6):
    for j in range(0,3):
        b[sayac].place(x=300+i*100,y=300+j*40,height="50")
        sayac +=1

        a = b[1]
        

#dogal durum butonları 

alt = tk.Button(pencere,width="26",bg="orange",text="İYİ")
alt.place(x=300,y=240,height="40")

alt1 = tk.Button(pencere,width="26",bg="orange",text="AYNI")
alt1.place(x=500,y=240,height="40")

alt2 = tk.Button(pencere,width="26",bg="orange",text="KÖTÜ")
alt2.place(x=700,y=240,height="40")

#label1

lbl_a=tk.Label(text="DOGAL DURUMLAR",width="35")
lbl_a.place(x=425,y=160,height="50")

#label2

lbl_a=tk.Label(text="ALTERNATİFLER",width="34")
lbl_a.place(x=30,y=240,height="40")

#İYİMSERLİK LABEL

# altarnetifler
alt4 = tk.Entry(pencere,width="40",bg="YELLOW")
alt4.place(x=30,y=300,height="40")

alt5 = tk.Entry(pencere,width="40",bg="YELLOW")
alt5.place(x=30,y=345,height="40")

alt6 = tk.Entry(pencere,width="40",bg="YELLOW")
alt6.place(x=30,y=390,height="40")

#hesaplamalar

def hesapla():
    # 1.altarnetif verileri
    x1 = int(b[0].get())
    x2 = int(b[3].get())
    x3= int(b[6].get())
    x4= int(b[9].get())
    x5= int(b[12].get())
    x6= int(b[15].get())
    
    sayilar=[x1,x2,x3,x4,x5,x6]
    max1=max(sayilar)
    w = alt4.get()
    
    #2.altarnetif verileri
    s1 = int(b[1].get())
    s2 = int(b[4].get())
    s3= int(b[7].get())
    s4= int(b[10].get())
    s5= int(b[13].get())
    s6= int(b[16].get())

    sayilar2=[s1,s2,s3,s4,s5,s6]
    r= alt5.get()
    max2=max(sayilar2)
    

    #3.altarnetif verileri
    e1 = int(b[2].get())
    e2 = int(b[5].get())
    e3= int(b[8].get())
    e4= int(b[11].get())
    e5= int(b[14].get())
    e6= int(b[17].get())
 
    sayilar3=[e1,e2,e3,e4,e5,e6]

    z = alt6.get()
    
    max3=max(sayilar3)

    #iyimserlik ölçütü label

    lbl_ö1=tk.Label(pencere,text=f"{max1}",width="12")
    lbl_ö1.place(x=900,y="300",height="40")

    lbl_ö2=tk.Label(pencere,text=f"{max2}",width="12")
    lbl_ö2.place(x=900,y="345",height="40")

    lbl_ö3=tk.Label(pencere,text=f"{max3}",width="12")
    lbl_ö3.place(x=900,y="390",height="40")

    #ölçüt degerleri lbl

    lbl_ö = tk.Button(pencere,width="12",bg="#7FFF00",text="İYİMSERLİK-Ö")
    lbl_ö.place(x="900",y="240",height="40")

    if max1>max2 and max1>max3:
        lbl_a=tk.Label(text=f"iyimserlik ölçütüne göre karar{w} şirketine yatırım yapmanız en iyi seçim olacaktır",width="100".format(w=w),bg="#7FFF00")
        lbl_a.place(x=300,y=600,height="100")

    elif max2>max1 and max2>max3:

        lbl_a=tk.Label(text=f"iyimserlik ölçütüne göre karar {r} şirketine yatırım yapmanız en iyi seçim olacaktır",width="100".format(r=r),bg="#7FFF00")
        lbl_a.place(x=300,y=600,height="100")

    elif max3>max1 and max3>max2:

        lbl_a=tk.Label(text=f"İyimserlik ölçütüne göre karar {z} seçimini yap",width="100".format(z=z),bg="#7FFF00")
        lbl_a.place(x=300,y=600,height="100")
    else:
        print("degerleri tekrar gözden geçiriniz")

#maliyet yapılı hesaplama
def maliyet():
    # 1.altarnetif verileri
    x1 = int(b[0].get())
    x2 = int(b[3].get())
    x3= int(b[6].get())
    x4= int(b[9].get())
    x5= int(b[12].get())
    x6= int(b[15].get())
    
    sayilar=[x1,x2,x3,x4,x5,x6]
    min1=min(sayilar)
    w = alt4.get()
    
    #2.altarnetif verileri
    s1 = int(b[1].get())
    s2 = int(b[4].get())
    s3= int(b[7].get())
    s4= int(b[10].get())
    s5= int(b[13].get())
    s6= int(b[16].get())

    sayilar2=[s1,s2,s3,s4,s5,s6]
    r= alt5.get()
    min2=min(sayilar2)
    
    #3.altarnetif verileri
    e1 = int(b[2].get())
    e2 = int(b[5].get())
    e3= int(b[8].get())
    e4= int(b[11].get())
    e5= int(b[14].get())
    e6= int(b[17].get())

    sayilar3=[e1,e2,e3,e4,e5,e6]


    z = alt6.get()
    
    min3=min(sayilar3)

    #iyimserlik ölçütü label

    lbl_ö1=tk.Label(pencere,text=f"{min1}",width="12")
    lbl_ö1.place(x=900,y="300",height="40")

    lbl_ö2=tk.Label(pencere,text=f"{min2}",width="12")
    lbl_ö2.place(x=900,y="345",height="40")

    lbl_ö3=tk.Label(pencere,text=f"{min3}",width="12")
    lbl_ö3.place(x=900,y="390",height="40")

    #ölçüt degerleri lbl

    lbl_ö = tk.Button(pencere,width="12",text="MALİYET.Y",bg="#8ac4ff")
    lbl_ö.place(x="900",y="240",height="40")

    if min1<min2 and min1<min3:
        lbl_a=tk.Label(text=f"Maliyet yapılı çözüme göre:{ w} şirketine yatırım yapmanız en iyi seçim olucaktır",width="100".format(w=w),bg="#8ac4ff")
        lbl_a.place(x=300,y=600,height="100")

    elif min2<min1 and min2<min3:

        lbl_a=tk.Label(text=f"Maliyet yapılı çözüme göre: { r} şirketine yatırım yapmanız en iyi seçim olucaktır",width="100".format(r=r),bg="#8ac4ff")
        lbl_a.place(x=300,y=600,height="100")

    elif min3<min1 and min3<min2:

        lbl_a=tk.Label(text=f"Maliyet yapılı çözüme göre: { z} seçimini yap",width="100".format(z=z),bg="#8ac4ff")
        lbl_a.place(x=300,y=600,height="100")
    else:
        print("degerleri tekrar gözden geçiriniz")
#ekle fonksiyonu
def ekle():
    alt7 = tk.Entry(pencere,width="40",bg="YELLOW")
    alt7.place(x=30,y=435,height="40")

    a=[]

    for i in range(0,20):
        a.append(tk.Entry(pencere,width="15"))
    
    sayac=0
   
    for i in range(0,6):
        for j in range(0,1):
            x =a[sayac].place(x=300+i*100,y=430+j*40,height="50")
            sayac +=1
    # sil foksiyonu
    def sil():
        alt7.destroy()
        for i in a:
            i.destroy()
    #sil butonu
    btn_sil= tk.Button(text="SİL",bg="red",command=sil)
    btn_sil.place(x="300",y="500",height="75",width="130")

#hesaplama butonu

btn = tk.Button(text="HESAPLA",command=hesapla,bg="#7FFF00")
btn.place(x="760",y="500",height="75",width="130")

#maliyet yapılı hesapla butonu
btn_ekle= tk.Button(text="HESAPLA.M",command=maliyet,bg="#8ac4ff")
btn_ekle.place(x="610",y="500",height="75",width="130",)

#ekle butonu
btn_ekle= tk.Button(text="EKLE",command=ekle,bg="#ffff00")
btn_ekle.place(x="460",y="500",height="75",width="130",)

pencere.mainloop()











    
