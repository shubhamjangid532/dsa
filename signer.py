import hmac
import hashlib

def create_signature(secret_key, message):
    # Convert string to bytes
    key_bytes = secret_key.encode('utf-8')
    msg_bytes = message.encode('utf-8')
    
    # Create HMAC using SHA256
    # digest() gives us the raw math result
    # hexdigest() turns it into a readable string (like 'a3f5...')
    signature = hmac.new(key_bytes, msg_bytes, hashlib.sha256).hexdigest()
    
    return signature

if __name__ == "__main__":
    secret = "my_super_secret_key"
    
    # 1. Server issues a token
    payload = '{"role": "user"}'
    original_sig = create_signature(secret, payload)
    print(f"Original Signature: {original_sig}")
    
    # 2. Hacker tries to tamper
    tampered_payload = '{"role": "admin"}'
    # The hacker sends 'tampered_payload' but keeps the 'original_sig' 
    # because they don't know the secret to make a new one.
    
    # 3. Server validates
    new_sig = create_signature(secret, tampered_payload)
    
    if new_sig == original_sig:
        print("ACCESS GRANTED (This should not happen)")
    else:
        print("ACCESS DENIED: Signature Mismatch!")



"""
Initialize min_price (to infinity or the first element) and max_profit (to 0).

Loop through prices.

  min_price = min(min_price, prices[idx])
  max_profit = max(max_profit, prices[idx]-min_price)

Update max_profit.

"""