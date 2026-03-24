# Tuples & Sets — Revision Sheet (Day 5)

---

## TUPLES — Key Concepts

- **Immutable** — once created, cannot change elements
- **Creating:** `t = (1, 2, 3)` | Single element: `t = (5,)` ← comma required, `(5)` is just an integer
- **Indexing/slicing works** same as lists: `t[0]`, `t[-1]`, `t[0:2]`
- **Cannot do:** `t[0] = 10` ❌ | No `.append()`, `.pop()`, `.insert()`, `.remove()`
- **Unpacking:** `a, b, c = (10, 20, 30)` → a=10, b=20, c=30
- **Tuples can be dictionary keys. Lists cannot.** (Because tuples are hashable, lists are not)

### Hashable = Unchangeable = Can Be a Dict Key

Python needs a fixed "locker number" (hash) for dict keys. If the object can change, the locker number changes and everything breaks. So:

- ✅ Hashable (can be key): `int`, `str`, `tuple`
- ❌ Unhashable (can't be key): `list`, `dict`, `set`

---

## SETS — Key Concepts

- **Unordered** — no indexing (`s[0]` ❌), no guaranteed order
- **Unique elements only** — duplicates auto-removed
- **Creating:** `s = {1, 2, 3}` | Empty set: `s = set()` ← NOT `{}` (that's an empty dict!)
- **From list:** `set([1, 2, 2, 3])` → `{1, 2, 3}`

### Methods
| Method | What it does |
|--------|-------------|
| `s.add(4)` | Add element |
| `s.remove(2)` | Remove — ERROR if missing |
| `s.discard(2)` | Remove — NO error if missing |

### Operations
| Operation | Syntax | Result |
|-----------|--------|--------|
| Union | `a \| b` | Everything from both |
| Intersection | `a & b` | Only common elements |
| Difference | `a - b` | In `a` but not in `b` |

### Killer Feature: O(1) Lookup
- `x in my_list` → O(n) slow
- `x in my_set` → O(1) fast
- **When you need fast lookups, convert to set**

---

## When To Use What

| Structure | Use when... |
|-----------|------------|
| **List** | Ordered, duplicates OK, need indexing |
| **Tuple** | Ordered, immutable, need as dict key |
| **Set** | Unordered, unique only, fast `in` checks |
| **Dict** | Key-value pairs |

---

## Problems & What I Got Wrong

### Problem 1: List Intersection Using Sets

**Task:** Two lists → list of common elements, no duplicates.

```python
def intersec(lst1, lst2):
    return list(set(lst1) & set(lst2))
```

✅ Got it first try. One-liner using `set()` and `&`.

---

### Problem 2: Remove Duplicates Preserving Order

**Task:** Remove duplicates from list, keep first occurrence, maintain order.

```python
def rem(lst):
    res = []
    seen = {}
    for num in lst:
        if num not in seen:
            res.append(num)
            seen[num] = True
    return res
```

**Mistakes I made:**
1. ❌ First tried `return list(set(lst))` — **sets don't preserve order.** `list(set(...))` scrambles the order.
2. ❌ Then tried counting with `.get()` and returning `set(seen)` — **overcomplicating it.** Don't need to count anything, just need seen/not seen.
3. ❌ Then started building logic with `seen = {}` but forgot to build a `res` list — **always need a result container.**

**Pattern:** Loop → check `if num not in seen` → add to result + mark seen → skip if already seen. Same pattern as string duplicate removal.

**Cleaner version with set:**
```python
seen = set()
# use seen.add(num) instead of seen[num] = True
```

---

### Problem 3: Tuple as Dictionary Key

**Task:** List of `(coordinate_tuple, label)` pairs → dict mapping coordinate to label. Last label wins if coordinate repeats.

```python
def cor(lst):
    d = {}
    for cord, label in lst:
        d[cord] = label
    return d
```

✅ Got it after understanding the input format. Key insight: tuples are hashable so `(1, 2)` works as a dict key. Overwriting automatically handles "last wins".

**What confused me:** Didn't understand the input format at first. The input is a list where each item is `((x, y), "label")` — a tuple inside a tuple.

---

### Problem 4: Unique Characters Across Strings

**Task:** List of strings → count of characters that appear in ALL strings.

```python
def coun(lst):
    com = set(lst[0])
    for s in lst[1:]:
        com = com & set(s)
    return len(com)
```

**Mistake I made:**
- ❌ Started with anagram pattern (`"".join(sorted(word))`) — **wrong problem.** This isn't grouping, it's finding common characters across all strings.

**Pattern:** Start with `set(first_string)`, loop through rest, keep intersecting with `&`. What's left is characters common to ALL strings.

---

### Problem 5: Find Duplicates Using Two Sets

**Task:** List of integers → list of elements that appear more than once.

```python
def dupl(lst):
    seen = set()
    dup = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
        else:
            dup.add(num)
    return list(dup)
```

**Mistakes I made:**
1. ❌ Tried building a unique list and doing `set(original) - set(unique)` — **both sets have same unique elements, difference is always empty.** Logic was fundamentally wrong.
2. ❌ Used `list[...]` with square brackets — **`list()` is a function, use parentheses.** Same mistake as `len[word]` from earlier.

**Pattern:** Two sets — `seen` tracks everything encountered, `dup` collects items seen more than once. If `num in seen` → it's a duplicate, add to `dup`.

**Remember:** Returned `set()` instead of `[]` for empty case because forgot to wrap in `list()`. Always `return list(dup)` if problem asks for a list.

---

## Patterns Summary

| Pattern | When to use |
|---------|------------|
| `set(a) & set(b)` | Find common elements between collections |
| `seen` set + result list | Remove duplicates while keeping order |
| `set(string)` per string + `&` loop | Find characters/elements common to ALL items |
| Two sets: `seen` + `dup` | Find elements that appear more than once |
| Tuple as dict key | When you need a list-like thing as a key (coordinates, pairs) |

---

## My Recurring Mistakes To Watch

- **`list[]` instead of `list()`** — list is a function, use parentheses
- **Using `set()` when order matters** — sets lose order, use seen-set + result-list pattern
- **Jumping to wrong pattern** — read the problem, don't auto-pilot to anagrams/counting
- **Forgetting to build a result container** — if you need to return something, create `res = []` early
- **Returning set when list is asked** — wrap with `list()`
