# Lorenz Chaos Encryptor 🦋

A symmetric stream cipher cryptography engine built entirely from scratch using the 3D Lorenz Attractor differential equations. 

## 🧠 The Math Behind the Code
This project leverages Chaos Theory—specifically the "Butterfly Effect" (sensitive dependence on initial conditions)—to generate highly unpredictable cryptographic keys. 

Instead of relying on standard random number generators, this engine mathematically simulates a 3D chaotic system:
* **Initial State (Seed):** The system starts at specific coordinates `(x0, y0, z0)`.
* **Transient Phase (Burn-in):** The engine runs for 100 iterations without encrypting to ensure the system enters a state of deep, unpredictable chaos.
* **XOR Bitwise Encryption:** The chaotic trajectory is translated into bytes (0-255) and XORed with the ASCII values of the plaintext.

## 🚀 Features
- **Zero External Crypto Libraries:** The encryption logic is 100% math-driven and written from scratch.
- **Symmetric Decryption:** The exact same Lorenz trajectory is recalculated to flawlessly decrypt the ciphertext.
- **High Sensitivity:** Altering the initial coordinates by even `0.00001` results in a completely different encryption path, rendering differential brute-force attacks useless.

## 💻 Tech Stack
- Python 3.x
- Numpy (for mathematical operations)

> *"Chaos is merely order waiting to be deciphered."*