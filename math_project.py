import hashlib
import random

# Step 1: Generate large prime for modulus
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_large_prime():
    while True:
        num = random.randint(10000, 99999)
        if is_prime(num):
            return num

# Step 2: Modular hashing function
def modular_hash(password, e=7):
    p = generate_large_prime()
    total = 0
    for ch in password:
        total += pow(ord(ch), e, p)
    hash_value = total % p
    return hash_value, p  # return both hash and prime used

# Step 3: Storing hashed password (Simulation)
def store_password(password):
    hashed, prime = modular_hash(password)
    print(f"\n[+] Password Stored Securely:")
    print(f"    Hash Value: {hashed}")
    print(f"    Prime Used: {prime}")
    return hashed, prime

# Step 4: Verifying password
def verify_password(input_password, stored_hash, prime, e=7):
    total = 0
    for ch in input_password:
        total += pow(ord(ch), e, prime)
    verify_hash = total % prime
    return verify_hash == stored_hash

# --- Main Program ---
print("🔐 Modular Arithmetic Based Password Hashing System 🔢")

password = input("Enter your password: ")
stored_hash, prime = store_password(password)

print("\n--- Password Verification ---")
verify = input("Re-enter your password to verify: ")

if verify_password(verify, stored_hash, prime):
    print("✅ Password Verified Successfully! (Hash matched)")
else:
    print("❌ Verification Failed! Password does not match.")