import math

h = 1500 * 8 / 4000000
lda = 212
K = 20
rho = lda * h

b = []
for k in range(K):
    bk = (rho**k) * math.exp(-rho) / math.factorial(k)
    b.append(bk)
    print(f"b[{k}]: {b[k]}")

pi = []
pik = 1
pi.append(pik)


for k in range(1, K + 1):
    pik = pi[k - 1] - pi[0] * b[k - 1]
    for j in range(1, k):
        pik -= pi[j] * b[k - j]

    pik /= b[0]
    pi.append(pik)

pi_sum = 0
for k in range(K + 1):
    pi_sum += pi[k]

for k in range(K + 1):
    pi[k] /= pi_sum
    print(f"pi[{k}]: {pi[k]}")

p = []
for k in range(K + 1):
    pk = pi[k] / (pi[0] + rho)
    p.append(pk)
    print(f"p[{k}]: {p[k]}")

answer = 0
for k in range(1, K + 1):
    answer += p[k] * k

answer += (1 - 1 / (pi[0] + rho)) * (K + 1)

print("------------------------------")
print(f"answer: {answer}")
print("------------------------------")
