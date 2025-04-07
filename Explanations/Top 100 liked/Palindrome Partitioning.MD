Code: [Palindrome partitioning.py](../../Solutions/Top%20100%20liked/Palindrome%20Partitioning.py)
# Example : 
```
s = "aab"
```

```python
dfs("aab", [])
│
├── s[:1] = "a" is palindrome → dfs("ab", ["a"])
│   ├── s[:1] = "a" is palindrome → dfs("b", ["a", "a"])
│   │   └── s[:1] = "b" is palindrome → dfs("", ["a", "a", "b"])
│   │      └── [] → append ["a", "a", "b"]
│   └── s[:2] = "ab" → not a palindrome → skip
│
├── s[:2] = "aa" is palindrome → dfs("b", ["aa"])
│   ├── s[:1] = "b" is palindrome → dfs("", ["aa", "b"])
│   │   └── [] → append ["aa", "b"]
│
└── s[:3] = "aab" → not a palindrome → skip
```