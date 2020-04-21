'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  /    / \
 4   1  #  6
/  /    / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
'''

def valid_serialization(preorder):
    stack = []

    def pop_valid():
        if len(stack) >= 2 and stack[-1] == '#' and stack[-2] == '#':
            stack.pop()
            stack.pop()
            if not stack: return 'empty'
            stack[-1] = '#'
            return True 
        return False 

    for node in preorder.split(','):
        stack.append(node)
        while True:
            valid = pop_valid()
            if not valid: break
            if valid == 'empty': return False

    return len(stack) == 1 and stack[0] == '#'

