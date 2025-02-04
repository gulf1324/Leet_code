##########################################################################
# Not a loop-wise algorithm
# -> more like for loop 
class Solution:
    def compress(self, chars: list[str]) -> int:
        read_i, write_i, count = 0,0,1
        char = ''

        while read_i <= len(chars) - 1:
            if char == chars[read_i]:
                count += 1
            else:
                write_i += len(char)
                write = char+(str(count) if count != 1 else '')
                for i in range(len(write)):
                    chars[write_i + i] = write[i]
                count = 1
                char = chars[read_i]
                write_i += len(write)-1
            read_i +=1
        write_i += len(char)
        write = char+(str(count) if count != 1 else '')
        for i in range(len(write)):
            chars[write_i + i] = write[i]

        return write_i+len(write)
##########################################################################
# Making the most out of while loops
class Solution:
    def compress(self, chars: list[str]) -> int:
        write_i = 0  
        read_i = 0  

        while read_i < len(chars):
            char = chars[read_i]
            count = 0

            # Count occurrences of the current character
            ######################################################
            while read_i < len(chars) and chars[read_i] == char: #
                read_i += 1                                      #
                count += 1                                       #
            ######################################################

            # Write the character
            chars[write_i] = char
            write_i += 1

            # Write the count (only if >1)
            if count > 1:
                for digit in str(count):
                    chars[write_i] = digit
                    write_i += 1
        return write_i                
##########################################################################

s = Solution()
print(s.compress(["a","b","b","c","c","c"])) 
# >>> 5 
#   chars == ['a', 'b', '2', 'c', '3', 'c']
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])) 
# >>> 4
#   chars == ['a', 'b', '1', '2', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']