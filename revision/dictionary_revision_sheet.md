# DICTIONARY PROBLEMS REVISION SHEET - UTKARSH

---

## KEY CONCEPTS TO REMEMBER

### 1. Creating and using dictionaries
```python
d = {}              # empty dictionary
d["a"] = 1          # add key-value pair
d["a"] = d["a"] + 1 # update value
"a" in d            # True — check if key exists
del d["a"]          # delete a key
```

### 2. .get(key, default) — replaces your if/else counting
```python
# OLD WAY (works but long):
if char in d:
    d[char] = d[char] + 1
else:
    d[char] = 1

# NEW WAY (same thing, one line):
d[char] = d.get(char, 0) + 1
```
**How it works:** `d.get("a", 0)` means "give me value of `a`. If `a` doesn't exist, give me `0` instead of crashing."

### 3. .keys(), .values(), .items()
```python
d = {"a": 1, "b": 2, "c": 3}
d.keys()    # dict_keys(["a", "b", "c"])
d.values()  # dict_values([1, 2, 3])
d.items()   # dict_items([("a", 1), ("b", 2), ("c", 3)])
```
**`.items()` gives both key and value at once:**
```python
for key, value in d.items():
    print(key, value)
# Output: a 1, b 2, c 3
```

### 4. Dictionary comprehension
```python
squares = {x: x*x for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 5. "".join() — glues a list into a string
```python
sorted("eat")              # → ["a", "e", "t"] (list)
"".join(sorted("eat"))     # → "aet" (string)
"-".join(["a", "e", "t"])  # → "a-e-t"
```
**Why you need it:** Dictionary keys can't be lists. Sort a word, join it into a string, use that as the key.

---

## PROBLEM 1: WORD FREQUENCY FROM SENTENCE

**Task:** `freq("the cat and the dog")` → `{"the": 2, "cat": 1, "and": 1, "dog": 1}`

**Logic:**
- Split sentence into words with `.split()`
- Loop through words, count with `.get()`

```python
def freq(s):
    count = {}
    for word in s.split():
        count[word] = count.get(word, 0) + 1
    return count
```

**Your mistakes:**
- Wrote `count = {}` twice — sloppy but not a bug
- No major logic errors — you got this one clean

---

## PROBLEM 2: INVERT A DICTIONARY

**Task:** `invert({"a": 1, "b": 2, "c": 3})` → `{1: "a", 2: "b", 3: "c"}`

**Logic:**
- Loop with `.items()` to get key and value
- Build new dictionary with them swapped: `res[value] = key`

```python
def invert(d):
    res = {}
    for key, value in d.items():
        res[value] = key
    return res
```

**Your mistakes:**
- First attempt: did `key, value = value, key` — this swaps the **variables** but doesn't store them anywhere. Like picking up two objects, swapping hands, then dropping both on the floor. Nothing saved.
- Put `return` inside the loop — returned after first pair
- Returned `key, value` (a tuple) instead of `res` (a dictionary)

**Key lesson:** Swapping variables in place does nothing if you don't put the result into a container (dictionary, list, etc.)

---

## PROBLEM 3: GROUP ANAGRAMS

**Task:** `ana(["eat", "tea", "tan", "ate", "nat", "bat"])` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

**Logic:**
- Two words are anagrams if their sorted letters are the same
- For each word, create a key by sorting: `key = "".join(sorted(word))`
- Dictionary where key = sorted string, value = list of words with that key
- If key exists → append word to list
- If key doesn't exist → create new list with `[word]`
- Return `list(res.values())`

```python
def ana(lst):
    res = {}
    for word in lst:
        key = "".join(sorted(word))
        if key in res:
            res[key].append(word)
        else:
            res[key] = [word]
    return list(res.values())
```

**Line-by-line walkthrough for `["eat", "tea", "tan", "ate"]`:**

`word = "eat"` → `key = "aet"` → not in res → `res = {"aet": ["eat"]}`

`word = "tea"` → `key = "aet"` → in res → append → `res = {"aet": ["eat", "tea"]}`

`word = "tan"` → `key = "ant"` → not in res → `res = {"aet": ["eat", "tea"], "ant": ["tan"]}`

`word = "ate"` → `key = "aet"` → in res → append → `res = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}`

`return list(res.values())` → `[["eat", "tea", "ate"], ["tan"]]`

**Your mistakes:**
- First attempt: wrote `res = res.join(sorted)` — `.join()` is a string method, not a dictionary method. You confused which object has which method.
- Wrote `res[key] = word` instead of `res[key] = [word]` — stored a string instead of a list. When second anagram came and you tried `.append()`, it broke because you can't append to a string.

**Key lesson:** When dictionary values are lists, initialize with `[word]` (a list), not `word` (a string).

---

## PROBLEM 4: CHARACTER MAPPING

**Task:** `charmap("abc", "xyz")` → `{"a": "x", "b": "y", "c": "z"}`

**Logic:**
- One loop using index — same index for both strings
- `s1[i]` maps to `s2[i]`

```python
def charmap(s1, s2):
    dic = {}
    for i in range(len(s1)):
        dic[s1[i]] = s2[i]
    return dic
```

**Your mistakes:**
- Used two nested loops — you don't need to compare every char with every other char. Same position = same index = one loop.
- Wrote `s[i] = s[j]` instead of `dic[s1[i]] = s2[i]` — didn't use the dictionary at all

**Note:** If a character appears more than once in `s1` (like `"hello"`), the later mapping overwrites the earlier one. `l` at index 2 maps to `r`, but `l` at index 3 maps to `l` — final result has `"l": "l"`. That's how dictionaries work — duplicate keys get overwritten.

---

## PROBLEM 5: TWO SUM WITH DICTIONARY

**Task:** `twosum([2, 7, 11, 15], 9)` → `[0, 1]` (because 2+7=9)

**Logic:**
- For each number, calculate `need = target - nums[i]`
- Check if `need` is already in the dictionary
- If yes → found the pair, return both indices
- If no → store `nums[i]: i` in dictionary for future lookups

```python
def twosum(lst, target):
    seen = {}
    for i in range(len(lst)):
        need = target - lst[i]
        if need in seen:
            return [seen[need], i]
        else:
            seen[lst[i]] = i
```

**No major mistakes — you got this clean. Previous experience with two sum (nested loop version) helped.**

**Why this is better:** Nested loop version is O(n²). This dictionary version is O(n) — one pass. Interviews want this version.

---

## PROBLEM 6: INVERT DICTIONARY WITH DUPLICATE VALUES

**Task:** `invertfinalboss({"a": 1, "b": 2, "c": 1})` → `{1: ["a", "c"], 2: ["b"]}`

**Logic (same pattern as group anagrams):**
- Loop with `.items()`
- Use value as key in new dictionary
- If value already exists as key → append original key to list
- If not → create new list with `[key]`

```python
def invertfinalboss(d):
    res = {}
    for key, value in d.items():
        if value in res:
            res[value].append(key)
        else:
            res[value] = [key]
    return res
```

**Your mistakes:**
- First attempt: wrote `res[value] = key` then tried `res.append` — mixed up simple invert with grouped invert
- After being told "same as group anagrams" → got it correct

---

## PATTERNS TO REMEMBER

| Pattern | Used In | How It Works |
|---------|---------|-------------|
| `.get(key, 0) + 1` | Word frequency, any counting | One-line replacement for if/else counting |
| `.items()` loop | Invert dict, char mapping | Gives you both key and value at once |
| `"".join(sorted(word))` as key | Group anagrams | Sort letters → string → dictionary key |
| `complement = target - current` | Two sum | Check if complement already seen |
| Value as key, collect into list | Group anagrams, invert with dupes | `if key in res: append` else `res[key] = [item]` |

---

## COMMON MISTAKES CHECKLIST

Before submitting, ask yourself:

- [ ] Am I using `.join()` on a string, not a dictionary?
- [ ] Am I initializing list values as `[item]` not just `item`?
- [ ] Is my `return` outside the loop?
- [ ] Am I looping through the right thing?
- [ ] Did I actually store results in a container (dict/list), not just swap variables?
- [ ] Did I run it with all test cases?
- [ ] One loop or two? (Character mapping = one loop, not nested)

---

## ALSO FIXED THIS SESSION

### String Compression — CORRECTED APPROACH

**OLD (WRONG):** Dictionary counting. Breaks on `"aabbaac"` — groups all same chars together instead of tracking consecutive runs.

**NEW (CORRECT):** Two variables — `current` and `count`. Walk through string. When character changes, dump to result and reset.

```python
def compress(s):
    current = s[0]
    count = 1
    res = ""
    for i in range(1, len(s)):
        if s[i] == current:
            count = count + 1
        else:
            res = res + current + str(count)
            current = s[i]
            count = 1
    return res + current + str(count)
```

**Key lesson:** Dictionary counting ≠ consecutive run counting. If order matters, walk through the string.

---

**NEXT UP: TUPLES AND SETS**
