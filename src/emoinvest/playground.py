from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt


ti = TechIndicators(key='3NYOU6ML1J5P3L40', output_format='pandas')
data, meta_data = ti.get_rsi(symbol='^GSPC', interval='60min', time_period=20)
data.plot()
a = len(data)
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()

a = 1

from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='3NYOU6ML1J5P3L40', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

a = 1