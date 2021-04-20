/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        
        Stack<Node> leftStack = new Stack<>();
        List<Integer> result = new LinkedList<>();
        Node cur = root;
        
        while (true) { 
            
            while (cur != null) {
                result.add(cur.val);
                if (cur.children.isEmpty()) break;
                Collections.reverse(cur.children);
                leftStack.addAll(cur.children);
                cur = leftStack.pop();
            }
            
            if (leftStack.isEmpty()) break;
            cur = leftStack.pop();
            
        }
        
        
        return result;
    }
}