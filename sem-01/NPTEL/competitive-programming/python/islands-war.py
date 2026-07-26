# islands war

N,M = map(int, input().split())
requests = []

for i in range(M):
    request = tuple(map(int, input().split()))
    requests.append(request)


requests = sorted(requests, key=lambda x: x[1])

bridge_drops=0
last_bridge = -1

for request in requests:
    if last_bridge > request[0]:
        continue
    else:
        last_bridge=request[1]
        bridge_drops+=1
    
    print(f"Last Bridge = {last_bridge}")
    print(f"bridge_drops = {bridge_drops}")



print(bridge_drops)