"""this function will take an input from the user and convert it into an encoded message,
it will also generate a key for the user to use to decode the message"""
import string as st
import random
from correction import correction_cal, correction_cal2

class Zeta:
    def __init__(self, msg, psswrd):#allows for input of the message
        self.msg = msg
        self.psswrd = psswrd

    def encoder(self):#function which generates a random number as the encryption key and scrambles the message
        n = random.randint(1,26)
        Alpha = list(st.ascii_lowercase) #list of the alphabet to encode the message in substitution cypher
        msg_list = list(self.msg)
        encoded_msg = "" # where the encoded message will be written

        for m in range(len(msg_list)):
            for l in range(len(Alpha)):
                if Alpha[l] == msg_list[m]:
                    if l + n > 25:#checks if correction is needed
                        encoded_msg = encoded_msg + str(Alpha[correction_cal(l, n)])#applies correction function
                    else:
                        encoded_msg =  encoded_msg + str(Alpha[l + n]) # encodes the message using substitution cypher
                    continue

        print("your message is " + self.msg, "the encoded message is " + encoded_msg, "your key is " + str(n))
        return n, encoded_msg

    def decoder(self):#function to decode the coded message
        encrpt_list = list(self.msg)# converts message we are trying to decode into a list
        key = int(self.psswrd)
        Alpha = list(st.ascii_lowercase)
        decoded_msg = ""

        for m in range(len(encrpt_list)):
            for l in range(len(Alpha)):
                if Alpha[l] == encrpt_list[m]:
                    if l - key < 0:#checks if correction is needed
                        decoded_msg = decoded_msg + str(Alpha[correction_cal2(l, key)])#applies correction function
                    else:
                        decoded_msg =  decoded_msg + str(Alpha[l - key]) # decodes the message using substitution cypher
                    continue
        print("Your decoded message is " + decoded_msg)
        return decoded_msg

beta = Zeta("danilo",8)
print(beta.encoder())
