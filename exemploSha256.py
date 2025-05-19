import hashlib, json
bloco = {
    "timestamp": "2025-05-20T00:00:00Z",
    "nonce": 1764,
    "index": 42,
    "previous_hash": "0006f0f9eb756436f00a011016cc924ee044af908c1f001c98e2939dffd0756a",
    "data": {
        "sender": "user.1",
        "amount": 1.98,
        "recipient": "user.2"
    }
}
# Gera o hash do bloco 
bloco_serializado = json.dumps(bloco, sort_keys=True).encode()
hash = hashlib.sha256(bloco_serializado).hexdigest()
print(hash)
# 00037afc4699b2ba3c2c59d3541a4937449d5b5dcd3ea58fb007eb9a4aae9a63
# 0339b668bc69222fb5d71c01aca107b9701297b590e1a0af22b68a15eded77ae