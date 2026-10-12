# ⚛️ Quantum Mastery Lab (Interactive Prototype)

> An advanced, highly intuitive, and mathematically rigorous interactive learning platform for quantum computing, quantum mechanics, and quantum algorithms — designed for students, beginners, and engineers.

---

## 🌟 Overview & Why This Prototype Exists

Many resources teach quantum computing either with **oversimplified pop-science metaphors** ("a qubit is 0 and 1 at the same time") or with **dense textbook math** that obscures physical intuition.

**Quantum Mastery Lab** bridges this gap:
1. **Mathematical Rigor made Visual**: Demystifies Hilbert spaces $\mathbb{C}^2$, Dirac notation, and unitary transformations with real-time 3D vector and phase-space animations.
2. **Interactive Experimentation**: Move angles, drop gates, step through circuits, and immediately see probabilities, complex phases, and entanglement entropy adapt in real time.
3. **Hands-On Tasks with Automated Verification**: Write circuits to solve real challenges (Bell states, Phase kickback, Grover search), verified by an automated statevector checker with custom feedback.
4. **Gamified Quizzes**: Multi-difficulty assessment arena with instant feedback and pedagogical explanations for every answer.
5. **Direct Production Bridge**: Exports directly to **Qiskit 1.0+** Python code and **OpenQASM 2.0** for execution on real IBM Quantum superconducting hardware.

---

## 🚀 Quickstart Guide

### Option 1: Run with Local Python Server (Recommended)
Launch the built-in local server that automatically opens your default web browser:
```powershell
python start_server.py
```
Open your browser to: [http://localhost:8080](http://localhost:8080)

### Option 2: Direct Browser Launch (No server required)
You can directly open `index.html` in Chrome, Edge, Safari, or Firefox:
```powershell
# Open directly in default browser on Windows
Start-Process "index.html"
```

### Option 3: Python Quantum Simulator Companion
Run the standalone NumPy quantum statevector simulator and Bell CHSH inequality test:
```powershell
python python/quantum_engine.py
python python/run_visualizer.py
```

---

## 🔬 Core Platform Features

### 1. 🌐 3D Interactive Bloch Sphere Visualizer
* **3D Orbit & Perspective Drag**: Pure HTML5 Canvas 3D projection engine with zero external heavy 3D library dependencies.
* **Spherical Coordinates ($\theta, \phi$)**:
  * $\theta$ (polar angle): Superposition distribution between $|0\rangle$ and $|1\rangle$.
  * $\phi$ (azimuthal angle): Relative phase in the complex plane.
* **Animated Gate Trajectories**: Applying Pauli-$X, Y, Z$, Hadamard $H$, Phase $S$, and $T$ gates animates the state vector along spherical geodesics.
* **Real-Time State Readout**:
  $$|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$$
  Calculates exact Cartesian coordinates $(x, y, z)$ and Born rule measurement probabilities $P(0) = \cos^2(\theta/2), P(1) = \sin^2(\theta/2)$.

### 2. ⚡ Multi-Qubit Visual Circuit Studio & Stepper
* **2 to 4 Qubit Registers**: Configure wires and customize initial state inputs ($|0\rangle$ or $|1\rangle$).
* **Full Gate Library**:
  * Single-qubit: $H, X, Y, Z, S, T$
  * Multi-qubit: Controlled-NOT ($CX$), Controlled-Z ($CZ$), $SWAP$, and Toffoli ($CCX$).
* **Step-by-Step Execution**: Step forward, step backward, or run auto-play to watch the statevector transform *column-by-column*.
* **State Diagnostics**:
  * Full complex amplitudes ($a + bi$) for all $2^n$ basis states.
  * **Phase Wheel Clocks**: Circular dials indicating magnitude (radius) and complex argument (angle & color).
  * **Entanglement Indicator**: Computes partial trace $\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|)$ and von Neumann Entanglement Entropy $S \in [0, 1]$ bit. Distinguishes product states from maximally entangled Bell/GHZ states.
* **Measurement Simulator**: Run 1024 shots with instant probability distribution histograms.

### 3. 📚 Demystifying "Difficult Topics" Masterclass Modules
1. **The Hilbert Space Reality**: Debunking the "0 and 1 at once" myth, Dirac kets/bras, orthonormal bases, and Born's rule.
2. **Quantum Gates & Unitarity**: Why operations MUST be unitary ($U^\dagger U = I$), conservation of probability, and the No-Cloning Theorem.
3. **Quantum Interference (The True Superpower)**: Why superposition alone has no speedup; how destructive cancellation of wrong answers and constructive amplification of correct answers powers quantum computation.
4. **Entanglement & Bell's Theorem**: Non-locality, EPR paradox, CHSH inequality test ($S \le 2$ classical vs $S = 2\sqrt{2} \approx 2.828$ quantum), and why entanglement cannot send messages faster than light.
5. **Quantum Teleportation & Superdense Coding**: Step-by-step 3-qubit teleportation protocol: shared EPR pair, Bell measurement, classical bits transmission, and unitary correction.
6. **Grover's Search Algorithm**: $O(\sqrt{N})$ search speedup via 2D geometric subspace rotation, Oracle phase inversion, and Diffusion inversion about the mean.
7. **Decoherence & Quantum Error Correction (QEC)**: Environmental noise, $T_1$ (relaxation) vs $T_2$ (dephasing) timescales, and ancilla syndrome measurements.

### 4. 🎯 Hands-On Tasks & Challenge Lab
1. **Ignition: Superposition ($|+\rangle$)** — Single qubit state prep.
2. **Relative Phase: Create ($|i\rangle$)** — Manipulating complex phases.
3. **Entanglement: Bell State ($|\Phi^+\rangle$)** — Creating canonical EPR pair ($S=1.000$).
4. **The Singlet State ($|\Psi^-\rangle$)** — Rotationally invariant antisymmetric state.
5. **SWAP Synthesis** — Decomposing SWAP into exactly 3 alternating CNOTs.
6. **Grover 2-Qubit Search** — Amplifying target marked state $|11\rangle$ to 100% probability.
* **Automated Statevector Evaluator**: Evaluates circuit state fidelity $F = |\langle\psi_{target}|\psi\rangle|^2$, entropy, and gate counts, providing instant tips and celebrations.

### 5. 🧠 Interactive Quiz Arena
* **10 Curated Conceptual & Mathematical Questions**: Spans Beginner, Intermediate, and Advanced Engineer categories.
* **Instant Explanations**: Deep explanations for both correct and incorrect choices.
* **Score & Rank Tracking**: Earn titles from *Quantum Explorer* to *Quantum Architect (Mastery)*.

### 6. 💻 Production Code Exporter
* Generates runnable **Qiskit 1.0+** Python code and **OpenQASM 2.0** text.
* One-click copy for execution in Jupyter notebooks or IBM Quantum Cloud.

---

## 📁 Repository Structure
```
quantum-mastery-lab/
├── index.html                  # Responsive modern web platform
├── css/
│   └── styles.css              # Custom styling, glow effects, theme tokens
├── js/
│   ├── complex.js              # Complex number mathematics engine
│   ├── bloch.js                # 3D Bloch sphere Canvas visualizer
│   ├── quantum-engine.js       # Core quantum statevector simulator & entropy
│   ├── circuit-ui.js           # Interactive visual circuit grid & step runner
│   ├── curriculum.js           # Masterclass curriculum & lesson data
│   ├── challenges.js           # Tasks engine with automated verification
│   ├── quiz.js                 # Multi-tier quiz engine & evaluation
│   └── app.js                  # Master application orchestrator
├── python/
│   ├── quantum_engine.py       # Standalone NumPy quantum simulator & CHSH test
│   └── run_visualizer.py       # Matplotlib statevector & histogram visualizer
├── start_server.py             # One-click local HTTP server launcher
└── README.md                   # Full documentation & guide
```

---

## 🛠️ Requirements & Compatibility
* **Web**: Any modern browser (Chrome, Edge, Firefox, Safari). Zero build tools required.
* **Python (Optional)**: Python 3.9+ with `numpy` and `matplotlib` (already tested and verified).
