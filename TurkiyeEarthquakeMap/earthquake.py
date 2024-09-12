import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükle
df = pd.read_csv('earthquake.csv')

# Tarih sütununu datetime formatına çevir
df['date'] = pd.to_datetime(df['date'])

# Yıllara göre deprem sayısı
yearly_earthquakes = df.groupby(df['date'].dt.year).size()

plt.figure(figsize=(12, 6))
yearly_earthquakes.plot(kind='bar')
plt.title('Yıllara Göre Deprem Sayısı')
plt.xlabel('Yıl')
plt.ylabel('Deprem Sayısı')
plt.xticks(rotation=60,fontsize=7)
plt.tight_layout()
plt.show()

# Deprem büyüklüğü dağılımı
plt.figure(figsize=(12, 6))
sns.histplot(df['xm'], bins=45, kde=True)
plt.title('Deprem Büyüklüğü Dağılımı')
plt.xlabel('Deprem Büyüklüğü (Xm)')
plt.ylabel('Frekans')
plt.show()

# En büyük 10 deprem
top_10_earthquakes = df.nlargest(10, 'xm')[['date', 'city', 'xm']]
print("En Büyük 10 Deprem:")
print(top_10_earthquakes)

# Derinlik ve büyüklük ilişkisi
plt.figure(figsize=(12, 6))
plt.scatter(df['depth'], df['xm'], alpha=0.5)
plt.title('Deprem Derinliği ve Büyüklüğü İlişkisi')
plt.xlabel('Derinlik (km)')
plt.ylabel('Deprem Büyüklüğü (Xm)')
plt.show()

# Şehirlere göre ortalama deprem büyüklüğü
city_avg_magnitude = df.groupby('city')['xm'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
city_avg_magnitude.plot(kind='bar')
plt.title('Şehirlere Göre Ortalama Deprem Büyüklüğü (İlk 10)')
plt.xlabel('Şehir')
plt.ylabel('Ortalama Deprem Büyüklüğü (Xm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print(df.head())


print(df.info())
