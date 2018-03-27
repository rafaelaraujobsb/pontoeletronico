import hashlib

def cryptmd5(password):
	return hashlib.md5(password.encode()).hexdigest()