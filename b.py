import pandas as pd

# Excel dosyasını oku
df = pd.read_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\Val.xlsx')



# 'bilateral' sütununu ekleyerek başlangıç değerini 0 olarak atayın
df['bilateral'] = 0

# Her bir satırdaki cümleleri kontrol et
for index, row in df.iterrows():
    sentence = str(row['text'])  # 'Cümle' sütunu, cümlenin bulunduğu sütun adıyla değiştirilmelidir.

    # Cümlede 'bilateral' kelimesi varsa bilateral değeri 1 olsun
    if 'bilateral' in sentence.lower():
        df.at[index, 'bilateral'] = 1



# Sonuçları yeni bir Excel dosyasına kaydet
df.to_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\Test_text12312.xlsx', index=False)
