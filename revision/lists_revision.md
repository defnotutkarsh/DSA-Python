# LISTS REVISION SHEET — DAY 3
**Utkarsh | DSA Grind | Read this before every session**

---

## KEY PATTERNS TO REMEMBER

| Pattern | When to Use | Template |
|---------|-------------|----------|
| **seen dict (True/False)** | Duplicates, membership | `seen = {}` → `if num not in seen: seen[num] = True` |
| **seen dict (value: index)** | Two Sum, find pairs | `need = target - num` → `if need in seen: return [seen[need], i]` → `seen[lst[i]] = i` |
| **Two Pointers (i, j)** | Merge sorted lists | `while i < len(a) and j < len(b):` compare and move |
| **Two Variables (first, second)** | Second largest, top-2 | `first = lst[0], second = None` track both in one loop |
| **Two Lists (separate + combine)** | Move zeroes, filter | `group_a = []`, `group_b = []`, combine at end |
| **Slicing** | Rotation, remove element | `lst[-k:] + lst[:-k]` or `lst[:i] + lst[i+1:]` |
| **Math Trick** | Missing number | `expected = n*(n+1)//2`, return `expected - actual_sum` |

---

## YOUR COMMON MISTAKES (STOP MAKING THESE)

| # | Mistake | Why It's Wrong | Fix |
|---|---------|---------------|-----|
| 1 | `lst = lst.append(x)` | append() returns None. lst becomes None. | `lst.append(x)` — no assignment |
| 2 | `max_val = 0` for finding max | Fails with all negatives. `[-5,-2,-8]` returns 0. | `max_val = lst[0]` — init to first element |
| 3 | Forgetting empty list check | `lst[0]` on `[]` crashes with IndexError | `if len(lst)==0: return None` |
| 4 | `for num in seen` instead of `lst` | seen starts empty. Loop runs 0 times. | `for num in lst` |
| 5 | `lst[i] = i` instead of `seen[lst[i]] = i` | Overwrites list element. Doesn't store in dict. | `seen[lst[i]] = i` |
| 6 | Incrementing wrong pointer in 2-pointer | Appended lst2[j] but did i += 1 | If you use lst2[j], increment j, not i |
| 7 | `fist` instead of `first` | Typo creates new variable. Original unchanged. | READ YOUR CODE before running |
| 8 | Nested for loops for merge sorted | Gives every combination. Not merging. | Use while loop with two pointers |
| 9 | Not deleting from seen after match | Duplicates in result. `[2,2]` instead of `[2]` | `del seen[num]` after appending |
| 10 | Using `str` or `sum` as variable names | Shadows Python built-in functions | Use `total`, `result`, `expected` instead |

---

## PROBLEM-BY-PROBLEM BREAKDOWN

---

### P1: Reverse a List
**Pattern:** Loop backwards with `range(len-1, -1, -1)`, append each element

```python
def reverse_list(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result
```

🔴 **Your Bug:** Used `lst + lst[i]` — can't add list + int
🟢 **Fix:** Use `append()` or wrap in list: `[lst[i]]`

---

### P2: Find Maximum
**Pattern:** Init to lst[0], loop and compare. Handle empty list first.

```python
def find_max(lst):
    if len(lst) == 0:
        return None
    no = lst[0]
    for i in range(len(lst)):
        if lst[i] > no:
            no = lst[i]
    return no
```

🔴 **Your Bug:** Initialized to -10000000. Forgot empty list check.
🟢 **Fix:** Always init to lst[0]. Always check empty first.

---

### P3: Remove Duplicates
**Pattern:** seen dict + result list. If not seen, append and mark.

```python
def remove_dupes(lst):
    seen = {}
    res = []
    for num in lst:
        if num not in seen:
            res.append(num)
        seen[num] = True
    return res
```

🔴 **Your Bug:** Wrote `for num in seen` — loops over empty dict, runs 0 times.
🟢 **Fix:** Loop over `lst`, not `seen`.

---

### P4: Two Sum
**Pattern:** seen = {value: index}. For each num, check if (target - num) exists in seen.

```python
def two_sum(lst, target):
    seen = {}
    for i in range(len(lst)):
        need = target - lst[i]
        if need in seen:
            return [seen[need], i]
        else:
            seen[lst[i]] = i
```

🔴 **Your Bug:** Only appended current index i, didn't store anything in seen.
🟢 **Fix:** Return `[seen[need], i]`. Store `seen[lst[i]] = i` in else block.

---

### P5: Rotate List
**Pattern:** Slicing — `lst[-k:] + lst[:-k]`

```python
def rotate_list(lst, k):
    if len(lst) == 0:
        return []
    return lst[-k:] + lst[:-k]
```

🔴 **Your Bug:** Tried to use a loop — unnecessary.
🟢 **Fix:** One line with slicing. Last k elements + rest.

---

### P6: Second Largest
**Pattern:** Track first and second. When num > first, second gets old first.

```python
def second_largest(lst):
    if len(lst) < 2:
        return None
    first = lst[0]
    second = None
    for i in range(len(lst)):
        if lst[i] > first:
            second = first
            first = lst[i]
        elif lst[i] != first and (second is None or lst[i] > second):
            second = lst[i]
    return second
```

🔴 **Your Bug:** Copied `float('-inf')` from GPT. Forgot `!= first` check. Typo: `fist`.
🟢 **Fix:** Use None for second. Always check `!= first` in elif. Read your code.

---

### P7: Move Zeroes to End
**Pattern:** Two lists: non-zero and zero. Combine at end.

```python
def move_zeroes(lst):
    zer = []
    nonzer = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zer.append(lst[i])
        else:
            nonzer.append(lst[i])
    return nonzer + zer
```

🔴 **Your Bug:** Tried to use dictionary — overcomplicated.
🟢 **Fix:** Two lists, one if/else, concatenate. Simple.

---

### P8: Count Frequency
**Pattern:** Dict with element as key, count as value.

```python
def count_freq(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
```

🔴 **Your Bug:** Said "i forgot" — but wrote it correctly when pushed.
🟢 **Fix:** You know this. Stop doubting yourself.

---

### P9: Merge Two Sorted Lists
**Pattern:** Two pointers i,j. While loop. Compare, append smaller, move that pointer.

```python
def merge_sorted(lst1, lst2):
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            result.append(lst2[j])
            j += 1
        else:
            result.append(lst1[i])
            i += 1
    result += lst1[i:]
    result += lst2[j:]
    return result
```

🔴 **Your Bug:** Used nested for loops. Swapped i and j increments. While condition checked len() instead of pointer.
🟢 **Fix:** WHILE loop not FOR. If you append lst2[j], increment j. Check pointer < len.

---

### P10: Intersection
**Pattern:** Put lst1 in seen dict. Loop lst2, check membership. Del after match.

```python
def intersection(lst1, lst2):
    seen = {}
    res = []
    for num in lst1:
        seen[num] = True
    for num in lst2:
        if num in seen:
            res.append(num)
            del seen[num]
    return res
```

🔴 **Your Bug:** Used two dicts with counting. Got duplicates without del.
🟢 **Fix:** One dict. `del seen[num]` after match to prevent duplicates.

---

### P11: Has Pair (Two Sum → Bool)
**Pattern:** Same as two sum but return True/False.

```python
def has_pair(lst, target):
    seen = {}
    for i in range(len(lst)):
        need = target - lst[i]
        if need in seen:
            return True
        else:
            seen[lst[i]] = i
    return False
```

🔴 **Your Bug:** Wrote `lst[i] = i` instead of `seen[lst[i]] = i`.
🟢 **Fix:** Store in `seen`, not in `lst`.

---

### P12: Find Missing Number
**Pattern:** Math — expected sum - actual sum = missing number.

```python
def find_missing(lst):
    n = len(lst)
    expected = n * (n + 1) // 2
    actual = 0
    for num in lst:
        actual += num
    return expected - actual
```

🔴 **Your Bug:** Used `sum` as variable name.
🟢 **Fix:** Use `expected`/`actual`. Don't shadow built-ins.

---

## BEFORE EVERY SESSION — ASK YOURSELF:

1. Did I handle the empty list case?
2. Did I init to `lst[0]` instead of 0 or some random number?
3. Am I looping over the RIGHT variable (`lst`, not `seen`)?
4. Am I incrementing the RIGHT pointer?
5. Am I storing in `seen`, not overwriting `lst`?
6. Did I actually RUN the code before pasting?
7. Did I use `str`/`sum`/`list` as variable names? (DON'T)
