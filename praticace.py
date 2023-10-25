import skfuzzy
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control


dominio_fila = np.arange(0,21,1)
dominio_ext = np.arange(0,21,1)

f1 = control.Antecedent(dominio_fila, "f1")
f2 = control.Antecedent(dominio_fila, "f2")
f3 = control.Antecedent(dominio_fila, "f3")
f4 = control.Antecedent(dominio_fila, "f4")

ext = control.Consequent(dominio_ext, "ext")

f1["pequeno"] = skfuzzy.trimf(f1.universe,[0,4,8])
f1["media"] = skfuzzy.trimf(f1.universe,[4,8,12])
f1["longa"] = skfuzzy.trapmf(f1.universe,[8,12,20,20])

f2["pequeno"] = skfuzzy.trimf(f2.universe,[0,4,8])
f2["media"] = skfuzzy.trimf(f2.universe,[4,8,12])
f2["longa"] = skfuzzy.trapmf(f2.universe,[8,12,20,20])

f3["pequeno"] = skfuzzy.trimf(f3.universe,[0,4,8])
f3["media"] = skfuzzy.trimf(f3.universe,[4,8,12])
f3["longa"] = skfuzzy.trapmf(f3.universe,[8,12,20,20])

f4["pequeno"] = skfuzzy.trimf(f4.universe,[0,4,8])
f4["media"] = skfuzzy.trimf(f4.universe,[4,8,12])
f4["longa"] = skfuzzy.trapmf(f4.universe,[8,12,20,20])

ext["zero"] = skfuzzy.trimf(ext.universe,[0,0,5])
ext["pequeno"] = skfuzzy.trimf(ext.universe,[0,4,8])
ext["media"] = skfuzzy.trimf(ext.universe,[4,8,12])
ext["longa"] = skfuzzy.trapmf(ext.universe,[8,12,20,20])

#f1.view()

r1 = control.Rule(f1["longa"] & f2["pequeno"], ext["longa"])
r2 = control.Rule(f3["media"] | f4["pequeno"], ext["media"])
r3 = control.Rule(f2["longa"] & f1["pequeno"], ext["zero"])

# r1.view()
# r2.view()
# r3.view()

semaforo_controle = control.ControlSystem([r1,r2,r3])
sA = control.ControlSystemSimulation(semaforo_controle)

sA.input["f1"] = 10
sA.input["f2"] = 3
sA.input["f3"] = 0
sA.input["f4"] = 1

sA.compute()
print(sA.output)
ext.view(sim=sA)
plt.show()