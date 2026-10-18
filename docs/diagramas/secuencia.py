import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
act = ["Ciudadano","Controlador\n(MVC)","GestorCasos\n(Singleton)","FaunaFactory\n(Factory Method)","Expediente","Voluntario\n(Observer)"]
x = [i*2.6 for i in range(len(act))]
msgs = [(0,1,"reportar(especie, nombre, ubicación)"),(1,2,"registrar_rescate(...)"),(2,3,"fabrica_para(especie).crear_expediente(...)"),(3,4,"«create»"),(4,2,"expediente"),(2,5,"notificar() → actualizar(expediente)"),(2,1,"expediente registrado"),(1,0,"vista.mostrar_caso(e)")]
fig, ax = plt.subplots(figsize=(14,6.5)); ax.axis("off"); ax.set_xlim(-1.5,x[-1]+1.5); ax.set_ylim(-len(msgs)-1.2,1.5)
for xi,a in zip(x,act):
    ax.text(xi,1,a,ha="center",va="center",fontsize=9,bbox=dict(boxstyle="round",fc="#FFF9C4",ec="#444"))
    ax.plot([xi,xi],[0.5,-len(msgs)-0.6],ls="--",c="#888",lw=1)
for i,(a,b,t) in enumerate(msgs):
    y=-i-0.3
    ax.annotate("",xy=(x[b],y),xytext=(x[a],y),arrowprops=dict(arrowstyle="->",lw=1.3,ls="--" if b<a else "-"))
    ax.text((x[a]+x[b])/2,y+0.12,f"{i+1}: {t}",ha="center",fontsize=8)
ax.set_title("Diagrama de secuencia: Reportar un rescate (Singleton + Factory Method + Observer + MVC)",fontsize=11)
plt.savefig("secuencia.png",dpi=130,bbox_inches="tight")
