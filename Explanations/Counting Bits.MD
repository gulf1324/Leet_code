### Bit Counting Solution
[Counting Bits.py](../Solutions/Counting%20Bits.py)

### Example: `n = 6`
- Output : `[0, 1, 1, 2, 1, 2, 2]`
  - 0 = `0b0` → 0 ones
  - 1 = `0b1` → 1 one
  - 2 = `0b10` → 1 one
  - 3 = `0b11` → 2 ones
  - 4 = `0b100` → 1 one
  - 5 = `0b101` → 2 ones
  - 6 = `0b110` → 2 ones

### Binary-Level Explanation
1. **Even Numbers (`i % 2 == 0`)**:
   - An even number’s binary is like shifting a smaller number left by 1 (dividing by 2 shifts right).
   - Example: 
     - 6 = `0b110` = 3 × 2.
     - 3 = `0b11`.
     - Shifting `0b11` left (or dividing 6 by 2) shows the same number of 1s.
   - So, `count(6) = count(6 // 2) = count(3)`.
   - General rule: For even `i`, the number of 1s equals the number of 1s in `i // 2`.

2. **Odd Numbers (`i % 2 != 0`)**:
   - An odd number is always 1 more than the previous (even) number.
   - Example:
     - 5 = `0b101`.
     - 4 = `0b100`.
     - 5 = 4 + 1, adding a 1-bit at the least significant position.
   - So, `count(5) = count(4) + 1`.
   - General rule: For odd `i`, the number of 1s is the previous number’s count (`res[-1]`) plus 1.

3. **Binary Pattern**:
   - Even numbers have a 0 in the least significant bit (LSB): `i = ...0`.
   - Odd numbers have a 1 in the LSB: `i = ...1`.
   - Dividing an even number by 2 (`i // 2`) strips the trailing 0, preserving the 1-bit count.
   - Adding 1 to an even number (making it odd) adds a 1-bit to the count.

### Efficiency
- **Time Complexity**: O(n) — one pass from 1 to n.
- **Space Complexity**: O(n) — storing the result list.