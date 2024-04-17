def solution(skill, skill_trees):
    ans = 0
    for i in range(len(skill_trees)):
        stack = []
        for j in range(0,len(skill_trees[i])):          
            if skill_trees[i][j] in skill:
                stack.append(skill_trees[i][j])
        if skill.startswith(''.join(stack)) == True:
            ans += 1
    return ans