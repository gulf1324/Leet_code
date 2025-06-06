Code: [Coin Change.py](../../Solutions/Top%20100%20liked/Coin%20Change.py)
# Example : 
```python
coins = [1,2,5], amount = 5
# >>> 1
```

```python
dp = [0, ∞, ∞, ∞, ∞, ∞, ∞]

i = 1
├─ coin = 1 → dp[1] = min(dp[1], dp[1-1]+1) = min(6, 0+1) = 1
├─ coin = 2 → 건너뜀 (1 < 2)
└─ coin = 5 → 건너뜀 (1 < 5)
→ dp = [0, 1, ∞, ∞, ∞, ∞]

i = 2
├─ coin = 1 → dp[2] = min(6, dp[1]+1) = min(6, 1+1) = 2
├─ coin = 2 → dp[2] = min(2, dp[0]+1) = min(2, 0+1) = 1 ✅
└─ coin = 5 → 건너뜀
→ dp = [0, 1, 1, ∞, ∞, ∞]

i = 3
├─ coin = 1 → dp[3] = min(6, dp[2]+1) = min(6, 1+1) = 2
├─ coin = 2 → dp[3] = min(2, dp[1]+1) = min(2, 1+1) = 2
└─ coin = 5 → 건너뜀
→ dp = [0, 1, 1, 2, ∞, ∞]

i = 4
├─ coin = 1 → dp[4] = min(6, dp[3]+1) = min(6, 2+1) = 3
├─ coin = 2 → dp[4] = min(3, dp[2]+1) = min(3, 1+1) = 2 ✅
└─ coin = 5 → 건너뜀
→ dp = [0, 1, 1, 2, 2, ∞]

i = 5
├─ coin = 1 → dp[5] = min(6, dp[4]+1) = min(6, 2+1) = 3
├─ coin = 2 → dp[5] = min(3, dp[3]+1) = min(3, 2+1) = 3
└─ coin = 5 → dp[5] = min(3, dp[0]+1) = min(3, 0+1) = 1 ✅
→ dp = [0, 1, 1, 2, 2, 1]

```