import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametri di massa e costante gravitazionale
G = 1.0  # Costante gravitazionale arbitraria per semplificare i calcoli
masses = [1.0, 1.0, 1.0]  # Masse dei corpi (uguali)

# Definizione delle equazioni di movimento
def three_body_equations(t, y):
    r1, r2, r3 = y[:2], y[2:4], y[4:6]
    v1, v2, v3 = y[6:8], y[8:10], y[10:12]

    def acceleration(rA, rB, mB):
        distance_vector = rB - rA
        distance = np.linalg.norm(distance_vector)
        return G * mB * distance_vector / distance**3 if distance != 0 else np.zeros(2)

    a1 = acceleration(r1, r2, masses[1]) + acceleration(r1, r3, masses[2])
    a2 = acceleration(r2, r1, masses[0]) + acceleration(r2, r3, masses[2])
    a3 = acceleration(r3, r1, masses[0]) + acceleration(r3, r2, masses[1])

    return np.concatenate((v1, v2, v3, a1, a2, a3))

# Condizioni iniziali casuali
np.random.seed()  # Cambia il seme per ottenere risultati differenti ad ogni esecuzione
initial_positions = np.random.uniform(-1, 1, (3, 2))  # Posizioni casuali in un range [-1, 1]
initial_velocities = np.random.uniform(-1, 1, (3, 2))  # Velocità casuali in un range [-1, 1]

# Creiamo lo stato iniziale come un vettore
initial_state = np.concatenate((initial_positions.flatten(), initial_velocities.flatten()))

# Risoluzione numerica con durata estesa della simulazione e maggior numero di intervalli
t_span = (0, 100)  # Maggior durata
t_eval = np.linspace(*t_span, 7000)  # Maggior numero di intervalli

sol = solve_ivp(three_body_equations, t_span, initial_state, t_eval=t_eval)

# Configurazione per l'animazione
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Definiamo i colori per le palline e le scie
colors = ['blue', 'green', 'red']

# Inizializziamo i punti e le linee di scia
points = [ax.plot([], [], 'o', color=colors[i], ms=8)[0] for i in range(3)]
trail_length = 100  # Lunghezza della scia in numero di posizioni
trails = [ax.plot([], [], lw=1, color=colors[i], alpha=0.6)[0] for i in range(3)]  # Linee per le scie

# Funzione di aggiornamento per l'animazione
def update(frame):
    if frame >= sol.y.shape[1]:  # Verifica che il frame sia nei limiti di sol.y
        return points + trails  # Se no, ritorna senza modificare
    # Posizioni attuali delle palline
    positions = sol.y[:6, frame].reshape(3, 2)
    for i, point in enumerate(points):
        point.set_data(positions[i, 0], positions[i, 1])

    # Aggiornamento delle scie
    for i, trail in enumerate(trails):
        start = max(0, frame - trail_length)
        trail.set_data(sol.y[i*2, start:frame], sol.y[i*2+1, start:frame])
    
    # Aggiorna i limiti dell'asse per mantenere le palline visibili
    all_x = sol.y[0:6:2, frame]
    all_y = sol.y[1:6:2, frame]
    ax.set_xlim(all_x.min() - 0.5, all_x.max() + 0.5)
    ax.set_ylim(all_y.min() - 0.5, all_y.max() + 0.5)
    
    return points + trails

ani = FuncAnimation(fig, update, frames=sol.y.shape[1], interval=30, blit=True)
plt.show()
