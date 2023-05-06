
import numpy as np

np.random.seed(42)

ids = np.random.randint(0, 1562, size=100)
idades = np.random.randint(18, 90, size=100)
sexos = np.random.choice(['F', 'M'], size=100)
estados_civis = np.random.choice(['solteiro', 'casado', 'divorciado', 'viuvo'], size=100) 
sinistros = np.random.randint(0, 2, size=100)
premios = np.round(np.random.uniform(500, 2000, size=100), 2)

np.savetxt('Dados/ids.txt', ids, fmt='%d')
np.savetxt('Dados/idades.txt', idades, fmt='%d')
np.savetxt('Dados/sexos.txt', sexos, fmt='%s')
np.savetxt('Dados/estados_civis.txt', estados_civis, fmt='%s')
np.savetxt('Dados/sinistros.txt', sinistros, fmt='%d')
np.savetxt('Dados/premios.txt', premios, fmt='%.2f')
