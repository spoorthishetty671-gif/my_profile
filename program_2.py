
# Number of cache lines
NUM_LINES = 8

# Initialize cache with empty lines
cache = [None] * NUM_LINES

# Memory block access sequence
blocks = [3, 11, 3, 19, 11, 27, 3]

# Initialize hit and miss counters
hits = 0
misses = 0

print("Block\tCache Line\tStatus\tCache Contents")
print("-" * 65)

# Process each memory block
for block in blocks:

    # Calculate cache line
    line = block % NUM_LINES

    # Check HIT or MISS
    if cache[line] == block:
        status = "HIT"
        hits += 1
    else:
        status = "MISS"
        misses += 1

        # Load block into cache
        cache[line] = block

    # Display cache contents after access
    print(block, "\t", line, "\t\t", status, "\t", cache)

# Calculate hit ratio
total_accesses = len(blocks)
hit_ratio = hits / total_accesses

# Display final results
print("\nTotal Accesses:", total_accesses)
print("Total Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hit_ratio)
print("Hit Ratio Percentage:", hit_ratio * 100, "%")
