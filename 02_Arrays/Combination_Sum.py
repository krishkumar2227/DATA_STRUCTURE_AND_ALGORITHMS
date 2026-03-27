def combinationSum(candidates, target):
    result = []
    candidates.sort()  

    def dfs(index, current, total):
       
        if total == target:
            result.append(current[:])
            return
        
        for i in range(index, len(candidates)):
            
            if total + candidates[i] > target:
                break
            
           
            current.append(candidates[i])
            
            
            dfs(i, current, total + candidates[i])
            
            
            current.pop()

    dfs(0, [], 0)
    return result