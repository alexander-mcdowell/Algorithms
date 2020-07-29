#include <stdlib.h>
#include <stdio.h>

struct node {
    char label;
    int value;
    struct node *left, *right;
};
typedef struct node node;

struct queue {
    node* array[100];
    int end;
};
typedef struct queue queue;

void push(queue *q, node* element) {
    (q->end)++;
    q->array[q->end] = element;
}

node* pop(queue *q) {
    node* popped = q->array[0];
    for (int i = 1; i <= q->end; i++) q->array[i - 1] = q->array[i];
    (q->end)--;
    return popped;
}

enum Direction {LEFT, RIGHT};

node createRoot(char label, int value) { return (node) {label, value, NULL, NULL}; }

void addNode(node* root, char label, int value, enum Direction dir) {
    node* child = (node *) malloc(sizeof(node));
    child->label = label;
    child->value = value;
    child->left = NULL;
    child->right = NULL;

    if (dir == LEFT) root->left = child;
    else root->right = child;
}

void removeNode(node* root, char label) {
    int found = 0;
    // Check the left side and see if the label matches. If so, recursively remove all children.
    if (root->left != NULL) {
        if (root->left->label == label) {
            if (root->left->left != NULL) removeNode(root->left, root->left->left->label);
            if (root->left->right != NULL) removeNode(root->left, root->left->right->label);

            // Free the allocated memory and sever the connection.
            free(root->left);
            root->left = NULL;

            found = 1;
        }
    }
    // Check the right side and see if the label matches. If so, recursively remove all children.
    if (root->right != NULL && !found) {
        if (root->right->label == label) {
            if (root->right->left != NULL) removeNode(root->right, root->right->left->label);
            if (root->right->right != NULL) removeNode(root->right, root->right->right->label);

            // Free the allocated memory and sever the connection.
            free(root->right);
            root->right = NULL;

            found = 1;
        }
    }
    // If the node is not found, move one layer down.
    if (!found) {
        if (root->left != NULL) removeNode(root->left, label);
        if (root->right != NULL) removeNode(root->right, label);
    }
}

void print(node* root, int depth) {
    for (int i = 0; i < depth; i++) (void) printf("--");
    (void) printf("{%c : %d}\n", root->label, root->value);

    if (root->left != NULL) print(root->left, depth + 1);
    if (root->right != NULL) print(root->right, depth + 1);
}

void depthFirst(node* root) {
    (void) printf("%c, ", root->label);
    if (root->left != NULL) depthFirst(root->left);
    if (root->right != NULL) depthFirst(root->right);
}

void breadthFirst(node* root) {
    queue q;
    q.end = -1;
    push(&q, root);
    node* popped;

    while (q.end != -1) {
        popped = pop(&q);
        (void) printf("%c, ", popped->label);
        if (popped->left != NULL) push(&q, popped->left);
        if (popped->right != NULL) push(&q, popped->right);
    }
}

void inorder(node* root) {
    if (root->left != NULL) inorder(root->left);
    (void) printf("%c, ", root->label);
    if (root->right != NULL) inorder(root->right);
}

void preorder(node* root) {
    (void) printf("%c, ", root->label);
    if (root->left != NULL) inorder(root->left);
    if (root->right != NULL) inorder(root->right);
}

void postorder(node* root) {
    if (root->left != NULL) inorder(root->left);
    if (root->right != NULL) inorder(root->right);
    (void) printf("%c, ", root->label);
}

int main(int argc, char const *argv[]) {
    node root = createRoot('A', 0);

    addNode(&root, 'B', 1, LEFT);
    addNode(&root, 'C', 2, RIGHT);
    addNode(root.left, 'D', 3, LEFT);
    addNode(root.left, 'E', 4, RIGHT);
    addNode(root.right, 'F', 5, LEFT);
    addNode(root.left->left, 'G', 6, LEFT);
    addNode(root.left->left, 'H', 7, RIGHT);
    addNode(root.right, 'I', 8, RIGHT);

    (void) printf("Initial tree:\n");
    print(&root, 0);

    (void) printf("Depth First Traversal: ");
    depthFirst(&root);
    (void) printf("\n");

    (void) printf("Breadth First Traversal: ");
    breadthFirst(&root);
    (void) printf("\n");

    (void) printf("Inorder Traversal: ");
    inorder(&root);
    (void) printf("\n");
    
    (void) printf("Preorder Traversal: ");
    preorder(&root);
    (void) printf("\n");

    (void) printf("Postorder Traversal: ");
    postorder(&root);
    (void) printf("\n");

    char label = 'B';
    removeNode(&root, label);

    (void) printf("Tree with element %c (and children) removed:\n", label);
    print(&root, 0);
    return 0;
}
