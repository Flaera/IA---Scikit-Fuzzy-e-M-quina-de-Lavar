import numpy as np
import skfuzzy
import matplotlib.pyplot as plt
from skfuzzy import control


dominio_fila = np.arange(0,1001,1)

f1 = control.Antecedent(dominio_fila,"f1")
f2 = control.Antecedent(dominio_fila,"f2")
f3 = control.Consequent(dominio_fila,"f3")
# ext = control.Consequent(dominio_ext,"ext")

"""
RULES:
se agua pouca entao eletricidade media
se agua pouca e detergente pouca entao eletricidade baixa
se detergente alta entao eletricidade alta
"""

#detergente:
f1["pouca"] = skfuzzy.trapmf(f1.universe,[0,100,250,300])
f1["media"] = skfuzzy.trimf(f1.universe,[200,500,650])
f1["alta"] = skfuzzy.trapmf(f1.universe,[500,700,1000,1000])
#agua:
f2["pouca"] = skfuzzy.trapmf(f2.universe,[0,100,250,300])
f2["media"] = skfuzzy.trimf(f2.universe,[200,500,650])
f2["alta"] = skfuzzy.trapmf(f2.universe,[500,700,1000,1000])
#eletricidade
f3["baixa"] = skfuzzy.trapmf(f3.universe,[0,100,250,700])
f3["media"] = skfuzzy.trimf(f3.universe,[200,500,650])
f3["alta"] = skfuzzy.trapmf(f3.universe,[500,700,1000,1000])

r2 = control.Rule(f2["pouca"], f3["media"])
r3 = control.Rule(f2["pouca"] & f1["pouca"], f3["baixa"])
r4 = control.Rule(f1["alta"], f3["alta"])

# r2.view()
# r3.view()
# r4.view()

lavanderia_control = control.ControlSystem([r2,r3,r4])
simulator_lav = control.ControlSystemSimulation(lavanderia_control)

simulator_lav.input["f1"] = 6
simulator_lav.input["f2"] = 2

simulator_lav.compute()
print(simulator_lav.output)
f3.view(simulator_lavanderia=simulator_lav)

plt.show()
