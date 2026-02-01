# list_tasks.py

# 1. Count Occurrences
def count_occurrences(lst, x):
    return lst.count(x)

# 2. Sum of Elements
def sum_elements(lst):
    return sum(lst)

# 3. Max Element
def max_element(lst):
    return max(lst)

# 4. Min Element
def min_element(lst):
    return min(lst)

# 5. Check Element
def check_element(lst, x):
    return x in lst

# 6. First Element
def first_element(lst):
    return lst[0] if lst else None

# 7. Last Element
def last_element(lst):
    return lst[-1] if lst else None

# 8. Slice List (first 3)
def slice_first_three(lst):
    return lst[:3]

# 9. Reverse List
def reverse_list(lst):
    return lst[::-1]

# 10. Sort List
def sort_list(lst):
    return sorted(lst)

# 11. Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))

# 12. Insert Element
def insert_element(lst, index, x):
    lst.insert(index, x)
    return lst

# 13. Index of Element
def index_of_element(lst, x):
    return lst.index(x) if x in lst else -1

# 14. Check for Empty List
def is_empty(lst):
    return len(lst) == 0

# 15. Count Even Numbers
def count_even(lst):
    return sum(1 for i in lst if i % 2 == 0)

# 16. Count Odd Numbers
def count_odd(lst):
    return sum(1 for i in lst if i % 2 != 0)

# 17. Concatenate Lists
def concatenate_lists(lst1, lst2):
    return lst1 + lst2

# 18. Find Sublist
def find_sublist(lst, sub):
    return any(lst[i:i+len(sub)] == sub for i in range(len(lst)))

# 19. Replace Element
def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst

# 20. Find Second Largest
def second_largest(lst):
    return sorted(set(lst))[-2]

# 21. Find Second Smallest
def second_smallest(lst):
    return sorted(set(lst))[1]

# 22. Filter Even Numbers
def filter_even(lst):
    return [i for i in lst if i % 2 == 0]

# 23. Filter Odd Numbers
def filter_odd(lst):
    return [i for i in lst if i % 2 != 0]

# 24. List Length
def list_length(lst):
    return len(lst)

# 25. Create a Copy
def copy_list(lst):
    return lst.copy()

# 26. Get Middle Element(s)
def middle_element(lst):
    n = len(lst)
    return lst[n//2] if n % 2 else lst[n//2 - 1:n//2 + 1]

# 27. Max of Sublist
def max_of_sublist(lst, start, end):
    return max(lst[start:end])

# 28. Min of Sublist
def min_of_sublist(lst, start, end):
    return min(lst[start:end])

# 29. Remove Element by Index
def remove_by_index(lst, i):
    if 0 <= i < len(lst):
        lst.pop(i)
    return lst

# 30. Check if List is Sorted
def is_sorted(lst):
    return lst == sorted(lst)

# 31. Repeat Elements
def repeat_elements(lst, n):
    return [x for x in lst for _ in range(n)]

# 32. Merge and Sort
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

# 33. Find All Indices
def find_all_indices(lst, x):
    return [i for i, v in enumerate(lst) if v == x]

# 34. Rotate List (right)
def rotate_list(lst, k):
    if not lst:
        return lst
    k %= len(lst)
    return lst[-k:] + lst[:-k]

# 35. Create Range List
def create_range(a, b):
    return list(range(a, b + 1))

# 36. Sum of Positive Numbers
def sum_positive(lst):
    return sum(i for i in lst if i > 0)

# 37. Sum of Negative Numbers
def sum_negative(lst):
    return sum(i for i in lst if i < 0)

# 38. Check Palindrome
def is_palindrome(lst):
    return lst == lst[::-1]

# 39. Create Nested List
def create_nested_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# 40. Unique Elements (Keep Order)
def unique_in_order(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

# set_tasks.py

# 1. Union of Sets
def union_sets(set1, set2):
    return set1 | set2

# 2. Intersection of Sets
def intersection_sets(set1, set2):
    return set1 & set2

# 3. Difference of Sets
def difference_sets(set1, set2):
    return set1 - set2

# 4. Check Subset
def is_subset(set1, set2):
    return set1.issubset(set2)

# 5. Check Element
def check_element(s, x):
    return x in s

# 6. Set Length
def set_length(s):
    return len(s)

# 7. Convert List to Set
def list_to_set(lst):
    return set(lst)

# 8. Remove Element
def remove_element(s, x):
    s.discard(x)   # x bo‘lmasa ham xato bermaydi
    return s

# 9. Clear Set
def clear_set(s):
    return set()

# 10. Check if Set is Empty
def is_set_empty(s):
    return len(s) == 0

# 11. Symmetric Difference
def symmetric_difference(set1, set2):
    return set1 ^ set2

# 12. Add Element
def add_element(s, x):
    s.add(x)
    return s

# 13. Pop Element
def pop_element(s):
    return s.pop() if s else None

# 14. Find Maximum
def max_in_set(s):
    return max(s)

# 15. Find Minimum
def min_in_set(s):
    return min(s)

# 16. Filter Even Numbers
def filter_even(s):
    return {i for i in s if i % 2 == 0}

# 17. Filter Odd Numbers
def filter_odd(s):
    return {i for i in s if i % 2 != 0}

# 18. Create a Set of a Range
def create_range_set(a, b):
    return set(range(a, b + 1))

# 19. Merge and Deduplicate
def merge_and_deduplicate(lst1, lst2):
    return set(lst1 + lst2)

# 20. Check Disjoint Sets
def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)

# 21. Remove Duplicates from a List
def remove_duplicates_from_list(lst):
    return list(set(lst))

# 22. Count Unique Elements
def count_unique_elements(lst):
    return len(set(lst))

# 23. Generate Random Set
import random
def generate_random_set(n, start, end):
    return set(random.randint(start, end) for _ in range(n))


# set_tasks.py

import random

# 1. Union of Sets
def union_sets(set1, set2):
    return set1 | set2

# 2. Intersection of Sets
def intersection_sets(set1, set2):
    return set1 & set2

# 3. Difference of Sets
def difference_sets(set1, set2):
    return set1 - set2

# 4. Check Subset
def check_subset(set1, set2):
    return set1.issubset(set2)

# 5. Check Element
def check_element(s, x):
    return x in s

# 6. Set Length
def set_length(s):
    return len(s)

# 7. Convert List to Set
def list_to_set(lst):
    return set(lst)

# 8. Remove Element
def remove_element(s, x):
    s.discard(x)   # agar element bo‘lmasa ham xato bermaydi
    return s

# 9. Clear Set
def clear_set(s):
    return set()

# 10. Check if Set is Empty
def is_set_empty(s):
    return len(s) == 0

# 11. Symmetric Difference
def symmetric_difference(set1, set2):
    return set1 ^ set2

# 12. Add Element
def add_element(s, x):
    s.add(x)
    return s

# 13. Pop Element
def pop_element(s):
    return s.pop() if s else None

# 14. Find Maximum
def find_max(s):
    return max(s)

# 15. Find Minimum
def find_min(s):
    return min(s)

# 16. Filter Even Numbers
def filter_even(s):
    return {i for i in s if i % 2 == 0}

# 17. Filter Odd Numbers
def filter_odd(s):
    return {i for i in s if i % 2 != 0}

# 18. Create a Set of a Range
def create_range_set(start, end):
    return set(range(start, end + 1))

# 19. Merge and Deduplicate
def merge_and_deduplicate(lst1, lst2):
    return set(lst1 + lst2)

# 20. Check Disjoint Sets
def check_disjoint(set1, set2):
    return set1.isdisjoint(set2)

# 21. Remove Duplicates from a List
def remove_duplicates_from_list(lst):
    return list(set(lst))

# 22. Count Unique Elements
def count_unique_elements(lst):
    return len(set(lst))

# 23. Generate Random Set
def generate_random_set(n, start, end):
    return set(random.randint(start, end) for _ in range(n))

# dict_tasks.py
from collections import defaultdict

# 1. Get Value
def get_value(d, key, default=None):
    return d.get(key, default)

# 2. Check Key
def check_key(d, key):
    return key in d

# 3. Count Keys
def count_keys(d):
    return len(d)

# 4. Get All Keys
def get_all_keys(d):
    return list(d.keys())

# 5. Get All Values
def get_all_values(d):
    return list(d.values())

# 6. Merge Dictionaries
def merge_dictionaries(d1, d2):
    return d1 | d2   # Python 3.9+

# 7. Remove Key
def remove_key(d, key):
    d.pop(key, None)
    return d

# 8. Clear Dictionary
def clear_dictionary():
    return {}

# 9. Check if Dictionary is Empty
def is_dict_empty(d):
    return len(d) == 0

# 10. Get Key-Value Pair
def get_key_value_pair(d, key):
    return (key, d[key]) if key in d else None

# 11. Update Value
def update_value(d, key, value):
    d[key] = value
    return d

# 12. Count Value Occurrences
def count_value_occurrences(d, value):
    return list(d.values()).count(value)

# 13. Invert Dictionary
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# 14. Find Keys with Value
def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

# 15. Create a Dictionary from Lists
def dict_from_lists(keys, values):
    return dict(zip(keys, values))

# 16. Check for Nested Dictionaries
def has_nested_dictionary(d):
    return any(isinstance(v, dict) for v in d.values())

# 17. Get Nested Value
def get_nested_value(d, outer_key, inner_key, default=None):
    return d.get(outer_key, {}).get(inner_key, default)

# 18. Create Default Dictionary
def create_default_dict(default_value):
    return defaultdict(lambda: default_value)

# 19. Count Unique Values
def count_unique_values(d):
    return len(set(d.values()))

# 20. Sort Dictionary by Key
def sort_dict_by_key(d):
    return dict(sorted(d.items()))

# 21. Sort Dictionary by Value
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# 22. Filter by Value
def filter_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

# 23. Check for Common Keys
def has_common_keys(d1, d2):
    return bool(set(d1.keys()) & set(d2.keys()))

# 24. Create Dictionary from Tuple
def dict_from_tuple(t):
    return dict(t)

# 25. Get the First Key-Value Pair
def get_first_item(d):
    return next(iter(d.items())) if d else None