def highest_priority_number(nums):
    # 가능한 모든 곱의 경우를 구합니다.
    products = set()
    n = len(nums)
    for i in range(n):
        products.add(nums[i])
        for j in range(i + 1, n):
            products.add(nums[i] * nums[j])
            for k in range(j + 1, n):
                products.add(nums[i] * nums[j] * nums[k])
    
    # 우선순위에 따라 정렬
    sorted_products = sorted(products, key=lambda x: (x % 2 == 0, -x))
    
    # 가장 높은 우선순위의 수를 반환
    return sorted_products[0]

def main():
    a,b,c = map(int, input().split())
    nums = [a,b,c]
    result = highest_priority_number(nums)
    print(result)

if __name__ == "__main__":
    main()