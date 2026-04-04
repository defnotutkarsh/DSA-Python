# DSA + Python Revision Sheet
### Everything you learned. Read it, redo the problems, then resume daily DSA.

---

## DAY 1-2: STRINGS

### Concepts
- **Indexing:** `s[0]` = first, `s[-1]` = last
- **Slicing:** `s[start:end]` — end is exclusive. `s[1:4]` on `"hello"` → `"ell"`
- **Strings are immutable** — `s.lower()` returns a new string, doesn't change `s`. You need `s = s.lower()`
- **Concatenation:** `result = result + char` inside a loop to build strings
- **`range(start, stop, step)`** — for reverse: `range(len(s)-1, -1, -1)`

### Key Methods
```python
s.lower()       # lowercase
s.split()       # split by spaces → list of words
s.split(",")    # split by comma
len(s)          # length
"".join(lst)    # join list into string
sorted(s)       # returns sorted list of characters
```

### Problems You Solved (redo all from memory)

**1. Reverse a string** (no `[::-1]`)
```python
def reverse(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result = result + s[i]
    return result
```

**2. Palindrome check**
```python
def is_palindrome(s):
    s = s.lower()
    return s == reverse(s)
# Or compare s[i] with s[len(s)-1-i]
```

**3. Count vowels** (case-insensitive)
```python
def count_vowels(s):
    s = s.lower()
    count = 0
    for char in s:
        if char in "aeiou":
            count += 1
    return count
```

**4. First non-repeating character** (two-pass with dict)
```python
def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:          # second loop in ORIGINAL order
        if count[char] == 1:
            return char
    return None
```

**5. Remove duplicates** (keep first occurrence, preserve order)
```python
def remove_dupes(s):
    seen = {}
    result = ""
    for char in s:
        if char not in seen:
            result += char
            seen[char] = True
    return result
```

**6. Anagram check** (compare two frequency dicts)
```python
def is_anagram(s1, s2):
    def count(s):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        return d
    return count(s1) == count(s2)
```

**7. String compression** — `"aaabbc"` → `"a3b2c1"`
```python
def compress(s):
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        count = 0
        while i < len(s) and s[i] == char:
            count += 1
            i += 1
        result += char + str(count)
    return result
```

**8. All substrings** (nested loops + slicing)
```python
def substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            result.append(s[i:j])
    return result
```

**9. Longest word in sentence**
```python
def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
```

### Your Mistakes to Remember
- ❌ Used `str` as a variable name (shadows built-in)
- ❌ Forgot `s = s.lower()` — assignment is needed because strings are immutable
- ❌ Forgot `return ""` or `return None` at end of functions
- ❌ Used `len[s]` instead of `len(s)` — `len` is a function, use parentheses

---

## DAY 3: LISTS

### Concepts
- **Mutable** — can change elements in place: `lst[0] = 99`
- **Indexing/slicing** — same as strings
- **`append()` modifies in place** — do NOT assign: `lst.append(5)` ✅ | `lst = lst.append(5)` ❌ (gives None)

### Key Methods
```python
lst.append(val)     # add to end (in place)
lst.pop()           # remove & return last
lst.pop(i)          # remove & return at index i
lst.insert(i, val)  # insert at index i
lst.remove(val)     # remove first occurrence of val
lst.sort()          # sort in place
sorted(lst)         # returns new sorted list
lst.reverse()       # reverse in place
len(lst)
val in lst          # membership check
```

### Problems You Solved

**1. Reverse a list** (no `[::-1]`, no `.reverse()`)
```python
def reverse_list(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result
```

**2. Find max without `max()`**
```python
def find_max(lst):
    biggest = lst[0]
    for num in lst:
        if num > biggest:
            biggest = num
    return biggest
```

**3. Remove duplicates from list** (preserve order)
```python
def remove_dupes(lst):
    seen = {}
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen[item] = True
    return result
```

**4. Two Sum** (find two numbers that add to target, return indices)
```python
def two_sum(lst, target):
    seen = {}  # value → index
    for i in range(len(lst)):
        complement = target - lst[i]
        if complement in seen:
            return [seen[complement], i]
        seen[lst[i]] = i
    return []
```

**5. Rotate array** — shift elements left by k positions
```python
def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]
```

---

## DAY 4: DICTIONARIES

### Concepts
- **Key-value pairs:** `d = {"name": "Utkarsh", "age": 22}`
- **Access:** `d["name"]` or `d.get("name", default)`
- **`.get(key, default)`** — returns default if key missing (avoids KeyError)
- **Check membership:** `key in d`
- **Loop:** `for key in d:` or `for key, val in d.items():`

### Key Pattern: Frequency Counter
```python
count = {}
for item in sequence:
    count[item] = count.get(item, 0) + 1
```
This pattern appeared in: character count, word frequency, anagram check, first non-repeating.

### Problems You Solved

**1. Word frequency counter**
```python
def word_freq(s):
    words = s.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
```

**2. Two sum with dict** (same as lists section — dict is the trick)

**3. Group anagrams**
```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())
```

---

## DAY 5: TUPLES & SETS

### Tuples
- **Immutable** list. Create: `t = (1, 2, 3)` | Single element: `t = (5,)` ← comma required
- **Indexing/slicing works.** Cannot assign/append/pop.
- **Unpacking:** `a, b, c = (10, 20, 30)`
- **Can be dict keys** (because hashable). Lists cannot.

### Sets
- **Unordered, unique elements.** No indexing.
- **Create:** `s = {1, 2, 3}` | Empty: `s = set()` (NOT `{}`)
- **O(1) lookup:** `x in s` is fast

### Key Methods
```python
s.add(val)          # add element
s.discard(val)      # remove (no error if missing)
s.remove(val)       # remove (KeyError if missing)
s1 & s2             # intersection
s1 | s2             # union
s1 - s2             # difference (in s1 but not s2)
```

### Problems You Solved

**1. Tuple unpacking + swap**
```python
a, b = b, a  # Python swap using tuple unpacking
```

**2. Find duplicates** (two-set pattern)
```python
def find_dupes(lst):
    seen = set()
    dupes = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
        else:
            dupes.add(num)
    return dupes
```

**3. Set intersection across multiple lists**
```python
def common_elements(lists):
    result = set(lists[0])
    for lst in lists[1:]:
        result = result & set(lst)
    return result
```

### Key Insight
- **Hashable = immutable = can be dict key.** `int`, `str`, `tuple` = hashable. `list`, `dict`, `set` = NOT hashable.

---

## DAY 6: SORTING + LAMBDA + MAP/FILTER

### Lambda
- One-line anonymous function: `lambda x: x * 2`
- Same as: `def f(x): return x * 2`

### sorted() with key
```python
# Sort strings by length
sorted(words, key=lambda x: len(x))

# Sort tuples by second element
sorted(pairs, key=lambda x: x[1])

# Sort dicts by value
sorted(d.items(), key=lambda x: x[1])
```

### map() and filter()
```python
# map — apply function to every element
list(map(lambda x: x**2, [1,2,3]))     # [1, 4, 9]

# filter — keep elements where function returns True
list(filter(lambda x: x%2==0, [1,2,3,4]))  # [2, 4]
```
Always wrap with `list()` — `map()` and `filter()` return iterators, not lists.

### Problems You Solved

**1. Sort by length**
```python
def sort_by_length(lst):
    return sorted(lst, key=lambda x: len(x))
```

**2. Only even numbers using filter**
```python
def only_even(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
```

### Your Mistakes to Remember
- ❌ `len[x]` — len is a function, not a list. Use `len(x)` with parentheses.

---

## DAY 6-7: RECURSION

### Pattern
```python
def recursive_func(input):
    if base_case:       # smallest input, return directly
        return answer
    return combine(input[0], recursive_func(smaller_input))
```

### Problems You Solved

**1. Factorial**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

**2. Recursive sum of list**
```python
def rec_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + rec_sum(lst[1:])
```

**3. Recursive max** (you struggled then solved it)
```python
def recursive_max(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = recursive_max(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max
```

---

## DAY 7+: LIST COMPREHENSIONS

### Syntax
```python
# Transform every element
[expression for x in lst]

# Transform + filter
[expression for x in lst if condition]
```

### Examples
```python
[x**2 for x in [1,2,3,4]]              # [1, 4, 9, 16]
[x for x in [1,2,3,4,5] if x%2==0]    # [2, 4]
[word.upper() for word in words]        # uppercase all words
[x for x in lst if x > 0]              # positive numbers only
```

### Nested (for 2D)
```python
# Flatten [[1,2],[3,4]] → [1,2,3,4]
[item for row in matrix for item in row]
```

---

## REVISION CHECKLIST

Write each from scratch (no looking). Time yourself.

| # | Problem | Target Time |
|---|---------|-------------|
| 1 | Reverse a string (no [::-1]) | 1 min |
| 2 | Palindrome check | 1 min |
| 3 | Count vowels | 1 min |
| 4 | First non-repeating character | 2 min |
| 5 | Anagram check | 2 min |
| 6 | String compression | 3 min |
| 7 | Reverse a list (no built-ins) | 1 min |
| 8 | Find max without max() | 1 min |
| 9 | Two sum with dict | 3 min |
| 10 | Remove duplicates (preserve order) | 2 min |
| 11 | Group anagrams | 3 min |
| 12 | Find duplicates (two-set) | 2 min |
| 13 | Sort by length (lambda) | 1 min |
| 14 | Filter evens (filter + lambda) | 1 min |
| 15 | Recursive max | 2 min |
| 16 | List comprehension — squares | 30 sec |
| 17 | Flatten nested list (comprehension) | 1 min |

**If you can't do all 17 from memory in under 30 minutes total, you haven't revised enough.**

---

## COMMON MISTAKES (YOUR PATTERN)

1. **`len[x]` instead of `len(x)`** — len is a function, use parentheses
2. **`str` as variable name** — shadows the built-in, breaks `str()` later
3. **Forgetting `s = s.lower()`** — strings are immutable, methods return new strings
4. **`lst = lst.append(x)`** — append modifies in place, returns None
5. **Forgetting return at end** — function returns None by default
6. **Opening GPT when stuck** — think for 60 seconds first. You solved recursive_max after saying "idk" by just thinking.
