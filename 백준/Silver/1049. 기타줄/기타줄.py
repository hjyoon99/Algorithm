n, m = map(int, input().split(" "))
package = []
one = []
for _ in range(m):
    a, b = map(int, input().split(" "))
    package.append(a)
    one.append(b)

package.sort()
one.sort()

# 전부 낱개로 사는 경우
total_one = n * one[0]

# 몫만큼 패키지 + 나머지 낱개
total_package_one = (n // 6) * package[0] + (n % 6) * one[0]

# 전부 패키지
total_package = ((n // 6) + 1) * package[0]

answer = min(total_one, total_package_one, total_package)

print(answer)