# rle-encode.py

def rle_encode(data):
    encoding = ""
    prev_char = ""
    count = 1

    if not data: return ''

    for char in data:
        # if the current char and 
        # prev char don't match....
        if char != prev_char:

            # ... then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # or increment the counter
            # if the characters do match
            count += 1
    else:
        # finish off the encoding
        encoding += str(count) + prev_char
        return encoding

# if __name__ == '__main__':
encoded_value = rle_encode('SSSSSSSSSSsAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBB')
print("The encoded value is : ", encoded_value)