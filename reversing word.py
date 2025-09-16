# Reverse Words in a String

# Problem: Write a function to reverse the order of words in a given string.
# Testcase 1:
# Input: "hello world"
# Output: "world hello"
word = "hello world"
star_word= ""
end_word = ""
for i in word:
    if i != " ":
        star_word += i
    else:
        end_word = star_word + end_word
        star_word = ""  
if star_word != " ":
    end_word = star_word + " "+ end_word
print(end_word)