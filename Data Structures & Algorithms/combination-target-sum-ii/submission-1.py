class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(start,cur,total):
            if target==total:
                res.append(cur.copy())
                return
            if total > target:
                return 

            prev=-1
            for i in range(start,len(candidates)):
                if candidates[i]==prev:
                    continue

                cur.append(candidates[i])
                dfs(i+1,cur,total+candidates[i])
                cur.pop()
                prev=candidates[i]
        dfs(0,[],0)
        return res


        