from keplergl import KeplerGl
import pandas as pd

# Veri yükleme
data = pd.read_csv("earthquake.csv")

# Türkiye için merkez ve zoom seviyesini ayarlayan config
config = {
    "version": "v1",
    "config": {
        "mapState": {
            "bearing": 0,
            "dragRotate": False,
            "latitude": 39.0,   # Türkiye'nin yaklaşık enlemi
            "longitude": 35.0,  # Türkiye'nin yaklaşık boylamı
            "pitch": 0,
            "zoom": 5.0  # Yakınlaştırma seviyesi
        }
    }
}

# Kepler.gl haritası oluşturma ve config ile başlatma
map1 = KeplerGl(height=600, config=config)

# Veriyi haritaya ekleme
map1.add_data(data, "Map Data")

# Haritayı HTML olarak kaydetme
map1.save_to_html(file_name='kepler_map_turkey.html')
