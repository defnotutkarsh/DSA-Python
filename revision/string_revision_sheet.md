# STRING PROBLEMS REVISION SHEET - UTKARSH

---

## KEY CONCEPTS TO REMEMBER

### 1. Strings are IMMUTABLE
```python
s = "hello"
s[0] = "X"      # ERROR — can't modify
s = s.lower()   # CORRECT — creates NEW string, reassign
```
**Your mistake:** Wrote `s.lower()` without assigning. Always do `s = s.lower()`

---

### 2. String Indexing
```python
s = "hello"
s[0]   # "h" (first)
s[4]   # "o" (last)
s[-1]  # "o" (last — shortcut)
s[5]   # ERROR — doesn't exist
```
**Rule:** Last valid index = `len(s) - 1`

---

### 3. range(start, stop, step)
```python
range(5)           # 0, 1, 2, 3, 4
range(4, -1, -1)   # 4, 3, 2, 1, 0 (for reverse)
range(1, 4)        # 1, 2, 3 (stops BEFORE 4)
```
**Your mistake:** Used `range(len(s), 1, -1)` — starts at invalid index, misses 0

---

### 4. Slicing s[start:end]
```python
s = "hello"
s[0:2]   # "he" (index 0, 1 — stops BEFORE 2)
s[1:4]   # "ell"
s[0:5]   # "hello" (full string)
```
**Rule:** End index is exclusive (not included)

---

### 5. Dictionaries
```python
d = {}              # empty
d["a"] = 1          # add key
d["a"] = d["a"] + 1 # update
"a" in d            # True (check if exists)
"x" in d            # False
```

---

### 6. Don't use `str` as variable name
```python
str = "hello"    # BAD — overwrites built-in
result = "hello" # GOOD
```

---

### 7. append() modifies in place
```python
res = []
res.append("a")       # CORRECT
res = res.append("a") # WRONG — res becomes None
```

---

## PROBLEM 1: REVERSE STRING

**Task:** `reverse_string("hello")` → `"olleh"`

**Logic:**
- Loop from last index to 0
- Add each character to result

```python
def reverse_string(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result = result + s[i]
    return result
```

**Your mistakes:**
- Used `range(len(s), 1, -1)` — wrong indices
- Put `return` inside loop — exits after first char

---

## PROBLEM 2: PALINDROME CHECK

**Task:** `is_palindrome("madam")` → `True`

**Logic:** Reverse and compare

```python
def is_palindrome(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result = result + s[i]
    return result == s
```

**Your mistake:** Named function `reverse()` instead of `is_palindrome()`

---

## PROBLEM 3: COUNT VOWELS

**Task:** `count_vowels("APPLE")` → `2` (case-insensitive)

**Logic:**
- Convert to lowercase FIRST
- Loop through, check if char in "aeiou"

```python
def count_vowels(s):
    s = s.lower()          # DON'T FORGET THIS
    count = 0
    vowels = "aeiou"
    for char in s:
        if char in vowels:
            count += 1
    return count
```

**Your mistake:** Wrote `s.lower()` without `s = `

---

## PROBLEM 4: COUNT WORDS

**Task:** `count_words("I love Python")` → `3`

**Logic:** Split and count

```python
def count_words(s):
    return len(s.split())
```

**Key concept:**
```python
"hello world".split()  # ["hello", "world"]
"".split()             # [] (empty list)
len([])                # 0
```

**Your mistake:** Counted spaces and added 1 — fails on empty string

---

## PROBLEM 5: FIRST NON-REPEATING CHARACTER

**Task:** `first_unique("aabbcdd")` → `"c"`

**Logic:**
1. Count all characters (dictionary)
2. Loop again, return first with count == 1
3. If none, return `""`

```python
def first_unique(s):
    count = {}
    for char in s:
        if char in count:
            count[char] = count[char] + 1
        else:
            count[char] = 1
    for char in s:
        if count[char] == 1:
            return char
    return ""               # DON'T FORGET THIS
```

**Your mistake:** Forgot `return ""` at end — returned `None`

---

## PROBLEM 6: REMOVE DUPLICATES

**Task:** `remove_duplicates("hello")` → `"helo"` (keep first occurrence)

**Logic:**
- Use `seen` dictionary to track what you've added
- If not seen, add to result AND mark as seen

```python
def remove_duplicates(s):
    seen = {}
    result = ""
    for char in s:
        if char not in seen:
            result = result + char
            seen[char] = True      # MARK AS SEEN
    return result
```

**Your mistakes:**
- Looped through `seen` instead of `s` — `seen` starts empty!
- Forgot `seen[char] = True` — never remembered anything

---

## PROBLEM 7: ANAGRAM CHECK

**Task:** `is_anagram("listen", "silent")` → `True`

**Logic:**
- Count characters in both strings
- Compare dictionaries

```python
def is_anagram(s1, s2):
    count1 = {}
    count2 = {}
    for char in s1:
        if char in count1:
            count1[char] = count1[char] + 1
        else:
            count1[char] = 1
    for char in s2:
        if char in count2:
            count2[char] = count2[char] + 1
        else:
            count2[char] = 1
    return count1 == count2
```

**No major mistakes here — you got it!**

---

## PROBLEM 8: ALL SUBSTRINGS

**Task:** `substrings("abc")` → `["a", "ab", "abc", "b", "bc", "c"]`

**Logic:**
- Outer loop: start index
- Inner loop: end index (start+1 to len+1)
- Slice and append

```python
def substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            result.append(s[i:j])
    return result
```

**Key understanding:**
- `i+1` because `s[0:0]` is empty (useless)
- `len(s)+1` because range stops BEFORE, need to include `len(s)`

**Your mistake:** `res = res.append(...)` — append returns None!

---

## PROBLEM 9: STRING COMPRESSION (CONSECUTIVE)

**Task:** `compress("aaabbc")` → `"a3b2c1"` (counts consecutive characters)

**Logic:**
- Track current character and its count
- When character changes, add to result, reset count
- Don't forget the last group at the end

```python
def compress(s):
    current = s[0]
    count = 1
    res = ""
    for i in range(1, len(s)):
        if s[i] == current:
            count = count + 1
        elif s[i] != current:
            res = res + current + str(count)
            count = 1
            current = s[i]
    return res + current + str(count)
```

**Key concepts:**
- `str(3)` converts integer to string — can't do `"a" + 3`
- Final `return res + current + str(count)` adds the last group (loop doesn't catch it)

**Walk through "aaabbc":**
| i | s[i] | current | count | res |
|---|------|---------|-------|-----|
| start | - | "a" | 1 | "" |
| 1 | "a" | "a" | 2 | "" |
| 2 | "a" | "a" | 3 | "" |
| 3 | "b" | "b" | 1 | "a3" |
| 4 | "b" | "b" | 2 | "a3" |
| 5 | "c" | "c" | 1 | "a3b2" |
| end | - | - | - | "a3b2c1" |

**Edge case:** Empty string will crash (s[0] fails). Add check if needed.

---

## PROBLEM 10: LONGEST WORD

**Task:** `longest_word("I love Python")` → `"Python"`

**Logic:**
- Split into words
- Track longest

```python
def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
```

**No mistakes — you nailed it!**

---

## QUICK REFERENCE TABLE

| Problem | Key Technique | Watch Out For |
|---------|---------------|---------------|
| Reverse | `range(len-1, -1, -1)` | Wrong range bounds |
| Palindrome | Reverse + compare | — |
| Count vowels | `.lower()` + check | `s = s.lower()` not `s.lower()` |
| Count words | `.split()` + `len()` | — |
| First unique | Count dict → find first with 1 | `return ""` at end |
| Remove dupes | `seen` dict + `not in` | Loop through `s`, not `seen` |
| Anagram | Two count dicts → compare | — |
| Substrings | Nested loops + slice | `append()` not `= append()` |
| Compress | Count dict → build string | `str()` to convert int |
| Longest word | `.split()` + track max | — |

---

## COMMON MISTAKES CHECKLIST

Before submitting, ask yourself:

- [ ] Did I run it with all test cases?
- [ ] Is my `return` outside the loop?
- [ ] Did I use `s = s.lower()` (not just `s.lower()`)?
- [ ] Did I forget `return ""` for edge cases?
- [ ] Am I looping through the right thing?
- [ ] Did I use `append()` without assigning to a variable?
- [ ] Is my variable name NOT `str`?

---

**NEXT UP: LISTS/ARRAYS**
problem 9 do it again