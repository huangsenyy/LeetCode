/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 同样的算法C++ 12ms, Python需要92ms
    bool isBalanced(TreeNode* root) {
        return this->calHeight(root) != -1;     
    }
    
    int calHeight(TreeNode* node) {
        if(node == NULL) {
            return 0;
        }
        
        int left_height = 0;
        int right_height = 0;
        left_height += calHeight(node->left);
        right_height += calHeight(node->right);
        if (abs(left_height-right_height)>1 || left_height == -1 || right_height == -1) {
            return -1;
        }
        return max(left_height, right_height) + 1;
    }
};


