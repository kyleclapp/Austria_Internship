from __future__ import absolute_import, division, print_function

import abc

import six

from cryptography import utils

##e = 5     n = 35     c=10     M= 5     d = 5 these are the values for the RSA  key from Assignment 1 and I will use these for the final project  

print("This is the final project for 3600U")

print("Please make a selection with the selection below to see demonstrate the corresponding encryption algorithm\n")     

print(" 1= RSA    2 = AES    3 = 3DES    4 = CAST-128(CAST5)    5 = RC4\n")

userinput = input("Please make a selecion\n\n")

print("Please choose the encryption mode that you would like to use, please note this only applies if you have selected \"AES\",  \"3DES\", or \"CAST-128(CAST5)\"\n\n")

print("Electronic Codebook (ECB) = 1\n    Cipher Block Chaining (CBC) = 2 \n    Cipher FeedBack Mode (CFB) = 3 \n     Output Feedback Mode (OFB) = 4  \n    Counter Mode (CTR) = 5\n")


encryption_input = input("Please make a selection corresponding to the mode of encryption you would like\n")







  
if userinput == "1":    

	print("You have selected RSA\n")
	
	
	import Crypto
	from Crypto.PublicKey import RSA
	from Crypto import Random
	import ast
	
	RSA_privatekey = RSA.generate(1024, randfunc=None ,  progress_func=None, e=5)
	RSA_publickey= RSA_privatekey.publickey()
	


	RSA_string_plaintext = input("Please enter text that you would like to encrypt\n\n\n")
	
	RSA_byte_plaintext = str.encode(RSA_string_plaintext)

	print(RSA_byte_plaintext, "\n\n\n")

	RSA_ciphertext = RSA_publickey.encrypt(RSA_byte_plaintext, 42)
	
	print(RSA_ciphertext)

	RSA_pfromc =  RSA_privatekey.decrypt(RSA_ciphertext)
	
	print(RSA_pfromc)


	######  This is the portion that I am having problems with 
	###### https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.PublicKey.RSA._RSAobj-class.html#keydata

	####This is the reference that I using, not sure if I am using it incorrectly though
	RSA_values = keydata() 
	print(RSA_values)

	#######
	
	

elif userinput == "2":

	import os
	from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import padding
	
	
	

	AES_plaintext = input("Please enter the ciphertext of your choice\n\n")


	print("\n")
#The following block of code does padding for the input
	AES_plaintext_bytes = AES_plaintext.encode()

	AES_padder = padding.PKCS7(128).padder()     #This creates the padding function, for AES this function pads the data to 128 bytes

	AES_padded_data = AES_padder.update(AES_plaintext_bytes)   #This pads the data



	AES_padded_data += AES_padder.finalize()    #This finalizes the padded data

	print(AES_padded_data, "\n\n")       #This prints the padded data


###The padding portion of the code is finished

###The following block of code encrypts the data

	###AES is almost working

	print("You have selected AES\n")
	AES_backend = default_backend()
	AES_key = os.urandom(32)
	AES_iv = os.urandom(16)
	AES_nonce = os.urandom(8)

#The following if statement determines what encryption mode the algorithm will use

	
	if encryption_input =="1":
		mode = modes.ECB()
		print("You have selected ECB")
	elif encryption_input =="2":
		mode = modes.CBC(AES_iv)
		print("You have selected CBC")
	elif encryption_input =="3":
		mode = modes.CFB(AES_iv)
		print("You have selected CFB")
	elif encryption_input =="4":
		mode = modes.OFB(AES_iv)
		print("You have selected OFB")
	elif encryption_input =="5":
		mode = modes.CTR(AES_nonce)
		print("You have selected CTR")
	else:
		print("Please input a number from 1-5")

##The if statement is finished 
##The following code will encrypt the data

	cipher = Cipher(algorithms.AES(AES_key), mode, backend=AES_backend)        #This line is commented out to test ECB
	AES_encryptor = cipher.encryptor()
	cipher_text = AES_encryptor.update(AES_padded_data) + AES_encryptor.finalize()
	AES_decryptor = cipher.decryptor()
	plaintext_from_ciphertext = AES_decryptor.update(cipher_text) + AES_decryptor.finalize()


##This prints the data to the users
	print("This is the key that was used to encrypt:", AES_key, "\n")
	print("This is the value of the Initization Vector that was used:", AES_iv, "\n")
	print("This is the cipher text: ",cipher_text, "\n")


########################################  This following code does the decryption of the data

	print("\nThis is the plaintext decoded from the plaintext: ",plaintext_from_ciphertext)



elif userinput == "3":     ##This is 3DES!!!!!!

	import os
	from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import padding
	


	

	TripleDES_plaintext = input("Please enter the ciphertext of your choice\n\n")


	print("\n")

	TripleDES_plaintext_bytes = TripleDES_plaintext.encode()

	

	print("You have selected 3DES\n")
	TripleDES_backend = default_backend()
	TripleDES_key = os.urandom(24)  #This value is 24 becuase of 3DES different key lengths
	TripleDES_iv = os.urandom(8)
	TripleDES_nonce = os.urandom(8)

	if encryption_input =="1":
		mode = modes.ECB()
		print("You have selected ECB")
		print(mode)
	elif encryption_input =="2":
		mode = modes.CBC(AES_iv)
		print("You have selected CBC")
	elif encryption_input =="3":
		mode = modes.CFB(AES_iv)
		print("You have selected CFB")
	elif encryption_input =="4":
		mode = modes.OFB(AES_iv)
		print("You have selected OFB")
	elif encryption_input =="5":
		mode = modes.CTR(AES_nonce)
		print("You have selected CTR")
	else:
		print("Please input a number from 1-5")


	cipher = Cipher(algorithms.TripleDES(TripleDES_key), mode, backend=TripleDES_backend)
	TripleDES_encryptor = cipher.encryptor()
	cipher_text = TripleDES_encryptor.update(TripleDES_plaintext_bytes) + TripleDES_encryptor.finalize()
	TripleDES_decryptor = cipher.decryptor()
	plaintext_from_ciphertext = TripleDES_decryptor.update(cipher_text) + TripleDES_decryptor.finalize()



	print("This is the key that was used to encrypt:", TripleDES_key, "\n")
	print("This is the value of the Initization Vector that was used:", TripleDES_iv, "\n")
	print("This is the cipher text: ",cipher_text, "\n")
	
	print(mode, "this is the mode")


########################################  This following code does the decryption of the data

	print("\nThis is the plaintext decoded from the plaintext: ",plaintext_from_ciphertext)

########################################  This following code does the decryption of the data

	print("\nThis is the plaintext decoded from the plaintext: ",plaintext_from_ciphertext)






elif userinput == "4":     ###This is CAST-128!!!!!

	import os
	from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import padding

	
	

	CAST5_plaintext = input("Please enter the ciphertext of your choice\n\n")

#This pads the data to 128 byte chunks for use in some encryption models
	print("\n")

	CAST5_plaintext_bytes = CAST5_plaintext.encode()

	CAST5_padder = padding.PKCS7(128).padder()     #This creates the padding function, 

	CAST5_padded_data = CAST5_padder.update(CAST5_plaintext_bytes)   #This pads the data



	CAST5_padded_data += CAST5_padder.finalize()    #This finalizes the padded data

	print(CAST5_padded_data, "\n\n")       #This prints the padded data

#The padding portion of the code is done

#The following code does the encryption 	

	print("You have selected CAST5\n")
	CAST5_backend = default_backend()
	CAST5_key = os.urandom(16)
	CAST5_iv = os.urandom(8)
	cipher = Cipher(algorithms.CAST5(CAST5_key), modes.CFB(CAST5_iv), backend=CAST5_backend)
	CAST5_encryptor = cipher.encryptor()
	cipher_text = CAST5_encryptor.update(CAST5_plaintext_bytes) + CAST5_encryptor.finalize()
	CAST5_decryptor = cipher.decryptor()
	plaintext_from_ciphertext = CAST5_decryptor.update(cipher_text) + CAST5_decryptor.finalize()



	print("This is the key that was used to encrypt:", CAST5_key, "\n")
	print("This is the value of the Initization Vector that was used:", CAST5_iv, "\n")
	print("This is the cipher text: ",cipher_text, "\n")




	print("\nThis is the plaintext decoded from the plaintext: ",plaintext_from_ciphertext)

	

elif userinput == "5":


	import os
	from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
	from cryptography.hazmat.backends import default_backend
	

	ARC4_plaintext = input("Please enter the ciphertext of your choice\n\n")

#This pads the data to 128 byte chunks for use in some encryption models
	print("\n")

	ARC4_plaintext_bytes = ARC4_plaintext.encode()


	ARC4_key = os.urandom(16)	
	algorithm = algorithms.ARC4(ARC4_key)
	ARC4_cipher = Cipher(algorithm, mode=None, backend=default_backend())
	ARC4_encryptor = ARC4_cipher.encryptor()
	ARC4_ct = ARC4_encryptor.update(ARC4_plaintext_bytes)
	ARC4_decryptor = ARC4_cipher.decryptor()
	ARC4_decryptor.update(ARC4_ct)

	print(ARC4_ct)

 






###This is the RSA help file

###RSA is an Asymetric algorithm. This means that there is a key that encrypts the data and another key that will decrypt the data. The structure that RSA follows is called the Public/Private key pair. The naming is quite literal as the public key is shared to the public and the private key is kept private and only you should have the key. The way that RSA works is that data is encrypted with the public key and is decrypted with the private key. The reason that this structure works is that encryption algorithm is based off multiplying very large prime numbers tthatogether. This is because the product of 2 very large prime numbers is extremely hard to factor (find the numbers that will multiply together to get the product). The reason that prime numbers are used is that the no otheractors of prime numbers are 1 and themselves, no other numbers will multiply to them. Because the the data is encrypted with the public key and is decrypted with the private key from the same keypair, this means that the keys have to be related somehow. I will explain below

# The public key contains modulus that was used, this is usually set to the variable "n", ******This needs to be clarified and written in plain english

# The public key contains the public exponent, this is usually set as the variable "e", 



#To make this encryption work, the private key has the above data, identical to the ppublic key given that they are from the same keypair

# Contains the private exponent, usually saved as the variabe "d"

# Contains the factors, usually written as "p" and "q" 

# Contains the variable "u", the CRT coefficient (Chinese Remainder Theorem)






####This is the AES help file



#AES stands for "Advanced Encryption Standard". It is the modern standard for encrypting and decrypting data. The encryption algortihm that AES uses is the Rijndael algortihm. As its current iteration, it can use 3 different key sizes with those being 128, 192, or 256 bits long. The block size for the plaintext is 128 bits long. This algorithm performs a different number of rounds of encryption depending on what key size that it was given. The number of rounds are 10,12, and 14 in relation to the key size that it was given. The larger the key, the more rounds of encryption gets performed.

#AES uses a substitution-permutation network as this proves to be computationally quick in both hardware and software. During each round there are 4 different types of susbitution/permutation that occur with diffferent keys on each round. As just mentioned, the keys used in each round are called sub-keys. They are all derived from the key that was supplied at the beginning (128/192/256 bits long) and several go through several permutations to get smaller keys (128 bits) that are used for each encryption round. Each round, a new key is generated.
S
#For the actual algorithm, in each round there are 4 steps. After the key for the round is decided, the plaintext will be put through in order; SubBytes, ShiftRows, MixColumns, and AddRoundKey. These 4 steps are all performed on each round except for MixColumns which does not get executed on the last round on all 3 variations of rounds (10,12,14)











###This is the help file for the CAST-128 cipher 

#https://tools.ietf.org/html/rfc2144     This is the RFC page for the CAST-128 algorithm

##The CAST-128(CAST5) is a symetric encryption block-cipher algorithm. This means that the the key used to encrypt the data is the same key that is used to decrypt the data. Block-Cipher indicates that it encrypts each block of data independently of the rest. This algorithm encrypts the data by performing 12 to 16 rounds of encryption using a festiel network. This algorithm can accept up to 64 bit inputs and have a key size from 40-128(Hence the 128 in the name).

##CAST-128 is compatible with the 5 different methods of encrypting as you had seen in the option menu. As you could see the options were as follows: Electronic Code Book(ECB)     Cipher Block Chaining (CBC)      Cipher FeedBack Mode (CFB)       Output Feedback Mode (OFB)      Counter Mode (CTR)

#In order to understand the following encryption methods, you will need to know some terms regarding to these above methodologies

#Key = This is almost always a cryptographically secure  randomly generated value, that is again almost always generated in multiples of 8 bits. This is because all of the encryption algortihms seen above use key sizes that are multiples of 8 bits. Depending on the algoritm and how secure you would to encrypt your data, there are different lengths of keys that you can use for each encryption algorithm

#Intialization Vector (Commonly referred to as IV) = This is usually a cryptographically securely generated value, almost always in 8-bit integers. What the IV is used for is to initailize the encryption algortihm at the beginning. This needs to be known to both parties as both encryption and decryption will need the same value to generate the same data

#Nonce = This is a number value that will only be used once in the initialization of the encryption process, this is only used in the Counter (CTR) mode. After the intialization, the value is thrown away and will not be used again. It is very similiar in fashioin to the Intialization vector as this Initiailizes the counter at a random number. No 2 Nonces should be used with the same key because of the nature of the counter. Using the nonce twice with the same key will provide the same cryptographic output. A nonce can be used again but has to be used with a different key to avoid cryptographic flaws

#How this algorfithm decides on how many rounds of ecnryption to perform depends on the length of the key. Becauase the algorithm can take 40-128 bits in they, no fixed set round of encryption will do. The algorithm stays with the 12 rounds of encryption until the key is 80 bits long. It is at this point that the algorithm switches to 16 rounds. All keys that will be used in this algorithm will need to be a multiple of 8 bits as this is the only way this algorithm will accept the key. 

#Upon recieiving the key and the data, as mentioned before the data will go through 8*32 S-boxes**** (Substitution boxes) which are based on "bent***" functions, subtraction, addition, and XORing (Exclusive or***). This is called the fiestel network. (This might need a correction)The subtitution boxes are fixed binary data in which the input data from the plaintext is XOR'ed with. After that binary math(subtraction, addition, XOR'ing) is round dependent which inidicates that every round the algorithm uses a different method. This is calculated mathematically with ""***Input the math function from the RFC page here*****












