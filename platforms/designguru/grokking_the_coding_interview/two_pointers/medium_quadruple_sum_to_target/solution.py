class Solution:
    def searchQuadruplets(self, arr, target):
        quadruplets = []
        arr.sort()

        a = 0
        for a in range(0, len(arr) - 3):
            if a > 0 and arr[a - 1] == arr[a]:
                continue
            for b in range(a + 1, len(arr) - 2):
                if b > a + 1 and arr[b - 1] == arr[b]:
                    continue
                c = b + 1
                d = len(arr) - 1
                while c < d:
                    quadruplet_sum = arr[a] + arr[b] + arr[c] + arr[d]
                    if quadruplet_sum == target:
                        quadruplets.append([arr[a], arr[b], arr[c], arr[d]])
                        c += 1
                        while c < d and arr[c - 1] == arr[c]:
                            c += 1
                        d -= 1
                        while c < d and arr[d] == arr[d + 1]:
                            d -= 1

                    elif quadruplet_sum > target:
                        d -= 1
                    else:
                        c += 1

        return quadruplets
