
# Assignment 3: Understanding Algorithm Efficiency and Scalability

This project analyzes and compares the efficiency and scalability of two core algorithmic techniques:

1. **Randomized Quicksort**
2. **Hash Table with Chaining**

---

## 📂 Contents

- `randomized_quicksort.py` – Implements Quicksort with a random pivot.
- `deterministic_quicksort.py` – Implements classic Quicksort with the first element as pivot.
- `comparison.py` – Compares the performance of Randomized vs. Deterministic Quicksort on various input types.
- `hash_table_chaining.py` – Implements a Hash Table using chaining to resolve collisions.
- `hash_test.py` – Demonstrates insert, search, and delete operations on the hash table.
- `Assignment 3: Understanding Algorithm Efficiency and Scalability` – Final report following APA format with theoretical analysis and runtime results.

---

## ▶️ How to Run

### 1. Sorting Algorithm Comparison

```bash
python comparison.py
```

This will execute Randomized and Deterministic Quicksort on:
- Random arrays
- Sorted arrays
- Reverse-sorted arrays
- Arrays with repeated elements

### 2. Hash Table Demonstration

```bash
python hash_test.py
```

This will:
- Insert key-value pairs (`"apple"`, `"banana"`, `"grape"`)
- Search for `"banana"` (should return 20)
- Delete `"banana"` and search again (should return None)

---

## 📊 Summary of Results

### Sorting Performance (Selected Results)

| Input Type | Size | Randomized (s) | Deterministic (s) | Observation |
|------------|------|----------------|--------------------|-------------|
| Random     | 1000 | 0.00503        | 0.0062             | Similar     |
| Sorted     | 2000 | 0.00899        | 0.17881            | Randomized faster |
| Reverse    | 5000 | 0.01002        | 0.26263            | Randomized faster |
| Duplicates | 1000 | 0.00000        | 0.00000            | Equal       |

### Hash Table Operations
- ✅ `Insert`: Successfully inserts key-value pairs
- 🔍 `Search`: Finds "banana" = 20
- ❌ `Delete`: Removes "banana", then search returns None

---

## 🧠 Key Learnings

- **Randomized Quicksort** avoids worst-case scenarios and performs well even on sorted or duplicate-heavy inputs.
- **Hashing with chaining** provides expected constant time for key operations, handling collisions effectively.
- Choosing the right algorithm for the data and scenario is critical for performance.

---

## 📌 Submission

This repository includes all required components:
- Python implementations
- Comparison scripts
- Detailed APA report
- This README

---

Developed by Bhawesh for Assignment 3: Understanding Algorithm Efficiency and Scalability
