encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
t = list(encrypted_message)

for i in range(len(t)):
    if i %2 == 1:
        temp = encrypted_message[i]
        temp2 = encrypted_message[-i - 1]
        t[i] = temp2
        t[-i-1] = temp
print(''.join(t))