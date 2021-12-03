from Crypt import Crypt

test_crpt = Crypt()

originalString = "password"
secretKey = '1234567890123456'
enc_key = test_crpt.encrypt(originalString, secretKey)
print("enc_key: ", enc_key)

dec_key = test_crpt.decrypt(enc_key, secretKey)
print("dec_key: ", dec_key)

print("done")