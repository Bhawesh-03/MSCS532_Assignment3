from hash_table_chaining import HashTable

ht = HashTable()
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("grape", 30)

print("Search 'banana':", ht.search("banana"))  # Output: 20
ht.delete("banana")
print("Search 'banana' after deletion:", ht.search("banana"))  # Output: None
