from Crypto.PublicKey import RSA
import pickle

#this should loop around until a delimeter is read
#or something similar
rcstring = s.recv(2048)
 
#this object is of type RSAobj_c, which only has public key
#encryption is possible, but not decryption
publickey = pickle.loads(rcstring)

print(publickey)



