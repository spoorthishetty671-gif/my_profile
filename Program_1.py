
# Initialize memory
memory = {
    100: 12,
    104: 8
}

# Initialize registers
registers = {
    "R1": 0,
    "R2": 0,
    "R3": 0
}

# Execute instruction a
print("Instruction: LOAD R1, 100")
registers["R1"] = memory[100]
print("R1 =", registers["R1"])

# Execute instruction b
print("\nInstruction: LOAD R2, 104")
registers["R2"] = memory[104]
print("R2 =", registers["R2"])

# Execute instruction c
print("\nInstruction: ADD R3, R1, R2")
registers["R3"] = registers["R1"] + registers["R2"]
print("R1 =", registers["R1"])
print("R2 =", registers["R2"])
print("R3 =", registers["R3"])

# Execute instruction d
print("\nInstruction: STORE R3, 108")
memory[108] = registers["R3"]

# Display final register contents
print("\nFinal Register Contents:")
print("R1 =", registers["R1"])
print("R2 =", registers["R2"])
print("R3 =", registers["R3"])

# Display final memory contents
print("\nFinal Memory Contents:")
print("M[108] =", memory[108])
