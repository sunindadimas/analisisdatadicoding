import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style("whitegrid")
sns.set(rc={"axes.facecolor":"#FFF9ED","figure.facecolor":"#FFF9ED"})
palette = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60","#84596B","#917B99","#AE8CA3","#C4A7CB"]

st.title("Air Quality Public Dataset")
st.write("**Dashboard for analyzing Air Quality Public Dataset**")

all_data = pd.read_csv("https://raw.githubusercontent.com/sunindadimas/analisisdatadicoding/main/Dashboard/main_data.csv")

pal = ["#FF0000", "#FFFF00", "#008000", "#FF0000", "#FFFF00", "#008000", "#FF0000", "#FFFF00", "#008000", "#FF0000", "#FFFF00", "#008000", "#FF0000", "#FFFF00", "#008000"]

st.write("**1. Apakah perkembangan tren kualitas udara dari tahun 2013 s/d 2017 mengelami penurunan atau peningkatan?**")
st.write("**Tren Perkembangan Kualitas Udara 2013 s/d 2017**")

mean_kualitas = all_data.groupby(['year', 'month'])['Kualitas'].mean()
mean_kualitas.index = mean_kualitas.index.map(lambda x: f'{x[0]}-{x[1]:02d}')
plt.figure(figsize=(20, 7))
plt.plot(mean_kualitas.index, mean_kualitas.values, marker='o', linestyle='-', color="#FF0000")
plt.xlabel('Year-Month', labelpad=20, fontsize=13)
plt.ylabel('Kualitas Udara', labelpad=20, fontsize=13)
plt.title('Tren Perkembangan Kualitas Udara', fontsize=25, pad=20, fontweight='bold')
plt.xticks(rotation=45)
plt.xlim(mean_kualitas.index[0], mean_kualitas.index[-1])
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

text_perkembangan = """
**Perkembangan Kualitas Udara: Pola dan Variabilitas**

Analisis data menunjukkan adanya penurunan kualitas udara dari Maret 2013 hingga Februari 2017, meskipun terdapat fluktuasi yang signifikan selama periode tersebut.

Bulan Desember 2015 mencuat sebagai periode dengan kualitas udara paling buruk di berbagai wilayah. Hal ini menyoroti perlunya investigasi lebih lanjut untuk memahami faktor-faktor yang mempengaruhi penurunan drastis kualitas udara pada bulan tersebut.

Di sisi lain, bulan Mei 2016 tercatat sebagai periode dengan kualitas udara terbaik. Hal ini menunjukkan bahwa upaya untuk meningkatkan kualitas udara dapat memberikan hasil yang positif.

Secara keseluruhan, data menunjukkan bahwa masih banyak pekerjaan yang harus dilakukan untuk mencapai tingkat kualitas udara yang optimal. Diperlukan upaya berkelanjutan dari berbagai pihak untuk mengatasi berbagai faktor yang menyebabkan pencemaran udara.
"""
st.write(text_perkembangan)

yearly_means = all_data.groupby("year")[["PM2.5", "PM10", "SO2", "NO2", "O3"]].mean()
plt.figure(figsize=(10, 6))
for i, feature in enumerate(yearly_means.columns):
    plt.plot(yearly_means.index, yearly_means[feature], label=feature, marker='o', color=pal[i])
plt.xlabel('Tahun', labelpad=10, fontsize=13)
plt.ylabel('Indeks', labelpad=10, fontsize=13)
plt.title('Tren Perkembangan Polutan', fontsize=20, pad=20, fontweight='bold')
plt.xticks(range(2013, 2016))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.88))
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

text_perkembangan_polutan = """
**Analisis Trend Polusi Udara (Maret 2013 - Februari 2017)**

Dari analisis data, terlihat bahwa rata-rata tingkat polutan udara menunjukkan variasi selama periode Maret 2013 hingga Februari 2017.
- PM10 dan PM2.5: Terjadi kenaikan rata-rata tingkat PM10 dan PM2.5, menunjukkan peningkatan risiko kesehatan masyarakat terhadap paparan partikel-partikel halus ini.
- O3: Rata-rata tingkat O3 mengalami penurunan, yang dapat berdampak negatif pada kesehatan manusia dan ekosistem.
- NO2: Rata-rata tingkat NO2 mengalami peningkatan, yang merupakan gas beracun yang dapat memperburuk penyakit pernapasan.
- SO2: Terjadi sedikit penurunan rata-rata tingkat SO2, menunjukkan adanya perbaikan dalam emisi sulfur dioksida.
"""
st.write(text_perkembangan_polutan)

st.write("**2. Bagaimana dengan kualitas udara pada waktu malam hari apakah baik untuk beraktivitas?**")

waktu_means = all_data.groupby("Waktu")["Kualitas"].mean()
plt.figure(figsize=(10, 6))
waktu_means.plot(kind="bar", stacked=False, color=pal)
plt.xlabel('Waktu', labelpad=10, fontsize=13)
plt.ylabel('Indeks', labelpad=10, fontsize=13)
plt.title('Kualitas Udara Pagi & Malam', fontsize=20, pad=20, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

st.write("**Pada malam hari kualitas udara kurang baik, maka kuarangi untuk melakukan aktivitas dimalam hari.**")

waktu_means = all_data.groupby("Waktu")[["PM10", "PM2.5", "NO2", "O3", "SO2"]].mean()
plt.figure(figsize=(10, 6))
waktu_means.plot(kind="bar", stacked=False, color=pal)
plt.xlabel('Waktu', labelpad=10, fontsize=13)
plt.ylabel('Indeks', labelpad=10, fontsize=13)
plt.title('Molekul Polutan Pagi & Malam', fontsize=20, pad=20, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title="Polutan", loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

text_malam_pagi = """
**Kualitas Udara pada Malam Hari dan Rekomendasi Aktivitas**

Data menunjukkan bahwa kualitas udara cenderung lebih buruk pada malam hari dibandingkan pagi dan siang hari. Hal ini disebabkan oleh beberapa faktor, antara lain:

- Inversi Suhu: Pada malam hari, suhu udara di permukaan bumi lebih rendah dibandingkan dengan udara di atasnya, menyebabkan udara dingin terperangkap di permukaan dan menghambat dispersi polutan.
- Aktivitas Kendaraan: Aktivitas kendaraan umumnya berkurang pada malam hari, menyebabkan emisi kendaraan tertahan di sekitar permukaan bumi.
- Emisi Industri: Beberapa industri beroperasi pada malam hari dan emisi industri ini dapat berkontribusi pada penurunan kualitas udara.

Sebagai rekomendasi, disarankan untuk mengurangi aktivitas luar ruangan pada malam hari dan mengurangi penggunaan kendaraan bermotor untuk membantu mengurangi emisi polutan udara.
"""
st.write(text_malam_pagi)


st.title('Kesimpulan')

text_kesimpulan="""
Berdasarkan analisis data kualitas udara dari tahun 2013 hingga 2017, dapat ditarik kesimpulan sebagai berikut:

**Pertanyaan 1: Tren Kualitas Udara**

1. Secara umum, kualitas udara mengalami peningkatan buruk dari tahun 2013 hingga 2017.

2. Terdapat fluktuasi kualitas udara yang signifikan dalam periode tersebut, dengan bulan Desember 2015 sebagai bulan dengan kualitas udara terburuk dan Mei 2016 sebagai bulan terbaik.

**Pertanyaan 2: Kualitas Udara Malam Hari**

1. Pada malam hari, kualitas udara umumnya lebih buruk dibandingkan dengan pagi dan siang hari.

2. Hal ini disebabkan oleh beberapa faktor, seperti inversi suhu, berkurangnya aktivitas kendaraan, dan emisi industri.
Oleh karena itu, disarankan untuk tidak terlalu sering beraktivitas di luar ruangan pada malam hari, terutama bagi orang-orang yang memiliki masalah kesehatan pernapasan.
 
Kesimpulan:

KKualitas udara di berbagai daerah memerlukan perhatian serius dan tindakan berkelanjutan dari berbagai pihak untuk meningkatkannya. Upaya ini dapat dilakukan dengan berbagai cara, antara lain:
- Mengurangi emisi gas buang kendaraan dengan menerapkan standar emisi yang lebih ketat dan mendorong penggunaan kendaraan yang ramah lingkungan.
- Mengurangi emisi dari industri dengan menerapkan teknologi yang lebih bersih dan efisien.
- Meningkatkan kesadaran masyarakat tentang pentingnya menjaga kualitas udara dan mendorong mereka untuk berperilaku yang ramah lingkungan.
- Memberikan himbauan kepada masyarakat untuk mengurangi aktivitas di luar ruangan pada malam hari dan saat kualitas udara buruk untuk menghindari paparan terhadap polutan udara yang berbahaya bagi kesehatan.
"""

st.write(text_kesimpulan)
