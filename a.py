import pandas as pd

# Excel dosyasının yolu ve adı
excel_dosya_yolu = r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\Val.xlsx'

# Excel dosyasını DataFrame'e yükle
df = pd.read_excel(excel_dosya_yolu)

# 'your_column' sütunundaki her satırı kontrol et
for index, row in df.iterrows():
    # Cümlede "one" kelimesi varsa 1, "two" kelimesi varsa 2 olarak işaretle
    if 'one' in str(row['text']):
        df.at[index, 'numbel'] = 1
    elif 'two' in str(row['text']):
        df.at[index, 'numbel'] = 2
    elif 'zero' in str(row['text']):
        df.at[index, 'numbel'] = 0
    elif 'three' in str(row['text']):
        df.at[index, 'numbel'] = 3
    elif 'four' in str(row['text']):
        df.at[index, 'numbel'] = 4
    elif 'five' in str(row['text']):
        df.at[index, 'numbel'] = 5
    elif 'six' in str(row['text']):
        df.at[index, 'numbel'] = 6
    elif 'seven' in str(row['text']):
        df.at[index, 'numbel'] = 7
    elif 'eight' in str(row['text']):
        df.at[index, 'numbel'] = 8
    elif 'nine' in str(row['text']):
        df.at[index, 'numbel'] = 9   

# Sonucu başka bir Excel dosyasına kaydetmek istiyorsanız:
df.to_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\result1.xlsx', index=False)
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\Val.xlsx')

# lupper, lmiddle, llower sütunlarını ekleyerek başlangıç değerini 0 olarak atayın
df['lupper'] = 0
df['lmiddle'] = 0
df['llower'] = 0

# Her bir satırdaki cümleleri kontrol et
for index, row in df.iterrows():
    sentence = str(row['text'])  # 'Cümle' sütunu, cümlenin bulunduğu sütun adıyla değiştirilmelidir.

    # Cümlede 'upper left' varsa lupper değeri 1 olsun
    if 'upper left' in sentence:
        df.at[index, 'lupper'] = 1

    # Cümlede 'middle left' varsa lmiddle değeri 1 olsun
    if 'middle left' in sentence:
        df.at[index, 'lmiddle'] = 1

    # Cümlede 'lower left' varsa llower değeri 1 olsun
    if 'lower left' in sentence:
        df.at[index, 'llower'] = 1

    # Cümlede 'all left' varsa lupper, lmiddle, llower değerleri 1 olsun
    if 'all left' in sentence:
        df.at[index, 'lupper'] = 1
        df.at[index, 'lmiddle'] = 1
        df.at[index, 'llower'] = 1

# Sonuçları yeni bir Excel dosyasına kaydet
df.to_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\Tesa.xlsx', index=False)



# Veya aynı dosyaya kaydetmek istiyorsanız:
#df.to_excel(excel_dosya_yolu, index=False)
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\Val.xlsx')

# lupper, lmiddle, llower sütunlarını ekleyerek başlangıç değerini 0 olarak atayın
df['rupper'] = 0
df['rmiddle'] = 0
df['rlower'] = 0

# Her bir satırdaki cümleleri kontrol et
for index, row in df.iterrows():
    sentence = str(row['text'])  # 'Cümle' sütunu, cümlenin bulunduğu sütun adıyla değiştirilmelidir.

    # Cümlede 'upper left' varsa lupper değeri 1 olsun
    if 'upper right' in sentence:
        df.at[index, 'rupper'] = 1

    # Cümlede 'middle left' varsa lmiddle değeri 1 olsun
    if 'middle right' in sentence:
        df.at[index, 'rmiddle'] = 1

    # Cümlede 'lower left' varsa llower değeri 1 olsun
    if 'lower right' in sentence:
        df.at[index, 'rlower'] = 1

    # Cümlede 'all left' varsa lupper, lmiddle, llower değerleri 1 olsun
    if 'all right' in sentence:
        df.at[index, 'rupper'] = 1
        df.at[index, 'rmiddle'] = 1
        df.at[index, 'rlower'] = 1

# Sonuçları yeni bir Excel dosyasına kaydet
df.to_excel(r'C:\Users\uurce\OneDrive\Masaüstü\yeniset\result12.xlsx', index=False)
